# The ledger becomes a promise
## A two-hour Origin Story sprint: Architecting Autonomous Workforce Foundations

**SuccessLabs Academy · HR01-AWF1 · Energy · Level 0 → Pre-Foundation**  
**Platform:** SAP · **Domain:** Human Capital Management · **Architecture:** Applied Application Architecture (AA)  
**Lab:** IIL — Implementation Intelligence Lab · **Intent:** Build  
**Planning reference:** HUB-ORIGIN-HR01-ENE-sprint · Free — Community/Citizen Edition  
**Version:** 2026-10-19 · Educational sprint, not an enrolled course or certification.

> **The essential idea:** Workforce applications evolved from recording people, to executing transactions, to coordinating services, to assisting decisions. Each step increases the need for clear ownership, trustworthy history and accountable humans.

## 1. What this sprint achieves

In 120 minutes, you will:
1. Explain five overlapping generations of workforce applications and the problem each tried to solve.
2. Explain why energy operations need employment facts, competence evidence and work authorization to remain distinct.
3. Assign six application responsibilities and defend a global core with justified local variants against alternatives.
4. Build a paper prototype for one workforce change, with an effective date, approval and three acceptance tests.
5. Explain where automation can help and when a human must stop or override a decision.

**Practical outcome:** one completed Workforce Evolution Build Card. This is implementation preparation using synthetic records; it does not imply live SAP configuration capability after two hours.

**The 20% to master:** application ownership; person versus employment versus position; effective-dated history; approved lifecycle events; controlled automation. Deep configuration, API transport, infrastructure sizing and AI model design belong to later sprints.

## 2. Read the case accurately

OmniVerse Energy Ltd. is a **fictional** enterprise with 68,000 employees in 42 countries, founded in 1978, with Mumbai/Houston headquarters. Earlier historical scenes explain the wider evolution of workforce administration; they are not OmniVerse corporate history. “OmniEnergy” is an alias retained in original HR research.

The enterprise case owns company facts. OVE-HR01 owns the workforce-foundation scenario. The proposed SAP landscape, incidents and all dialogue below are illustrative. No rollout or achieved improvement is claimed. The source's 18-month roadmap and numeric victory measures are learning assumptions/targets.

### What the analysis reveals

- **Purpose:** a trusted workforce foundation supports safe staffing, correct pay, access control and reskilling.
- **Actual design dilemma:** rapid uniform template, independent local deployments, or a federated global core with governed local extensions.
- **Evolution tension:** copying a paper form into software improves storage; it does not resolve ownership or conflicting definitions.
- **Application architecture task:** decide which application is responsible for each fact and decision. HR12 handles transport/recovery design; HR11 handles deeper AI governance.
- **Evidence gap:** experiments are designed, not executed. Benefits and operational outcomes must be tested before being claimed.

## 3. Evolution: five generations, five unfinished problems

These are teaching lenses with overlapping periods, not an official industrial classification. Adoption varies by country, enterprise and worker population. Paper, ERP and cloud may coexist today.

| Generation | Broad context | Workforce application purpose | What improved | What remained unresolved | Energy implementation lesson |
|---|---|---|---|---|---|
| 1. Record the worker | Industrialization; paper ledgers | Record names, wages and attendance | A durable record | Duplicate names, delayed updates, little shared visibility | Identity must be stable; a row is not the whole person |
| 2. Administer employment | Large utilities and oil-and-gas organizations; personnel offices | Standardize personnel files and procedures | Repeatable administration | Files disagree; qualifications and employment facts diverge | A personnel file cannot prove current work authorization |
| 3. Execute transactions | Mainframe HRIS and ERP; late twentieth century onward | Process payroll, time and organizational changes | Structured rules and repeatability | Local customization, fragmented history and reconciliation | Preserve dates and identifiers when migrating; payroll remains a distinct responsibility |
| 4. Coordinate services | Cloud HCM, self-service and mobile work; 2000s onward | Make approved workforce facts usable across services | Broader access and connected employee journeys | More copies, unclear authority, permission errors | Define an authoritative source per object and accountable application boundaries |
| 5. Assist governed decisions | Current experimentation and future scenarios | Recommend actions and automate bounded, approved tasks | Potentially faster service and skills matching | Stale evidence, opaque recommendations, overreach | Recommendation ≠ approval; require evidence, owner, override and fallback |

**Verified SAP landmarks:** SAP R/3 began in 1992; SAP acquired SuccessFactors in February 2012. These anchor product evolution, not mandatory migration dates for every customer. Cloud adoption does not automatically produce trusted data or safe autonomy. [R1–R2]

