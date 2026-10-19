# The payroll run succeeded; the worker was not paid correctly
## A two-hour Origin Story sprint: Architecting Autonomous Payroll Enterprises

**SuccessLabs Academy · HR07 · Energy · Level 0 → Pre-Foundation**  
**Platform:** SAP · **Domain:** Human Capital Management · **Architecture:** Applied Application Architecture (AA)  
**Lab:** IIL — Implementation Intelligence Lab · **Intent:** Build  
**Planning reference:** HUB-ORIGIN-HR07-ENE-sprint · Free — Community/Citizen Edition  
**Version:** 2026-10-19 · Published lesson; not an enrolled course or certification.

> **Evolution lens:** record → calculate → integrate → control → assist. New technology changes how work is coordinated; it does not remove responsibility for evidence, people impact and authorized decisions.

## 1. What this two-hour sprint achieves

By the end you will:
1. Explain the general origins and purpose of this domain before naming a product.
2. Reconstruct its process evolution across **1975–2026**, identifying what improved and what remained unresolved.
3. Compare **2030, 2035, 2040 and 2050** scenarios, with a competing future and a validation question.
4. Map application responsibilities and source objects for the OmniVerse Energy case.
5. Produce a synthetic build prototype, run three tabletop tests and defend an evidence-based next step.

**The 20% to master:** gross versus net; approved inputs and cutoffs; retroactivity; payment versus calculation; reconciliation and continuity.

**Deliverable:** one Domain Evolution Build Card containing a timeline, persona needs, ownership map, state/control prototype, option decision and test evidence. Practical capability here means implementation preparation; it does not imply production configuration proficiency after two hours.

## 2. Origins and purpose — the general story

Payroll turns an approved employment/pay entitlement into calculations, payments and records. Manual wage books gave way to batch engines and connected HR/payroll systems. Reliable calculation is only one part: authorized inputs, country rules, banking, accounting and employee explanation must agree.

**Teach the decision first:** what decision is needed, whose outcome matters, what evidence supports it, which application is responsible, and who has authority to act?

### Fifty years of process evolution

Dates group broad historical patterns for learning. They do not claim invention dates, uniform adoption or a source-proven worldwide chronology. Paper, legacy, cloud and assisted processes can coexist today; the table is an educational synthesis.

| Era | Process pattern | What improved | Remaining gap | Energy-sector example |
|---|---|---|---|---|
| 1975–1984 | Wage books and batch calculation | Repeatable wage administration | Late changes and manual reconciliation | Shift and hazard entitlements require careful recording |
| 1985–1994 | Computerized payroll engines | More structured deductions and repeatable runs | Input quality and local rule differences remain | A valid formula still pays wrong if the hours are wrong |
| 1995–2004 | ERP HR/payroll and bank/accounting connections | Employee records and postings more connected | Cross-system differences and failed handoffs | Trace a refinery allowance from approval to ledger |
| 2005–2014 | Global templates and service hubs | More shared controls and operating consistency | One engine cannot be assumed to cover all local requirements | Keep country-qualified review and accountable local owners |
| 2015–2019 | Cloud/hybrid payroll and employee access | More visible payslips and integrated controls | A portal does not fix disputed pay | Luciana needs a reason and correction route |
| 2020–2022 | Remote operations and continuity pressure | Stronger need for controlled operations despite disruption | Unavailable inputs can threaten deadlines | Pre-agree cutoff, fallback and recovery ownership |
| 2023–2026 | Assisted anomaly investigation | Potentially faster explanations and control triage | A flag is not proof of error; autonomy can release wrong pay | Human authorization and reconciled outcomes remain essential |

**Evolution activity:** cover the table. For each era, say “the process changed from ___ to ___ because ___; the unresolved problem was ___.” Use an energy example rather than a product slogan.

**Historical caution:** the 2020–2022 row describes possible process pressures/responses in distributed work, not proof that every energy enterprise changed in that way. Modern product documentation supports current capabilities, not the full historical chronology.

