#!/usr/bin/env python3
"""Generate SuccessLabs Learning Township from the authoritative HUB CSV."""
import csv, re, sys
from collections import Counter
from pathlib import Path

SOURCE = Path("township-source/successlabs_township_31680_learning_pathways.csv")
ROOT = Path("Learning Township")
FIELDS = ["Pathway ID","Index #","Unit ID","Unit Title","Sector Code","Sector Name","Academy Code","Academy Name","Series Code","Curriculum Tier","Tier Level (1-5)","Learning Format","Objective","Duration","Student Output","Unit Occupancy Status","Allocated Member"]
EXPECTED = 31680
LIT_EXPECTED = 5280
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

SERIES_FOLDER_NAMES = dict(HR_SERIES_NAMES)
# CRM — canonical MDM code + Wisdom code + BootCamp title
SERIES_FOLDER_NAMES["CRM01"] = "CRM01-ACM1-Architecting-Connected-Customer-Enterprises"
SERIES_FOLDER_NAMES["CRM02"] = "CRM02-AMK2-Architecting-Autonomous-Customer-Engagement"
SERIES_FOLDER_NAMES["CRM03"] = "CRM03-ASL3-Architecting-Intelligent-Revenue-Organizations"
SERIES_FOLDER_NAMES["CRM04"] = "CRM04-ACO4-Architecting-Digital-Commerce-Enterprises"
SERIES_FOLDER_NAMES["CRM05"] = "CRM05-ACS5-Architecting-Autonomous-Customer-Service"
SERIES_FOLDER_NAMES["CRM06"] = "CRM06-ACX6-Architecting-Exceptional-Customer-Experiences"
SERIES_FOLDER_NAMES["CRM07"] = "CRM07-APR7-Architecting-Recurring-Revenue-Enterprises"
SERIES_FOLDER_NAMES["CRM08"] = "CRM08-AOF8-Architecting-Autonomous-Customer-Operations"
SERIES_FOLDER_NAMES["CRM09"] = "CRM09-ADI9-Architecting-Customer-Intelligence"
SERIES_FOLDER_NAMES["CRM10"] = "CRM10-AEX0-Architecting-Digital-Customer-Experiences"
SERIES_FOLDER_NAMES["CRM11"] = "CRM11-AAI1-Architecting-AI-Powered-Customer-Enterprises"
SERIES_FOLDER_NAMES["CRM12"] = "CRM12-AIG2-Architecting-Connected-Customer-Ecosystems"
# FI — canonical MDM code + Wisdom code + BootCamp title
SERIES_FOLDER_NAMES["FI01"] = "FI01-AFR1-Architecting-Autonomous-Financial-Close"
SERIES_FOLDER_NAMES["FI02"] = "FI02-APT2-Architecting-Autonomous-Payables"
SERIES_FOLDER_NAMES["FI03"] = "FI03-AOT3-Architecting-Intelligent-Revenue-Operations"
SERIES_FOLDER_NAMES["FI04"] = "FI04-ATX4-Architecting-Digital-Tax-Enterprises"
SERIES_FOLDER_NAMES["FI05"] = "FI05-ATR5-Architecting-Autonomous-Treasury-Operations"
SERIES_FOLDER_NAMES["FI06"] = "FI06-AFP6-Architecting-Enterprise-Financial-Planning"
SERIES_FOLDER_NAMES["FI07"] = "FI07-ACC7-Architecting-Cost-Profitability-Excellence"
SERIES_FOLDER_NAMES["FI08"] = "FI08-AFA8-Architecting-Enterprise-Asset-Accounting"
SERIES_FOLDER_NAMES["FI09"] = "FI09-AGR9-Architecting-Financial-Governance-Risk"
SERIES_FOLDER_NAMES["FI10"] = "FI10-AFI0-Architecting-Financial-Intelligence"
SERIES_FOLDER_NAMES["FI11"] = "FI11-AAI1-Architecting-AI-Powered-Finance-Enterprises"
SERIES_FOLDER_NAMES["FI12"] = "FI12-AIG2-Architecting-Connected-Financial-Enterprises"
# PROC — canonical MDM code + Wisdom code + BootCamp title
SERIES_FOLDER_NAMES["PROC01"] = "PROC01-APR1-Architecting-Autonomous-Procurement-Strategy"
SERIES_FOLDER_NAMES["PROC02"] = "PROC02-ASR2-Architecting-Intelligent-Supplier-Sourcing"
SERIES_FOLDER_NAMES["PROC03"] = "PROC03-ASN3-Architecting-Contract-Excellence"
SERIES_FOLDER_NAMES["PROC04"] = "PROC04-ASU4-Architecting-Supplier-Relationship-Excellence"
SERIES_FOLDER_NAMES["PROC05"] = "PROC05-APO5-Architecting-Autonomous-Procure-to-Pay"
SERIES_FOLDER_NAMES["PROC06"] = "PROC06-ARI6-Architecting-Resilient-Supply-Operations"
SERIES_FOLDER_NAMES["PROC07"] = "PROC07-AQC7-Architecting-Supplier-Quality-Performance-Excellence"
SERIES_FOLDER_NAMES["PROC08"] = "PROC08-ASP8-Architecting-Spend-Optimization-Excellence"
SERIES_FOLDER_NAMES["PROC09"] = "PROC09-ARG9-Architecting-Risk-Sustainable-Procurement"
SERIES_FOLDER_NAMES["PROC10"] = "PROC10-AAN0-Architecting-Procurement-Intelligence"
SERIES_FOLDER_NAMES["PROC11"] = "PROC11-AAI1-Architecting-AI-Powered-Procurement-Enterprises"
SERIES_FOLDER_NAMES["PROC12"] = "PROC12-AIG2-Architecting-Connected-Procurement-Enterprises"
# SCM — canonical MDM code + Wisdom code + BootCamp title
SERIES_FOLDER_NAMES["SCM01"] = "SCM01-ASC1-Architecting-Autonomous-Supply-Chain-Strategy"
SERIES_FOLDER_NAMES["SCM02"] = "SCM02-APS2-Architecting-Intelligent-Demand-Planning"
SERIES_FOLDER_NAMES["SCM03"] = "SCM03-APN3-Architecting-Integrated-Supply-Planning"
SERIES_FOLDER_NAMES["SCM04"] = "SCM04-AMP4-Architecting-Smart-Manufacturing"
SERIES_FOLDER_NAMES["SCM05"] = "SCM05-ADL5-Architecting-Autonomous-Logistics-Transportation"
SERIES_FOLDER_NAMES["SCM06"] = "SCM06-AIN6-Architecting-Resilient-Inventory-Management"
SERIES_FOLDER_NAMES["SCM07"] = "SCM07-AQC7-Architecting-Quality-Compliance-Excellence"
SERIES_FOLDER_NAMES["SCM08"] = "SCM08-ACM8-Architecting-Supplier-Collaboration-Excellence"
SERIES_FOLDER_NAMES["SCM09"] = "SCM09-ASD9-Architecting-Sustainable-Supply-Chains"
SERIES_FOLDER_NAMES["SCM10"] = "SCM10-AAN0-Architecting-Supply-Chain-Intelligence"
SERIES_FOLDER_NAMES["SCM11"] = "SCM11-AAI1-Architecting-AI-Powered-Supply-Chain-Enterprises"
SERIES_FOLDER_NAMES["SCM12"] = "SCM12-AIG2-Architecting-Connected-Supply-Chain-Ecosystems"
# BTM — canonical MDM code + Wisdom code + BootCamp title
SERIES_FOLDER_NAMES["BTM01"] = "BTM01-ABT1-Architecting-Autonomous-Enterprise-Strategy"
SERIES_FOLDER_NAMES["BTM02"] = "BTM02-ARP2-Architecting-Future-Ready-Enterprise-Architecture"
SERIES_FOLDER_NAMES["BTM03"] = "BTM03-APM3-Architecting-Process-Driven-High-Performance-Enterprises"
SERIES_FOLDER_NAMES["BTM04"] = "BTM04-ACH4-Architecting-Change-Ready-Adaptive-Organizations"
SERIES_FOLDER_NAMES["BTM05"] = "BTM05-AVP5-Architecting-Value-Driven-Transformation"
SERIES_FOLDER_NAMES["BTM06"] = "BTM06-ATD6-Architecting-Data-Driven-Enterprises"
SERIES_FOLDER_NAMES["BTM07"] = "BTM07-ATE7-Architecting-Digital-Cloud-Enabled-Enterprises"
SERIES_FOLDER_NAMES["BTM08"] = "BTM08-AIO8-Architecting-Connected-Enterprise-Ecosystems"
SERIES_FOLDER_NAMES["BTM09"] = "BTM09-ARG9-Architecting-Trust-Risk-Resilient-Enterprises"
SERIES_FOLDER_NAMES["BTM10"] = "BTM10-AAN0-Architecting-Transformation-Intelligence"
SERIES_FOLDER_NAMES["BTM11"] = "BTM11-AAI1-Architecting-AI-Powered-Enterprises"
SERIES_FOLDER_NAMES["BTM12"] = "BTM12-AEC2-Architecting-Sustainable-Future-Ready-Enterprises"