**Future horizon:** skills-based deployment and AI-assisted services are possible directions. Scenes set in 2027 or 2035 are imagined design futures, not forecasts, product commitments or achieved OmniVerse states.

## 4. The story: Anika asks what the record must promise

All scenes and dialogue are newly written fiction using the source personas and their stable identities.

### Scene 1 — The old ledger
Anika Sharma (OVE-HR01-P01), Global EC Transformation Director, opens a workshop with an imagined industrial-era ledger. One column lists a worker; another records attendance.

“The ledger answers who was written down,” she says. “Does it tell us who this person is, whether the employment is active, or whether the person can perform today's task?”

The room sees the origin of the foundation: **recordkeeping serves a decision**. Digitizing the ledger improves retrieval, but does not prove accuracy.

**Pause:** Name one decision that would be unsafe if a ledger were one week out of date.

### Scene 2 — The payroll machine
Mei Wong (OVE-HR01-P05), Global Payroll Control Head, places two synthetic records beside each other: the same person, two unexplained employments.

“A computer will process both perfectly,” she says. “Perfect execution of the wrong population still gives the wrong outcome.”

Anika separates the person from the employment relationship and the position being occupied. Mei asks when each change became valid. The lesson shifts from storing data to **preserving identity and time**.

**Pause:** A worker moves to a renewable project next month. Why must today's record remain available?

### Scene 3 — The global template
Farah Al-Mansoori (OVE-HR01-P03), Middle East HR Country Lead, brings the source scenario's 31 local-field requests and nine approval variants.

Rajiv Kapoor (OVE-P05), CDIO, asks for the minimum common platform. Anika resists approving every request or deleting them all. For each one she asks: what decision needs it, what evidence justifies it, who owns it, and can a standard configuration meet the need?

The common core becomes a **shared meaning**, with local differences justified and reviewed.

**Pause:** Classify one request as mandatory, configurable or obsolete. State what evidence you still need; a country label alone is not proof.

### Scene 4 — The certificate that did not authorize work
Michael Torres (OVE-HR01-P02), Texas Refinery Director, asks whether a completed learning course can release a worker to a restricted task.

Samuel Okoro (OVE-HR01-P04), Identity and OT Security Lead, shows three different claims:
- EC: an approved employment is active.
- Learning: a course or certification record exists.
- Site safety/HSE: an authorized person has accepted the task-specific work conditions.

An account or badge is a further access mechanism. None of these facts substitutes for all the others. Exact HSE approvals and emergency procedures must be agreed for the site.

**Pause:** Which application owns the authorization decision? What happens if its evidence is missing?

### Scene 5 — The helpful assistant
In an imagined 2027 pilot, an assistant recommends a worker for a renewable assignment. It cites an active employment and a certificate—but the certificate is expired.

Nina Kohli (OVE-P01), CHRO, asks whether speed has improved trust. Anika rejects the recommendation and records why. Samuel checks that no recommendation has granted access.

**The next evolutionary step is bounded assistance:** the application can propose; accountable owners decide within approved policy. Anika asks what evidence would justify enabling a low-risk task, such as drafting a reminder, before expanding automation.

**Pause:** Choose one task to automate and one decision to retain with an authorized human. Explain the boundary.

### Scene 6 — A different promise
In an imagined 2035 retrospective, Anika does not celebrate replacing HR. She describes a foundation that helps people change roles without losing their history, pay accuracy or dignity.

The ledger's promise has evolved: **the right fact, valid at the right time, used by the right application, under the right authority**.

## 5. Application ownership: the minimum useful map

This is the proposed learning architecture, not a confirmed OmniVerse deployment.

| Application responsibility | Owns / provides | Does not establish by itself |
|---|---|---|
| SAP SuccessFactors Employee Central | Approved person/employment/job facts and relevant organization/position structures | Current competence or restricted-work authorization |
| Learning application | Learning completions and competence/certification evidence, with validity where applicable | Permission to perform every site task |
| Site safety / HSE | Restricted-work authorization under site policy, including required conditions and approvals | Employment or payroll master record |
| IAM | Digital identities/accounts and access provisioning under approved access policy | Professional competence or HSE work permission |
| Payroll — HR07 | Payroll calculation and pay outcomes from approved inputs | Ownership of all upstream workforce facts |
| Time & Absence — HR08 | Approved time and absence records/inputs | Final pay outcomes or site authorization |