## 3. Future perspectives to 2050

**Scenario boundary:** all four horizons are possible design directions. None is an official SAP roadmap, forecast, legal prediction or achieved OmniVerse result.

| Horizon | Possible process direction | What to validate before scaling |
|---|---|---|
| 2030 | Assisted explanations grounded in authorized payroll results | Test a bounded synthetic pilot; compare with a non-AI/manual option and preserve an accountable owner |
| 2035 | More timely controls and simulations before release | Validate evidence quality, worker access and role/country differences; do not infer authority from a recommendation |
| 2040 | Resilient cross-provider payroll governance with clear local scope | Evaluate interoperability, practical operating value, worker impact and recovery under changing requirements |
| 2050 | A possible adaptable payroll ecosystem preserving correct, explainable and timely pay | Retain human challenge, explainable responsibility, accessible alternatives and evidence history; revise when assumptions fail |

| Alternative 2050 world | What could happen | Design choice useful today |
|---|---|---|
| Trusted learning ecosystem | People, accountable owners and bounded assistance improve the capability together | Inspectable evidence, worker voice and measured experiments |
| Opaque metric/automation regime | Convenient scores or actions displace context and responsibility | Explicit prohibitions, review gates, correction and fallback |
| Fragmented local ecosystems | Different applications, definitions and institutions remain incompatible | Shared semantics and acceptance contracts with justified local variants |

**2050 experiment question:** which part of the future could you test with today's synthetic records? What observation would make you abandon the proposed design?

## 4. OmniVerse Energy — the decision and the people

**Fictional enterprise baseline:** OmniVerse Energy Ltd., 68,000 employees across 42 countries. “OmniEnergy” is an alias preserved in original research. Historical eras are not a corporate biography; OmniVerse was founded in 1978.

**Modernize global payroll without gambling with employee pay, legal compliance, or energy operations.**
OmniEnergy payroll must process offshore rotations, refinery shifts, overtime, hazard premiums, mobility, expatriate allowances, sales incentives, union rules, and country statutory obligations for 68,000 employees. Fragmented engines and manual interfaces create control and employee-trust risks.

**Scope note:** Country statutory settings are deliberately not prescribed. Validate current law, agreements and product coverage with qualified local owners; this sprint tests architecture and controls using synthetic records.

### Canonical personas

| Stable source ID | Persona / source designation | Concern |
|---|---|---|
| OVE-HR07-P01 | Meera Iyer, Global Payroll Transformation Executive | Owns accuracy, strategy, controls, migration, and employee trust. |
| OVE-HR07-P02 | Hans Becker, Germany Payroll Lead | Protects statutory and works-council requirements. |
| OVE-HR07-P03 | Luciana Costa, Refinery Employee Persona | Needs understandable, accurate, and timely pay. |
| OVE-HR07-P04 | Robert Li, Group Financial Controller | Requires reconciled postings, liabilities, and evidence. |
| OVE-HR07-P05 | Ngozi Adeyemi, Payroll Technology and Security Lead | Owns interfaces, segregation of duties, recovery, and monitoring. |

Names, roles and source IDs are retained. Proposed decision rights require discovery validation; a persona title is not proof of final authority.

**Decision to investigate:** Compare one platform, regional hubs and a hybrid service model; evaluate local coverage, continuity and control rather than standardization alone.

## 5. Persona-led story — The payroll run succeeded; the worker was not paid correctly

All narrative links and dialogue prompts below are newly written fiction. Present-day personas are workshop voices, not people claimed to have worked in all historical eras.

### Scene 1 — The old record

Meera Iyer brings a paper-era record to the workshop and asks, “What decision was this meant to support?” The group compares the first two timeline rows. An available record improved visibility; the unresolved gap in those rows shows why visibility alone was insufficient.

**Pause:** name one fact the old record could prove and one decision it could not justify.