LIT_SERIES = {
    "LIT01": ("IDT1", "Architecting My Purpose & Identity"),
    "LIT02": ("IDT2", "Architecting a Growth Mindset Life"),
    "LIT03": ("IDT3", "Architecting Emotional Freedom"),
    "LIT04": ("IDT4", "Architecting Authentic Leadership"),
    "LIT05": ("IDT5", "Architecting an Intentional Life"),
    "LIT06": ("IDT6", "Architecting Continuous Learning"),
    "LIT07": ("IDT7", "Architecting a Balanced Digital Life"),
    "LIT08": ("IDT8", "Architecting Meaningful Relationships"),
    "LIT09": ("IDT9", "Architecting Integrity & Values"),
    "LIT10": ("IDT10", "Architecting a Fulfilling Life"),
    "LIT11": ("IDT11", "Architecting Inner Transformation"),
    "LIT12": ("IDT12", "Architecting a Better World"),
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
        series_folder=SERIES_FOLDER_NAMES.get(series,series)
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
    (lit/"README.md").write_text("# LIT — Leadership and Identity Transformation Capability Academy\\n\\n**Source Sunday**\\n\\nTwelve canonical MDM/Wisdom program folders. The 5,280 LIT pathway expansion remains on hold.\\n", encoding="utf-8")
    for mdm, (wisdom, title) in LIT_SERIES.items():
        folder = lit / f"{mdm}-{wisdom}-{re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder/"README.md").write_text(
            f"# {title}\\n\\n**MDM Code:** {mdm}  \\n**Wisdom Code:** {wisdom}  \\n"
            "**Academy:** LIT — Source Sunday  \\n**Status:** MDM scaffold only; 5,280-pathway expansion on hold.\\n\\n"
            "Five life areas: spiritual, social, academic, professional, personal. "
            "Future curriculum emphasizes activities, simulations, reflection, and evidence. "
            "No sector pathways or LMS identifiers have been created.\\n", encoding="utf-8")
    # Planned LIT pathways: 12 programs x 11 GICS sectors x 5 tiers x 8 HUB formats.
    # Reuse sector, tier, and format vocabulary from the authoritative HUB export;
    # do not invent HUB enrollment IDs, prices, or publication status.
    sector_labels = {}
    tier_labels = {}
    for r in records:
        sector_labels[r["Sector Code"]] = r["Sector Name"]
        tier_labels[int(r["Tier Level (1-5)"])] = r["Curriculum Tier"]
    lit_rows = []
    for mdm, (wisdom, title) in LIT_SERIES.items():
        series_folder = lit / f"{mdm}-{wisdom}-{re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-')}"
        for sector_code, order in sorted(SECTOR_ORDER.items(), key=lambda item: item[1]):
            sector_name = sector_labels[sector_code]
            sector_folder = series_folder / f"{order:02d}-{mdm}-{sector_code}-{slug(sector_name)}"
            origin = sector_folder / "0-The-Origin-Story"
            origin.mkdir(parents=True, exist_ok=True)
            (origin/"README.md").write_text(
                f"# The Origin Story — {title}\\n\\n**Sector:** {sector_name}  \\n"
                "**Level:** 0 — The Origin Story  \\n**Status:** Planned, not counted among 5,280 pathways.\\n\\n"
                "Explore the origins of identity, values, leadership and purpose in this sector.\\n",
                encoding="utf-8")
            for tier_number in sorted(TIER_FOLDERS):
                for fmt in formats:
                    planned_id = f"LIT-{mdm}-{sector_code}-L{tier_number}-{slug(fmt)}"
                    path = sector_folder / TIER_FOLDERS[tier_number] / slug(fmt)
                    path.mkdir(parents=True, exist_ok=True)
                    (path/"README.md").write_text(
                        f"# {title} — {fmt}\\n\\n"
                        f"**Planning Reference (not an LMS ID):** \`{planned_id}\`  \\n"
                        f"**MDM Code:** {mdm}  \\n**Wisdom Code:** {wisdom}  \\n"
                        f"**GICS Sector:** {sector_name} ({sector_code})  \\n"
                        f"**Curriculum Tier:** {tier_labels[tier_number]} (Level {tier_number})  \\n"
                        f"**Learning Format:** {fmt}  \\n**Status:** Planned; no live course or enrollment implied.\\n\\n"
                        "## Activity-first learning\\n"
                        "Explore an authentic sector-based leadership or identity challenge. "
                        "Complete a decision simulation, reflect on choices and consequences, "
                        "and produce evidence across spiritual, social, academic, professional, "
                        "and personal life goals. These are curriculum design intentions, not completed lesson plans.\\n",
                        encoding="utf-8")
                    lit_rows.append({
                        "Planning Reference": planned_id, "MDM Code": mdm, "Wisdom Code": wisdom,
                        "Program": title, "Sector Code": sector_code, "Sector Name": sector_name,
                        "Tier Level": tier_number, "Curriculum Tier": tier_labels[tier_number],
                        "Learning Format": fmt, "Status": "Planned", "LMS ID": ""})
    if len(lit_rows) != LIT_EXPECTED:
        sys.exit(f"Expected {LIT_EXPECTED} LIT pathways, found {len(lit_rows)}")
    with (lit/"lit-planned-pathways.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(lit_rows[0]))
        writer.writeheader()
        writer.writerows(lit_rows)
    (lit/"README.md").write_text(
        "# LIT — Leadership and Identity Transformation Capability Academy\\n\\n"
        "**Source Sunday**\\n\\n"
        "**5,280 planned pathways** = 12 programs × 11 GICS sectors × 5 tiers × 8 formats. "
        "An additional 132 Level-0 Origin Story folders are excluded from this count.\\n\\n"
        "These are planning records, **not** imported HUB courses, LMS IDs, published lessons, or enrollments. "
        "See [LIT planned pathway catalog](lit-planned-pathways.csv).\\n", encoding="utf-8")
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
        "Explore **7 academy folders (6 populated from HUB, 1 planned LIT academy) → 12 series → 11 GICS sectors → 6 curriculum tiers (0–5); formats available for Levels 1–5**.\n\n"
        "This township is separate from the **2,640 vendor-neutral Architecture Learning Journeys** under `learning-journeys/`.\n\n"
        "The source of truth is the uploaded HUB CSV. The published catalog excludes allocated-member names. "
        "Available/Occupied describes township allocation, **not** live-course status.\n\n"
        "See [catalog.csv](catalog.csv) for a searchable catalog index.\n",encoding="utf-8")
    print(f"Created {len(seen):,} HUB pathways, {len(lit_rows):,} planned LIT pathways and {len(origin_units)+132:,} Origin Story placeholders.")

if __name__=="__main__":
    main()