**Important SAP detail:** person, employment and assignment identifiers have different roles; do not map them by name alone. Job Information is effective-dated, while Employment Information is not an effective-dated entity. Define identifier mappings and date semantics per entity. “Date every change” is a governance principle, not a claim that every EC object is technically effective-dated. [R3–R4]

**Event reason:** explains why a job/compensation transaction occurred. It is not the effective date, approval or evidence that downstream applications received the change. [R5]

## 6. Your exact 120-minute sprint

| Minutes | Activity | Evidence you produce |
|---|---|---|
| 0–10 | Read mission and five concepts. Explain why energy workforce facts matter. | Two-sentence purpose statement |
| 10–30 | Read generations 1–3 and story scenes 1–2; rebuild the evolution without looking. | Three-row “problem → application response → remaining gap” timeline |
| 30–50 | Read generations 4–5 and scenes 3–6. Ask which old problem persists in the new medium. | Two further timeline rows; one future claim labeled as a hypothesis |
| 50–65 | Play Anika. Answer Farah, Mei and Samuel using their concerns; ask one discovery question each. | Three persona needs and unanswered questions |
| 65–80 | Build the six-application ownership map. Challenge it with Michael's certificate scene. | Six owners; one explicit authorization boundary |
| 80–100 | Complete the transfer prototype below. Choose a global core/local-variant approach and compare one alternative. | Workforce change design plus one short architecture decision |
| 100–115 | Run three tabletop tests; record expected result, your observed paper result and any revision. Give a 60-second explanation to Nina. | Test evidence and an honest pass/revise decision |
| 115–120 | Run the rapid review checklist. | Five-minute recall and next experiment |

**Evolution emphasis:** the first 50 minutes establish origin and evolution; every later exercise tests whether the next generation actually solved the previous generation's problem. Resource reading is selective within these activities, not extra homework.

## 7. Build experiment: a transfer with an expired certificate

**Synthetic scenario:** worker W-100 has person reference P-100 and employment reference E-100. A transfer from refining to a renewable-project role is proposed for **1 November 2026**. Training evidence for a required restricted task expired on **18 October 2026**. Identifiers are teaching labels, not prescribed SAP field mappings.

### Complete your Workforce Evolution Build Card

| Item | Your response |
|---|---|
| Purpose | Which employee and operational outcome must this change support? |
| Employment change | Current and proposed legal entity, position, location; identify missing facts instead of inventing them |
| Identity | Is the person the same? Is this a job transfer, new employment, global assignment or concurrent employment? What evidence decides? |
| Time | Proposed effective date, approval timing, as-of view; distinguish entry date from business validity |
| Application owners | EC / Learning / HSE / IAM / Payroll / Time |
| Approval | Who approves the employment change? Who separately authorizes restricted work? |
| Local variant | One requested field or approval; classify and justify it, or hold for evidence |
| Automation | One low-risk task permitted; one protected decision; human owner and fallback |
| Architecture decision | Option, alternative, trade-off and evidence needed before implementation |
| Tests | Input → expected → actual tabletop result → evidence note → pass/revise |

**Reference reasoning:** do not create a new person merely because a position changes. Establish the correct employment transaction before configuring it. An employment transfer may proceed under approved policy while a restricted task remains blocked; certificate expiry does not automatically terminate employment. Learning renewal alone must not bypass HSE authorization.

| Test | Expected result in this proposed design |
|---|---|
| T1: View records before and on the approved future transfer date | Correct as-of job state; no premature transfer; identity/employment treatment matches the agreed transaction |
| T2: Assistant recommends the worker using expired evidence | Recommendation is rejected/held; restricted task is not authorized; accountable owner receives the exception |
| T3: Required approval is missing or a receiving application has no confirmed outcome | Change is not reported as fully completed; exception and owner remain visible; applicable controlled fallback is invoked |

**Optional test after this sprint:** rehire or concurrent employment. Do not assume every worker has only one employment.

**Acceptance:** explain all five generations; map all six responsibilities; distinguish person/employment/position and date/reason; pass all three tabletop expectations after revisions; state what remains unverified. A safety-authorization bypass requires redesign.

**Learning evidence only:** record what your paper exercise actually did. Live configuration, real integration performance and operational outcomes remain untested.

## 8. High-impact resources — read with a question