### Scene 2 — Digital speed, same unresolved problem

Luciana sees an unexplained deduction. Hans challenges the global template. Robert finds ledger differences while Ngozi simulates a failed input feed just before cutoff.

The team maps the conflict back to the electronic/integrated era. A faster application can amplify an unclear definition or a weak decision. Meera Iyer asks which source record and accountable owner would settle the disagreement.

**Pause:** identify the competing stakeholder needs; ask for evidence before proposing configuration.

### Scenes 3–6 — Replay the source challenges

**Scene 3:** **Pay incident:** Luciana receives an unexplained deduction.

Act as Meera Iyer. Ask one discovery question; state the affected application responsibility; compare one alternative; name the evidence and owner needed to proceed. Record an unresolved issue rather than inventing an answer.

**Scene 4:** **Localization conflict:** Hans rejects parts of the global template.

Act as Meera Iyer. Ask one discovery question; state the affected application responsibility; compare one alternative; name the evidence and owner needed to proceed. Record an unresolved issue rather than inventing an answer.

**Scene 5:** **Finance mismatch:** Robert finds payroll-to-ledger differences.

Act as Meera Iyer. Ask one discovery question; state the affected application responsibility; compare one alternative; name the evidence and owner needed to proceed. Record an unresolved issue rather than inventing an answer.

**Scene 6:** **Continuity test:** Ngozi simulates an unavailable interface before cutoff.

Act as Meera Iyer. Ask one discovery question; state the affected application responsibility; compare one alternative; name the evidence and owner needed to proceed. Record an unresolved issue rather than inventing an answer.

### Scene 7 — An imagined 2050 design review

The workshop imagines: **a possible adaptable payroll ecosystem preserving correct, explainable and timely pay**. A future assistant offers a polished recommendation, but one relevant record is stale or disputed. The affected worker asks to inspect and correct the evidence.

The group tests whether its architecture still provides a source owner, a human challenge route and controlled recovery. It compares the trusted and fragmented future scenarios instead of assuming a frictionless global system.

**Pause:** which present-day design decision would make this future easier to govern? What should remain with a human even if preparation becomes automated?

## 6. Key concepts and application responsibility

| Concept | Meaning and boundary |
|---|---|
| Gross/net | Earnings before versus after applicable deductions |
| Retroactivity | Recalculation of a prior period for an approved change; not automatically an error |
| Cutoff | Agreed processing boundary and exception process |
| Payroll result | Calculated outcome; not proof of bank receipt |
| Disbursement | Authorized release and execution of funds |
| Reconciliation | Match inputs/results/payments/postings and resolve differences |

| Application / accountable area | Responsibility |
|---|---|
| EC / HR01 | Approved employment/pay inputs within scope |
| Time / HR08 | Approved time and absence inputs |
| Payroll | Gross-to-net and statutory calculation |
| Treasury / bank process | Authorized funds disbursement and payment status |
| Finance | Accepted balanced postings/liabilities |

**Source information objects:** pay period; wage type; retro period; deduction; bank instruction; posting; control total. Record attribute owner, authoritative source, purpose, access, retention, effective date and quality rule.

**Source value stream:** Approved inputs → validate → calculate → resolve → authorize → pay → post → reconcile. Define a stakeholder-valued exit criterion at each stage before detailed process modeling.

A capability is an ability the organization needs; the value stream describes progression toward stakeholder value. Neither is simply a list of applications.

**AA boundary:** this sprint assigns application responsibility and acceptance criteria. Reference data stewardship, security, integration, UX, infrastructure and AI concerns without assuming the application view alone implements those controls. Cross-domain consumers must not silently become owners of source facts.

## 7. Exact 120-minute sprint flow

