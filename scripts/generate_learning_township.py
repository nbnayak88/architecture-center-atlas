#!/usr/bin/env python3
"""Generate SuccessLabs Learning Township from the authoritative HUB CSV."""
import csv, re, sys
from collections import Counter
from pathlib import Path

SOURCE = Path("township-source/successlabs_township_31680_learning_pathways.csv")
ROOT = Path("Learning Township")
FIELDS = ["Pathway ID","Index #","Unit ID","Unit Title","Sector Code","Sector Name","Academy Code","Academy Name","Series Code","Curriculum Tier","Tier Level (1-5)","Learning Format","Objective","Duration","Student Output","Unit Occupancy Status","Allocated Member"]
EXPECTED = 31680

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def clean(s):
    return str(s).replace("\r"," ").replace("\n"," ").strip()

def main():
    if not SOURCE.exists():
        sys.exit(f"Missing source: {SOURCE}. Upload the authoritative HUB CSV to this exact path.")
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        reader=csv.DictReader(handle)
        missing=set(FIELDS)-set(reader.fieldnames or [])
        if missing: sys.exit(f"Missing columns: {sorted(missing)}")
        records=list(reader)
    if len(records)!=EXPECTED: sys.exit(f"Expected {EXPECTED} rows, found {len(records)}")
    ids=[r["Pathway ID"] for r in records]
    if len(set(ids))!=EXPECTED: sys.exit("Duplicate Pathway IDs detected")
    units={r["Unit ID"] for r in records}
    if len(units)!=792: sys.exit(f"Expected 792 units, found {len(units)}")
    academy_codes=sorted({r["Academy Code"] for r in records})
    if len(academy_codes)!=6: sys.exit("Expected six academies")
    tiers=sorted({r["Curriculum Tier"] for r in records})
    formats=sorted({r["Learning Format"] for r in records})
    if len(tiers)!=5 or len(formats)!=8: sys.exit("Expected 5 tiers and 8 formats")
    sectors=sorted({r["Sector Code"] for r in records})
    if len(sectors)!=11: sys.exit("Expected 11 sectors")
    seen=set()
    for r in records:
        series=r["Series Code"]
        path=ROOT / f'{r["Academy Code"]}-{slug(r["Academy Name"])}' / series / f'{r["Sector Code"]}-{slug(r["Sector Name"])}' / f'{r["Curriculum Tier"]}-{r["Tier Level (1-5)"]}' / slug(r["Learning Format"])
        if path in seen: sys.exit(f"Duplicate target folder: {path}")
        seen.add(path)
        path.mkdir(parents=True,exist_ok=True)
        text=f"""# {clean(r['Unit Title'])} — {clean(r['Learning Format'])}

**Pathway ID:** `{clean(r['Pathway ID'])}`  
**Catalog Index:** {clean(r['Index #'])}  
**Unit ID:** {clean(r['Unit ID'])}  
**Academy:** {clean(r['Academy Name'])} ({clean(r['Academy Code'])})  
**Series:** {clean(series)}  
**GICS Sector:** {clean(r['Sector Name'])} ({clean(r['Sector Code'])})  
**Curriculum Tier:** {clean(r['Curriculum Tier'])} (Level {clean(r['Tier Level (1-5)'])})  
**Learning Format:** {clean(r['Learning Format'])}  
**Duration:** {clean(r['Duration'])}  
**Township Occupancy:** {clean(r['Unit Occupancy Status'])}

## Learning objective
{clean(r['Objective'])}

## Student output
{clean(r['Student Output'])}

## Architecture-first learning principle
Teach sector and domain architecture through business outcomes, capabilities, value streams, information, governance, integration, and evidence. Product and vendor technologies are optional implementation examples. Reference applicable TOGAF, BIZBOK, BABOK, DAMA-DMBOK, APQC, GICS and other international frameworks.

## Publication note
This is a HUB catalog record, **not proof that a course is live or purchasable**. Township occupancy is not publication status. Allocated member names are intentionally excluded from the public repository for privacy.
"""
        (path/"README.md").write_text(text,encoding="utf-8")
    assert len(seen)==EXPECTED
    ROOT.mkdir(exist_ok=True)
    with (ROOT/"catalog.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=[x for x in FIELDS if x!="Allocated Member"])
        writer.writeheader()
        for r in records: writer.writerow({k:r[k] for k in writer.fieldnames})
    (ROOT/"README.md").write_text(
        "# SuccessLabs Academy — Learning Township\n\n"
        "**31,680 HUB catalog pathways** = 792 learning units × 5 curriculum tiers × 8 learning formats.\n\n"
        "Explore **6 academies → 12 series → 11 GICS sectors → 5 curriculum tiers → 8 learning formats**.\n\n"
        "This township is separate from the **2,640 vendor-neutral Architecture Learning Journeys** under `learning-journeys/`.\n\n"
        "The source of truth is the uploaded HUB CSV. The published catalog excludes allocated-member names. "
        "Available/Occupied describes township allocation, **not** live-course status.\n\n"
        "See [catalog.csv](catalog.csv) for a searchable catalog index.\n",encoding="utf-8")
    print(f"Created {len(seen):,} unique pathway folders across {len(units)} units.")

if __name__=="__main__":
    main()