| Resource | Use in the sprint | Question to answer |
|---|---|---|
| [R1 SAP history](https://www.sap.com/uk/about/company/history.html) and [R2 SuccessFactors history lesson](https://learning.sap.com/courses/sap-successfactors-platform-introduction-academy/summarizing-the-sap-successfactors-history-and-modules_e11f8449-433a-4934-84f3-b6333a765e57) | 5-minute selective scan during evolution | What changed from ERP transactions to cloud HCM services? |
| [R3 Person and employment objects](https://learning.sap.com/courses/sap-successfactors-employee-central-core-academy/using-special-hr-transactions-for-hires-and-terminations_e8c3ec4e-0435-4920-89ce-29ded46e87bf) | 5-minute scan during ownership/build | Why must a person and an employment be distinguishable? |
| [R4 Effective dating](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/95fbd901727d4f25b740a0c69f01b1be.html?locale=en-US) and [Employment entity](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/empemployment) | 4-minute lookup during build | Which object preserves history, and which is not effective-dated? |
| [R5 Events and event reasons](https://learning.sap.com/courses/sap-successfactors-employee-central-core-administration/managing-events-and-event-reasons) | 3-minute lookup during build | Why did the change occur, and when should it apply? |
| [R6 NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | 3-minute scan during future scene | Who governs, what risk is mapped, what evidence is measured, and how is risk managed? |

Official SAP documentation establishes product behavior; the fictional case establishes the learning scenario. Access requirements can vary. Do not read entire courses in this sprint.

**Existing student workspace:** [OmniVerse HR Student Resource Index](https://docs.google.com/document/d/1Jbrsu4PkFBR0dNJ7NELR13d5pk-2mCAeWopOH59kWKk/edit). It lists the existing HR resources. Its current instructions say student access is pending; copies are independent snapshots. This sprint does not alter Drive sharing or claim to refresh those files.

## 9. Five-minute rapid review

| Minute | Recall without looking |
|---|---|
| 1 | Name the five generations: record → administer → execute → coordinate → assist. What unresolved problem passes to the next? |
| 2 | Explain person, employment and position. Explain effective date versus event reason. Are all EC entities effective-dated? |
| 3 | Name the owners of employment facts, learning evidence, site authorization, accounts, pay and time. Why is a badge insufficient? |
| 4 | Explain the future transfer and expired-certificate tests. Who can stop the restricted task? |
| 5 | Give Nina a 60-second answer: why this foundation, what will you build first, what evidence will permit the next step? |

**Pass phrase:** “Automation may accelerate an approved task; it does not create missing authority or trustworthy evidence.”

**Next experiment:** take one disputed local requirement into Pre-Foundation. Define its terms, owner, evidence, configuration option and acceptance test.

## 10. Source traceability and boundaries

| Source | What is reused | Treatment |
|---|---|---|
| [Enterprise case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd) | Company identity, 68,000 employees, 42 countries, founding/HQ | Fictional baselines preserved |
| [OVE-HR01](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/hr01-workforce-foundation.md) | Five domain personas, design dilemma, 31 fields/nine variants, duplicate records, safety/access scenes | Stable IDs preserved; new dialogue is illustrative |
| [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) | OVE-P01 Nina; OVE-P05 Rajiv | Same roles and IDs; no invented biographical history |
| [Source register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/references/source-and-assumptions.md) | Fictional/assumption/target distinctions | No achieved benefit or forecast asserted |
| [Notion enterprise KM hub](https://app.notion.com/p/377ce6de608980daae89e74da8236287) / [HR01 original research](https://app.notion.com/p/358d96630bf44787b59ec0b1b389eb46) | Research lineage; enterprise hub read alongside GitHub; HR01 details read from preserved GitHub snapshot | Original research left intact |
| R1–R6 above | SAP history, entity/date/event concepts, AI risk functions | Official references checked 2026-10-19 |
| New sprint material | Five-generation teaching model, story dialogue, future scenes, synthetic transfer and tabletop expectations | Educational synthesis and illustrative design, not historical testimony |

**Identity caution:** Michael Torres differs from enterprise CFO Michael Reed; Farah Al-Mansoori differs from COO Farah Al-Hassan. Use stable IDs, not first-name matching.

**Standards alignment:** TOGAF application responsibility and architecture decisions; BIZBOK capability/value distinction; BABOK need/requirement/acceptance trace; DAMA ownership and quality; COBIT accountable decisions and controls; ISO/IEC 27001 access-control principles. These are educational mappings, not claims of compliance, certification or reproduction of proprietary standards. NIST AI RMF supports the bounded-assistance discussion.

**Publication:** this is a manually authored derivative in architecture-center-atlas. It does not change canonical case facts or establish unattended GitHub–Notion–Drive synchronization.