| Minutes | Activity | Evidence |
|---|---|---|
| 0–10 | Read the general purpose and essential concepts | Two-sentence purpose and responsibility boundary |
| 10–30 | Rebuild the 1975–2026 process timeline from memory | Seven problem → response → remaining-gap rows |
| 30–50 | Compare 2030–2050 futures and the energy-specific scope note | One future hypothesis, competing scenario and validation question |
| 50–65 | Simulate the canonical decision scenes as the domain lead | Five persona needs; three evidence-seeking questions |
| 65–80 | Map objects, source owners and consumer applications | Ownership map and one protected decision boundary |
| 80–100 | Complete the Build Card and compare solution options | State/control prototype and short architecture decision |
| 100–115 | Run all three tabletop tests; revise and explain the design in 60 seconds | Expected versus actual paper results; pass/revise decision |
| 115–120 | Perform rapid review without looking | Recall check and next learning experiment |

Resource scans below fit inside these activities. The two-hour total does not require reading every linked product or course.

## 8. Build experiment — a small, reviewable implementation design

Use **two synthetic records**, one routine and one variant drawn from the source challenges. Assign teaching identifiers **HR07-SYN-001/002**. Do not use real employee information, internal endpoints or live banking/access actions.

| Build Card field | What you must write |
|---|---|
| Purpose/population | Decision, affected person/role and intended outcome; identify missing facts |
| Two variants | Legitimate retroactive change versus Duplicate bank instruction |
| Objects and time | Identifiers, source, relevant validity/as-of/processing dates; distinguish their meanings |
| Lifecycle/gates | Proposed from-state → permitted transition → prerequisite → accountable actor |
| Evidence | Source reference, validation status, version and correction owner |
| Application boundary | EC / HR01 responsibility versus Finance |
| Global/local decision | Shared principle, justified role/country variant and evidence still needed |
| Human and automation boundary | One permitted administrative task; one protected consequential decision |
| Exception/recovery | Visible exception, owner, fallback, recovery and confirmation |
| Architecture decision | Compare one platform, regional hubs and a hybrid service model; evaluate local coverage, continuity and control rather than standardization alone. |
| Measure | Definition, denominator, exclusions, as-of date, owner and interpretation limits |
| Test evidence | Input → expected → actual paper result → correction → evidence note → pass/revise |

**Conceptual workflow:** establish approved source evidence → validate → apply agreed rule → authorized decision/action → confirm downstream business outcome → review exceptions. These are teaching stages, not prescribed SAP object/status names. Choose actual module configuration only after validating the contract and product version.

### Three tabletop tests

| Test | Challenge | Expected result in this proposed design |
|---|---|---|
| T1 | Legitimate retroactive change | Recalculate per approved country/process rules; explain delta rather than suppress all retroactivity |
| T2 | Duplicate bank instruction | Detect repeated business instruction; prevent uncontrolled second payment and confirm bank status |
| T3 | Failed pre-cutoff feed / ledger mismatch | Expose exception, invoke approved continuity process and reconcile; no success claim based solely on run completion |

**How to run:** represent each record/state on paper or in a simple table. Execute the steps yourself; record whether the initial design produced the expected outcome. If it did not, revise and rerun. Designed expectations are not actual SAP test results.

**Acceptance:** explain the timeline, defend one 2050 hypothesis against an alternative, distinguish the concepts, assign owners and satisfy all three tabletop expectations after documented revision. An unsupported safety/pay/access/employee-rights outcome requires redesign. List any control that remains untested.

**Source measure:** On-time correct pay = employees paid correct authorized amount by due date / employees due; classify corrections by cause, not a zero-retro target. Owner: domain lead unless specified; cadence: proposed pilot review and monthly follow-up. Establish denominator, exclusions, as-of date and baseline before setting a numeric target. Original source “Victory Measures” are targets, not achievements.

Do not fabricate a baseline, achieved benefit or target. A successful prototype proves only the limited behaviour you actually exercised.

## 9. High-impact resources — current solutions and learning

