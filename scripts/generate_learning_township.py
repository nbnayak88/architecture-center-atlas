#!/usr/bin/env python3
"""Generate SuccessLabs Learning Township from the authoritative HUB CSV."""
import csv, re, sys
from collections import Counter
from pathlib import Path

SOURCE = Path("township-source/successlabs_township_31680_learning_pathways.csv")
ROOT = Path("Learning Township")
FIELDS = ["Pathway ID","Index #","Unit ID","Unit Title","Sector Code","Sector Name","Academy Code","Academy Name","Series Code","Curriculum Tier","Tier Level (1-5)","Learning Format","Objective","Duration","Student Output","Unit Occupancy Status","Allocated Member"]
EXPECTED = 31680
SECTOR_ORDER = {'ENE':1,'MAT':2,'IND':3,'CD':4,'CS':5,'HC':6,'FIN':7,'IT':8,'COM':9,'UT':10,'RE':11}

TIER_FOLDERS = {1:"01-Pre-Foundation",2:"02-Foundation",3:"03-Essentials",4:"04-Advanced",5:"05-Ultimate"}

ACADEMY_FOLDERS = {
    "HR": "01-HR-Human-Capital-Capability-Academy-Workforce-Monday",
    "CRM": "02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday",
    "FI": "03-FI-Finance-Capability-Academy-Finance-Wednesday",
    "PROC": "04-PROC-Procurement-Capability-Academy-Procurement-Thursday",
    "SCM": "05-SCM-Supply-Chain-Management-Capability-Academy-Supply-Chain-Friday",
    "BTM": "06-BTM-Business-Transformation-Capability-Academy-Transformation-Saturday",
    "LIT": "07-LIT-Leadership-and-Identity-Transformation-Capability-Academy-Source-Sunday",
}

HR_SERIES_NAMES = {
    "HR01": "HR01-AWF1-Architecting-Autonomous-Workforce-Foundations",
    "HR02": "HR02-ATA2-Architecting-Autonomous-Talent-Acquisition",
    "HR03": "HR03-APH3-Architecting-High-Performance-Organizations",
    "HR04": "HR04-AGL4-Architecting-Growth-Leadership",
    "HR05": "HR05-ARP5-Architecting-Rewards-Performance-Excellence",
    "HR06": "HR06-ALM6-Architecting-Continuous-Learning-Mobility",
    "HR07": "HR07-APE7-Architecting-Autonomous-Payroll-Enterprises",
    "HR08": "HR08-AWT8-Architecting-Workforce-Time-Operations",
    "HR09": "HR09-AWI9-Architecting-Workforce-Intelligence",
    "HR10": "HR10-ADX0-Architecting-Digital-Employee-Experience",
    "HR11": "HR11-AAI1-Architecting-AI-Powered-HR-Enterprises",
    "HR12": "HR12-AIG2-Architecting-Connected-HR-Enterprises",
}

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
    if set(academy_codes) != set(ACADEMY_FOLDERS)-{"LIT"}: sys.exit(f"Unexpected source academies: {academy_codes}")
    tiers=sorted({r["Curriculum Tier"] for r in records})
    formats=sorted({r["Learning Format"] for r in records})
    if len(tiers)!=5 or len(formats)!=8: sys.exit("Expected 5 tiers and 8 formats")
    sectors=sorted({r["Sector Code"] for r in records})
    if len(sectors)!=11: sys.exit("Expected 11 sectors")
    if set(sectors) != set(SECTOR_ORDER): sys.exit('Unexpected GICS sector codes')
    seen=set()
    origin_units={}
    for r in records:
        series=r["Series Code"]
        tier_number=int(r["Tier Level (1-5)"])
        if tier_number not in TIER_FOLDERS: sys.exit("Invalid tier number")
        series_folder=HR_SERIES_NAMES.get(series,series) if r["Academy Code"]=="HR" else series
        path=ROOT / ACADEMY_FOLDERS[r["Academy Code"]] / series_folder / f'{SECTOR_ORDER[r["Sector Code"]]:02d}-{series}-{r["Sector Code"]}-{slug(r["Sector Name"])}' / TIER_FOLDERS[tier_number] / slug(r["Learning Format"])
        origin_dir=path.parent.parent/"0-The-Origin-Story"
        origin_units[str(origin_dir)]=(r["Unit ID"],r["Unit Title"])
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
    lit=ROOT/ACADEMY_FOLDERS["LIT"]
    lit.mkdir(parents=True,exist_ok=True)
    (lit/"README.md").write_text("# LIT — Leadership and Identity Transformation Capability Academy\\n\\n**Source Sunday**\\n\\nStatus: New academy scaffold. The authoritative HUB CSV contains six academies; no LIT series, pathways, or courses have been invented.\\n\\nFocus: leadership identity, values, purpose, self-awareness, systems thinking, responsible transformation and evidence-based personal growth.\\n",encoding="utf-8")
    assert len(seen)==EXPECTED
    if len(origin_units)!=792: sys.exit("Expected 792 unique Origin Story units")
    for origin_path,(unit_id,unit_title) in origin_units.items():
        origin=Path(origin_path)
        origin.mkdir(parents=True,exist_ok=True)
        (origin/"README.md").write_text(
            "# The Origin Story — "+clean(unit_title)+"\\n\\n"
            +"**Unit ID:** "+clean(unit_id)+"\\n\\n"
            +"**Level:** 0 — The Origin Story\\n\\n"
            +"**Status:** Curriculum placeholder; not a published HUB pathway.\\n\\n"
            +"Explore the origin, evolution, business context and architecture foundations of this unit.\\n\\n"
            +"The authoritative HUB CSV contains Levels 1–5 only. No Level 0 Pathway ID or content is invented.\\n",
            encoding="utf-8")
    ROOT.mkdir(exist_ok=True)
    with (ROOT/"catalog.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=[x for x in FIELDS if x!="Allocated Member"])
        writer.writeheader()
        for r in records: writer.writerow({k:r[k] for k in writer.fieldnames})
    (ROOT/"README.md").write_text(
        "# SuccessLabs Academy — Learning Township\n\n"
        "**31,680 HUB catalog pathways** = 792 learning units × 5 curriculum tiers × 8 learning formats.\n\n"
        "Explore **7 academy folders (6 populated from HUB, 1 new LIT scaffold) → 12 series → 11 GICS sectors → 6 curriculum tiers (0–5); formats available for Levels 1–5**.\n\n"
        "This township is separate from the **2,640 vendor-neutral Architecture Learning Journeys** under `learning-journeys/`.\n\n"
        "The source of truth is the uploaded HUB CSV. The published catalog excludes allocated-member names. "
        "Available/Occupied describes township allocation, **not** live-course status.\n\n"
        "See [catalog.csv](catalog.csv) for a searchable catalog index.\n",encoding="utf-8")
    print(f"Created {len(seen):,} HUB pathway folders plus {len(origin_units):,} Origin Story placeholders.")

if __name__=="__main__":
    main()
