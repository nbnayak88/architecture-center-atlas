#!/usr/bin/env python3
"""Generate exactly 2,640 vendor-neutral architecture journey folders."""
from pathlib import Path
import csv
SECTORS=["Energy","Materials","Industrials","Consumer Discretionary","Consumer Staples","Health Care","Financials","Information Technology","Communication Services","Utilities","Real Estate"]
STREAMS=["Enterprise Architecture","Business Architecture","Data Architecture","Application Architecture","Technology Architecture","AI Architecture","Security Architecture","UI/UX Architecture","Infrastructure Architecture","Integration Architecture","Domain Architecture","Industry Architecture"]
LABS=[("Discover","Product Innovation Lab","PIL"),("Flow","Process Excellence Lab","PEL"),("Design","Strategy & Architecture Lab","SAL"),("Run","Operations Optimization Lab","OOL"),("Build","Implementation Intelligence Lab","IIL"),("Move","Migration Modernization Lab","MEL"),("Connect","Integration Intelligence Lab","IEL"),("Validate","Quality Assurance Lab","QAL"),("Support","Application Management Services Lab","AMS"),("Prove","Certification Command Lab","CCL"),("Scale","School of Career Acceleration Lab for Excellence","SCALE"),("Influence","Presales Precision Lab","PSL"),("Lead","Project Performance Lab","PML"),("Prototype","Product Prototyping Lab","PDL"),("Evolve","Emerging Technologies Lab","ETL"),("Share","Media & Content Lab","MCL"),("Document","Knowledge Keystone Lab","KAL"),("Engage","Experts Engagement Lab","ECL"),("Scan","Global Industry Intelligence Lab","GIL"),("Innovate","Research & Innovation Lab","RIL")]
PATHS=["Domain Foundation","Product & Technology Knowledge","Business Process & Operating Context","Data & Information Model","Requirement Analysis","Solution Design Awareness","Configuration / Development Awareness","Architecture & Integration Awareness","Implementation Awareness","Migration & Data Readiness Awareness","Testing & Quality Awareness","Release, Adoption & Support Awareness","Troubleshooting Mindset","Incident & Defect Awareness","Complex Scenario Thinking","Optimization & Continuous Discovery / Continuous Improvement","Stakeholder Management","Communication & Collaboration","Advisory & Trusted SME","Automation, AI & Intelligent Products","Transformation & Business Value","Strategic Mastery & Future Vision"]
STAGES=["Explorer","Foundation","Practitioner","Builder","Consultant","Architect","Transformation Leader"]
def slug(x):
    import re
    return re.sub(r"[^a-z0-9]+","-",x.lower()).strip("-")
root=Path("learning-journeys")
root.mkdir(exist_ok=True)
rows=[]
for si,sector in enumerate(SECTORS,1):
 for ai,arch in enumerate(STREAMS,1):
  for li,(intent,lab,code) in enumerate(LABS,1):
   path=root/f"{si:02d}-{slug(sector)}"/f"{ai:02d}-{slug(arch)}"/f"{li:02d}-{slug(intent)}-{code.lower()}"
   path.mkdir(parents=True,exist_ok=True)
   jid=f"JL-{len(rows)+1:05d}"
   content=f"""# {sector} — {arch} — {lab}

**Journey ID:** {jid}  
**Sector:** {sector} (GICS)  
**Architecture focus:** {arch}  
**Lab:** {li:02d} — {intent} — {lab} ({code})  
**Status:** Planned — catalog scaffold, not a published course.

## Architectural purpose
Develop vendor-neutral {arch.lower()} capabilities in the {sector} sector through the **{intent}** practice of the {lab}. Begin with stakeholders, outcomes, value streams, business capabilities, processes, information, controls, and architecture decisions before selecting technologies.

## Applicable global references
Use the standards relevant to the scenario: TOGAF, ArchiMate, ISO/IEC/IEEE 42010, BIZBOK (Business Architecture Guild), BABOK, DAMA-DMBOK, APQC PCF, GICS, BPMN, COBIT, ITIL, NIST, ISO/IEC security and AI standards, and other applicable industry frameworks. These are reference points, not claims of certification or endorsement.

## 22 universal Pahacha mastery paths
""" + "\n".join(f"{i}. {name}" for i,name in enumerate(PATHS,1)) + """

## Professional evolution (Stages 0–6)
""" + "\n".join(f"- Stage {i}: {name}" for i,name in enumerate(STAGES)) + """

## Evidence-based learning
- Define a sector-specific architecture problem and measurable business outcome.
- Map stakeholders, capabilities, value streams, and relevant processes.
- Create appropriate architecture views and an architecture decision record.
- Assess quality, security, data, integration, sustainability, and change impacts.
- Produce a roadmap, evidence portfolio, and reflection on realized value.

## Delivery and governance
Learning formats, product levels, pricing, owners, and dates are configured separately. No vendor product is mandatory. This README is a curriculum scaffold, not a claim of live availability.
"""
   (path/"README.md").write_text(content,encoding="utf-8")
   rows.append([jid,sector,arch,intent,lab,code,str(path),"Planned"])
assert len(rows)==2640
with (root/"catalog.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f);w.writerow(["journey_id","sector","architecture","intent","lab","lab_code","folder","status"]);w.writerows(rows)
(root/"README.md").write_text("# SuccessLabs Academy — 2,640 Architecture Learning Journeys\n\n11 GICS sectors × 12 architecture streams × 20 Labs = **2,640** vendor- and product-agnostic core journeys. Each contains 22 universal Pahacha paths, not 22 extra core courses. All catalog scaffolds are **Planned**, not Live.\n\nBrowse by sector → architecture → lab, or consult [catalog.csv](catalog.csv).\n\nGenerated by [scripts/generate_learning_journeys.py](../scripts/generate_learning_journeys.py).\n",encoding="utf-8")
print(f"Generated {len(rows)} journey folders")