**Reviewed 19 October 2026.** Representative resources, not an exhaustive inventory or independent market ranking. Vendor pages establish advertised scope; fit, outcomes, licensing, country coverage and generally available features need separate verification. Use a matching product version in implementation.

| Official resource | Selective learning focus |
|---|---|
| [SAP Core HR and Payroll help](https://help.sap.com/docs/portfolio-category/CORE_HR_AND_PAYROLL) | Navigate current Employee Central Payroll guides |
| [SAP Payroll Control Center](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/standard-delivery-of-payroll-control-center?locale=en-US) | Control and exception concepts; match correct product version |
| [Workday](https://www.workday.com/) | Study payroll scope by country and provider |
| [ADP](https://www.adp.com/) | Compare payroll services and controls |
| [Dayforce](https://www.dayforce.com/) | Compare connected pay/time responsibilities |
| [UKG](https://www.ukg.com/) | Compare payroll/workforce scope |

**Resource route within existing activity time:** 5 minutes on the first SAP resource, 4 minutes on a second relevant SAP/standards reference, 4 minutes on one cross-vendor alternative, 3 minutes comparing a scenario against the same acceptance tests. Scan selectively; membership/tenant access may be required for detailed documentation.

**Comparison row:** solution/module → authoritative objects → role/country variants → permissions → evidence/versioning → business acceptance → recovery → license/coverage gap. Add it to the existing Build Card, not another deliverable.

**Latest does not mean proven:** compare demonstrable behaviour against the same test cases. An acquisition, new bundle or AI announcement does not establish that every feature is licensed, enabled or appropriate for OmniVerse.

## 10. Five-minute rapid review

| Minute | Recall without looking |
|---|---|
| 1 | Trace the seven eras from 1975 to 2026 using this lens: record → calculate → integrate → control → assist |
| 2 | Define the first three concepts and the most easily confused boundary |
| 3 | Name each source/application owner and the decision it cannot make alone |
| 4 | Explain all three tests and one recovery/appeal/correction step |
| 5 | Give the domain lead a 60-second answer: what might change by 2050, what alternative could emerge, and what will you test next? |

**Next Pre-Foundation experiment:** take one unresolved source challenge, define its vocabulary, approved rules, configuration hypothesis, permissions and acceptance test. Ask the affected employee and accountable owner to challenge it. Stop, revise or extend based on evidence.

## 11. Traceability and standards boundaries

- **Canonical enterprise:** [OmniVerse case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd).
- **Canonical domain:** [OVE-HR07 source case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/hr07-payroll.md); five source personas/IDs and source challenge names are preserved.
- **Original Notion lineage:** [preserved research](https://app.notion.com/p/0414bddb302b4ac1bda81984212bf533); read through the GitHub snapshot for this publication. No Notion edit is implied.
- **Source interpretation:** [enterprise source register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/references/source-and-assumptions.md). Scenario numbers and victory measures are fictional assumptions/targets.
- **New lesson content:** historical teaching synthesis, connecting narrative, future scenarios, synthetic records and proposed controls are illustrative; no executed tenant/operational outcome is asserted.

**Trace:** OVE-HR07-CAP01 → OVE-HR07-VS01 → OVE-HR07-REQ01/02 → OVE-HR07-ADR01 → this tabletop derivative of OVE-HR07-EXP01/T01 → OVE-HR07-KPI01. Publishing a lesson does not populate OVE-HR07-EV01 with observed operational evidence.

**Educational alignment:** TOGAF for application responsibilities and alternatives; BIZBOK for capability/value distinctions; BABOK for needs/acceptance; DAMA for ownership/quality; COBIT for accountable control; ISO/IEC 27001 principles for information access. These mappings are not compliance certification or reproduction of proprietary standards.

**Publication:** manual derivative in architecture-center-atlas. Origin Story remains sprint-only. Production implementation, enrollment, realized benefit, Notion/Drive refresh and unattended synchronization remain unclaimed.
