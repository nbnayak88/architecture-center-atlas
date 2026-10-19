# From finding workers to earning candidate trust
## A two-hour Origin Story sprint: Architecting Autonomous Talent Acquisition

**SuccessLabs Academy · HR02-ATA2 · Energy · Level 0 → Pre-Foundation**  
**Platform:** SAP · **Domain:** Human Capital Management · **Architecture:** Applied Application Architecture (AA)  
**Lab:** IIL — Implementation Intelligence Lab · **Intent:** Build  
**Planning reference:** HUB-ORIGIN-HR02-ENE-sprint · Free — Community/Citizen Edition  
**Version:** 2026-10-19 · Published learning content, not an enrolled course or certification.

> **Essential idea:** Talent acquisition evolved from finding available people, to managing applications, to coordinating candidate journeys, to assisting skills-based decisions. Better automation does not remove the need for relevant evidence, fair assessment and accountable hiring decisions.

## 1. What this sprint achieves

In 120 minutes, you will:
1. Explain the general origin and five overlapping generations of talent acquisition.
2. Translate that evolution into energy-sector hiring needs without assuming every role needs the same controls.
3. Distinguish position, requisition, candidate, application, assessment and offer.
4. Assign application responsibilities from approved demand to employment handoff.
5. Build and test a small recruiting design that balances speed, evidence and candidate trust.

**Output:** one Talent Acquisition Evolution Build Card, with an ownership map, two role variants, a decision record and three tabletop tests.

**The 20% to master:** approved hiring demand; candidate versus application; role-relevant assessment evidence; controlled state/offer transitions; human accountability and visible exceptions.

This sprint builds implementation preparation using synthetic data. Production SAP configuration, legal determinations and operational results are not implied.

## 2. Talent acquisition in general — origin and purpose

Recruitment began as an organizational answer to a simple problem: work required people whose availability and abilities matched the need. As enterprises grew, informal introductions and local hiring could no longer provide consistent visibility, repeatable selection or auditable approvals. Personnel administration, advertising, agencies and application tracking addressed different parts of that problem.

**Recruitment** commonly emphasizes attracting and selecting people for openings. **Talent acquisition** broadens the horizon to demand, future skill pipelines, internal candidates, relationships and candidate experience. These practices coexist; they are not universally sequential stages.

**Purpose:** turn an authorized workforce need into a fairly assessed, mutually accepted hiring decision, with a reliable handoff into employment and readiness.

**Boundary:** hiring someone is different from making them ready to work. Accepted offer ≠ created employment ≠ site access ≠ authorization for a hazardous task.

### Five generations of evolution

Periods below are broad teaching contexts, not official classifications or universal adoption dates. Different models coexist today.

| Generation | General context and response | What improved | What remained unresolved | Energy translation |
|---|---|---|---|---|
| 1. Find available workers | Local referrals, direct approaches, paper notices and agency introductions | Reach and immediate staffing | Narrow networks, inconsistent evidence, limited traceability | Who can fill a shift is not the same as who can safely perform its tasks |
| 2. Standardize selection | Personnel offices, job descriptions, application forms and interview procedures | Repeatability and documented decisions | Paper delays, subjective criteria, disconnected approvals | Define role-specific competence and demand before advertising |
| 3. Track applications | Electronic applicant tracking and online job boards | Searchable records and visible stages | Keyword proxies, duplicates and treating people as application rows | One engineer may apply to multiple requisitions; preserve each decision's context |
| 4. Orchestrate the journey | Cloud recruiting, career sites, mobile applications, scheduling and connected services | Candidate reach, communication and coordinated handoffs | Fragmented journeys, contradictory messages and unclear owners | Renewable-project speed must coexist with offshore evidence requirements |
| 5. Assist skills-based decisions | Current experimentation and future AI-assisted workflows | Potentially faster administration and discovery of adjacent skills | Biased proxies, stale evidence, opaque recommendations and automation overreach | Assist recruiters; retain accountable selection and protected safety decisions |

**The evolutionary test:** ask what problem a new application solves, what old problem persists, and what new control it needs. A chatbot attached to a fragmented recruiting process does not establish a coherent talent-acquisition architecture.

**Autonomous, in this learning series:** bounded orchestration of approved tasks, with observable outcomes and human escalation. It does not mean unreviewed employment decisions.

## 3. Apply the story to OmniVerse Energy

**Fictional case facts:** OmniVerse Energy Ltd. has 68,000 employees across 42 countries. “OmniEnergy” is an alias in preserved source research. The HR02a source sets a learning challenge of 450 safety-critical/scarce-skill roles in six months, including Sofia's request for 200 project and engineering hires. These are scenario demand assumptions, not achieved hires, approved budgets or evidence that the two populations should be added together.

Energy transition changes the demand mix: petroleum/refinery expertise remains important while renewable projects, grid engineering, digital systems and cybersecurity require additional capabilities. The application architecture must support different selection evidence without creating an uncontrolled application for every business unit.

| Pressure | Weak foundation | Design principle |
|---|---|---|
| Urgent construction workforce | Speed measured only by volume or time | Remove administration; preserve job-relevant assessment gates |
| Offshore/hazardous work | Uploaded certificate treated as verified qualification | Record validation evidence and scope; keep site authorization separate |
| Scarce transition skills | Exact title or keyword treated as ability | Assess relevant skills and transferable experience with structured evidence |
| Global operations | Local workarounds and inconsistent approval meanings | Shared core states with justified local variants |
| Candidate trust | Duplicate messages or unexplained outcomes | One accountable stage owner and clear next steps |
| AI assistance | Recommendation treated as an employment decision | Evidence, authorized review, challenge route and auditable rationale |

**Strategic choice:** centralized recruiting, business-led hiring, or a federated TA product model. The federated option is a hypothesis to test, not an approved answer.

## 4. Meet the source personas

| Stable source ID | Persona | Concern to explore |
|---|---|---|
| OVE-HR02a-P01 | Arjun Malhotra — Global Talent Acquisition Product Owner | Recruiting outcomes, platform governance and candidate trust |
| OVE-HR02a-P02 | Sofia Bennett — Renewables Growth President | 200 project/engineering hires before construction begins |
| OVE-HR02a-P03 | Kwesi Boateng — Offshore Operations Director | Verified credentials for rotational and hazardous environments |
| OVE-HR02a-P04 | Elena Markovic — Responsible AI and Privacy Counsel | Opaque screening and unnecessary candidate data |
| OVE-HR02a-P05 | Noor Rahman — Candidate Persona, Grid Engineer | Clear requirements, timely communication and fair assessment |

Source roles/IDs are retained. All dialogue below is newly written fiction. These characters are not claimed to have lived through the historical generations.

## 5. The story — Arjun follows the application backward

### Scene 1 — Before the application
Arjun opens a workshop with an imagined paper notice: “Workers needed.”

Sofia asks why anyone should spend time on history when construction is approaching. Arjun asks: “Was the real need a person, an approved position, or a capability needed by a date?”

The notice could attract people, but it could not prove who authorized the demand or what evidence made a candidate suitable.

**Evolution lesson:** attracting applicants cannot repair an undefined workforce need.  
**Pause:** What must be approved before this role is advertised?

### Scene 2 — The form becomes a system
Arjun sketches a paper form beside an electronic application. Both ask the same questions. Noor asks why every application requires entering the same career history again.

The team distinguishes a **candidate profile** from a **job-specific application**. A person can be considered for more than one opening; each application needs its own status and selection evidence. Digitization improves retrieval, but a poorly designed form remains burdensome.

**Evolution lesson:** build the right objects before automating their movement.  
**Pause:** If Noor applies for two jobs, must both applications have the same outcome?

### Scene 3 — The race to fill
Sofia wants to shorten selection for the 200 hires. Arjun offers to remove duplicate data entry and coordinate interviews, but asks which assessments are relevant to each role.

Kwesi refuses to accept an uploaded certificate as proof of validated offshore credentials. Arjun separates submission, validation and later site authorization.

**Evolution lesson:** reduce waiting and repetition before removing evidence gates.  
**Pause:** Which step can be accelerated, and which evidence must remain?

### Scene 4 — The helpful ranking
In an imagined future pilot, an assistant ranks applications. Noor is placed low because the model gives heavy weight to a past job title, although the application contains relevant grid-engineering evidence.

Elena asks which criteria were approved, what evidence supports the recommendation and how Noor can challenge an adverse outcome. Arjun pauses the affected automation for review. A difference in progression rates is a signal to investigate; by itself it does not establish its cause.

**Evolution lesson:** a recommendation is an input to judgment, not proof of suitability or fairness.  
**Pause:** What would you inspect before enabling this assistance again?

### Scene 5 — One candidate, two messages
Noor receives “prepare for onboarding” and “assessment incomplete” on the same day.

Arjun finds that one application state triggered a message before its prerequisite was confirmed. He assigns ownership to the recruiting state transition and defines the handoff acceptance, rather than adding another reminder.

**Evolution lesson:** candidate experience depends on coherent application responsibilities, not just attractive screens.  
**Pause:** Which state authorizes a message? What must happen if the next application rejects the handoff?

### Scene 6 — A different measure of success
In an imagined future retrospective, Sofia asks whether the system is autonomous yet. Arjun shows the work it can coordinate, the exceptions it reveals and the decisions named humans still own.

Noor's accepted offer is not counted as site readiness. Kwesi receives validated evidence for his scope, while onboarding, employment creation and safety authorization remain visible downstream responsibilities.

**Evolution lesson:** mature automation makes responsibility clearer. It does not erase it.

## 6. Minimum application ownership map

Proposed SAP-centered learning design; not a confirmed OmniVerse landscape. Product features, permissions and handoffs require tenant-specific validation.

| Responsibility / application area | Owns or provides | Boundary |
|---|---|---|
| Workforce planning, position control and Finance approval | Approved demand, position context and funding authorization | A requisition alone does not prove funding; Finance approval is an authority exercised through an agreed workflow |
| Recruiting Marketing / career-site and engagement services | Attraction, job presentation and candidate engagement | A talent-community contact is not automatically an applicant |
| Recruiting Management / recruiter experience | Requisition, candidate/application states, selection evidence references and offer workflow | Recruiting does not authorize hazardous work |
| Assessment / credential-verification service or accountable verifier | Scoped assessment results and evidence of credential validation | A score is not the final hiring decision; an upload is not validation |
| Onboarding — HR02b | Pre-start/readiness activities and agreed hiring handoff coordination | Initiated onboarding does not establish all work permissions |
| Employee Central — HR01 | Approved employment creation and workforce facts through the configured hire process | Candidate ID is not automatically person/employment ID |
| IAM and site safety/HSE | Accounts/access under approved policy; restricted-work authorization under site policy | Offer acceptance, badge issuance and course completion are distinct from task authorization |

This sprint defines application responsibilities and acceptance. HR12 covers detailed message transport/retry design; HR11 covers deeper AI governance; HR02b covers onboarding execution. Shared boundary awareness does not transfer ownership of those domains into HR02.

### Six objects you must distinguish

| Object | Plain meaning | Beginner mistake |
|---|---|---|
| Position | Organizational role/slot, where position management is used | Assuming every requisition has one mandatory one-to-one position relationship |
| Requisition | Governed hiring request with defined scope and approvals | Treating advertisement publication as demand approval |
| Candidate profile | Information about the prospective/internal candidate | Treating it as an employee master record |
| Application | Consideration of a candidate for a particular requisition | Sharing one outcome across every application |
| Assessment evidence | Role-relevant observations/results with provenance | Treating a keyword score as verified competence |
| Offer/version | Proposed employment terms with approval and acceptance states | Treating a draft, sent and accepted offer as equivalent |

**SAP anchor:** official learning describes a recruiting flow from requisition through sourcing, screening and selection, followed by offer activities. Profile and application are distinct concepts; verify configuration-specific synchronization rather than assuming every field continuously matches.

## 7. Exact two-hour sprint flow

| Minutes | Activity | Learning evidence |
|---|---|---|
| 0–10 | Read purpose and five essential concepts; compare recruitment and talent acquisition | Two-sentence purpose and boundary statement |
| 10–30 | Rebuild the general five-generation timeline | Five “problem → response → remaining gap” rows |
| 30–50 | Read energy pressures and scenes 1–3 | Translate three general lessons into energy requirements |
| 50–65 | Simulate scenes 4–6 as Arjun; question Sofia, Kwesi, Elena and Noor | Four needs, one question each and one challenged assumption |
| 65–80 | Map objects and application ownership | Ownership map plus candidate/application distinction |
| 80–100 | Build the two-role recruiting prototype below | State/gate matrix and a short architecture decision |
| 100–115 | Run three tabletop tests; revise and defend to Sofia in 60 seconds | Expected/actual paper results and pass/revise decision |
| 115–120 | Run rapid review without looking | Recall check and next experiment |

Evolution occupies the first 50 minutes and supplies the questions tested throughout the build. Selective resource scans fit inside these activities.

## 8. Build experiment — speed without losing evidence

**Synthetic prototype:** requisition R-ENE-001 for a grid engineer and R-ENE-002 for an offshore maintenance technician. Candidate C-001 is a teaching identifier for Noor's grid-engineer application A-001. Use a separate synthetic candidate C-002/application A-002 for the offshore scenario; do not invent an offshore background for Noor.

Use this proposed conceptual lifecycle:
**Draft demand → authorized requisition → published → application received → assessed → selection approved → offer approved/sent → accepted → handoff acknowledged.**

These are design labels, not prescribed SAP status names or one shared workflow for every object. Requisition, application, offer and handoff each have their own lifecycle. Define how their states constrain one another.

| Build Card field | Your response |
|---|---|
| Need | Business outcome and required-by date; identify missing evidence |
| Role variants | Relevant grid-engineer evidence; relevant offshore evidence; who validates each |
| Objects | Requisition, candidate, application, assessment and offer identifiers |
| State/gate | From-state, allowed next state, prerequisite and authorized actor |
| Candidate message | What Noor hears, when, who owns accuracy and how questions are answered |
| Privacy | Data purpose, authorized users and retention decision owner; do not assume consent is the only applicable basis |
| Automation | One permitted administrative task and one decision requiring authorized review |
| Exception | Missing evidence, disputed recommendation or rejected handoff; owner and recovery route |
| Architecture decision | Compare central template, local independence and federated core; record trade-off and evidence needed |
| Measures | Speed paired with evidence quality, fairness investigation and candidate experience |
| Tests | Input → expected → actual paper result → evidence note → pass/revise |

**Reference design reasoning:** use shared core objects and explicit gates with justified role/local variants. Do not hard-code that every candidate must possess the same certificate. A missing offshore credential can block the applicable selection/readiness gate while leaving a different role's application unaffected. Define the required gate with accountable business and safety owners.

| Test | Input / challenge | Expected result in this proposed design |
|---|---|---|
| T1 — Urgency and credentials | Sofia requests faster progression; offshore candidate has an uploaded but unvalidated required credential | Administrative waiting may be reduced; applicable evidence gate stays blocked/visible to its owner; no site authorization follows |
| T2 — Recommendation challenged | Noor's application contains relevant evidence despite a low automated recommendation | Authorized reviewer examines approved criteria and evidence; records rationale; no unreviewed adverse decision; candidate communication reflects confirmed state |
| T3 — Offer/handoff mismatch | Accepted approved offer exists, but downstream handoff is rejected or unacknowledged | Do not claim employment/readiness complete; expose exception and owner; prevent contradictory completion messages and uncontrolled duplicate creation |

**Record actual paper behavior:** did your design catch the exception, or did you revise it after seeing the test? A designed expectation is not an executed tenant result.

### Measure the right outcome
- **Case definition of time-to-fill:** accepted-offer date minus approved-requisition date. State treatment of paused/cancelled requisitions and multiple openings before comparing.
- **Credential validation:** applicable candidates with verified required evidence divided by applicable candidates at the defined gate; define denominator/as-of date.
- **Fairness review:** compare progression with appropriate denominators and context, investigate differences and assess job relevance. No simple rate proves absence/presence of discrimination.
- **Candidate experience:** whether messages are accurate and next steps understandable; collect feedback rather than infer satisfaction from speed.
- **Handoff completion:** only count confirmed outcomes under agreed acceptance criteria.

No numeric target or realized improvement is asserted.

**Acceptance:** explain all five generations; distinguish all six objects; assign boundaries; satisfy the three tabletop expectations after documented revisions; state what remains untested. An unauthorized employment decision or safety bypass requires redesign.

## 9. High-impact resources — read with a question

| Resource | Selective use within sprint | Question |
|---|---|---|
| [SAP — Overview of Recruiting](https://learning.sap.com/courses/navigating-the-employee-lifecycle-through-sap-successfactors/overview-of-sap-successfactors-recruiting) | 5 minutes during general/energy translation | Which responsibilities belong to attraction, recruiting and offers? |
| [SAP — Recruiter experience](https://learning.sap.com/courses/explore-sap-successfactors-solutions/reviewing-the-recruiter-experience-in-sap-successfactors-recruiting_bb963912-92c4-4d1b-8091-4bcc97fd79fc) | 4 minutes during ownership | Where are screening evidence and offer activities represented? |
| [SAP — Candidate application](https://learning.sap.com/courses/sap-successfactors-recruiting-recruiter-experience-project-team-orientation/explaining-candidate-application) and [candidate profile](https://help.sap.com/docs/successfactors-recruiting/setting-up-and-maintaining-sap-successfactors-recruiting/candidate-profile-in-sap-successfactors) | 4 minutes during build | How does a candidate differ from one application? |
| [SAP — Job requisitions](https://help.sap.com/docs/successfactors-recruiting/setting-up-and-maintaining-sap-successfactors-recruiting/025f199fb0ca4b65b8ac1ee2944d22c4.html) | 3 minutes during build | Which roles, fields and local differences require configuration? |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Optional next-step reading | How will the owner govern, map, measure and manage risks of assistance? |

Official SAP resources checked 2026-10-19. Access and tenant behavior may vary. This is not a recommendation to migrate products or a claim that optional AI functionality is enabled. The sprint follows the case's SuccessFactors Recruiting context.

## 10. Five-minute rapid review

| Minute | Recall without looking |
|---|---|
| 1 | Name five generations: find → standardize → track → orchestrate → assist. What problem survives each transition? |
| 2 | Distinguish position, requisition, candidate, application, evidence and offer. Can two applications for one person differ? |
| 3 | Who owns attraction, recruiting states, validation, onboarding, employment and site authorization? |
| 4 | Explain all three tests. Which administrative task can be accelerated without removing a decision gate? |
| 5 | Give Sofia a 60-second answer: how will you increase speed while preserving evidence, fairness and candidate trust? |

**Pass phrase:** “A faster pipeline is valuable only when its decisions remain relevant, explainable and accountable.”

**Next Pre-Foundation experiment:** define one role's requisition fields, application stages, approved assessment rubric, permissions, message triggers and handoff acceptance. Validate with Arjun, the hiring owner and the candidate perspective.

## 11. Sources, stable IDs and standards boundaries

| Source | Reuse and evidence status |
|---|---|
| [OmniVerse enterprise case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd) | Fictional enterprise identity, scale and energy context |
| [OVE-HR02a canonical recruiting case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/hr02a-recruiting.md) | Five personas/IDs, 450-role scenario, 200-hire pressure, four decision scenes, ownership, time-to-fill definition; all fictional |
| [HR studio](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/README.md) | HR01, HR02a recruiting and HR02b onboarding boundaries; source namespace remains OVE-HR02a despite curriculum series HR02-ATA2 |
| [Original Notion research link preserved in source](https://app.notion.com/p/d6d16db9507b453fa4cbad6eaeec9eeb) | Lineage only; source content read from its preserved GitHub snapshot in this publication |
| [Enterprise source register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/references/source-and-assumptions.md) | Distinguish baselines, assumptions, targets and observed evidence |
| Official SAP resources above | Product concepts; not evidence of an OmniVerse deployment |
| New teaching material | Five-generation model, dialogue, future scenes, synthetic identifiers, proposed gates and tests are educational synthesis/illustrative design |

**Trace:** OVE-HR02a-CAP01 demand authorization/candidate assessment/offer governance → OVE-HR02a-VS01 → OVE-HR02a-REQ01/02 → OVE-HR02a-ADR01 → this tabletop derivative of OVE-HR02a-EXP01/T01. No observed evidence is inserted into OVE-HR02a-EV01 by publishing a lesson.

**Educational standards alignment:** TOGAF for application responsibilities/options; BIZBOK for capabilities versus value stages; BABOK for needs, requirements and acceptance; DAMA for candidate-data ownership/quality; COBIT for decision accountability; ISO/IEC 27001 principles for access and information protection. These mappings do not establish compliance or reproduce proprietary standards.

**Publication:** manually authored HR02 derivative in architecture-center-atlas. Historical generations are broad teaching lenses; imagined future scenes are not forecasts. No tenant tests, actual hires, student enrollment, Notion/Drive refresh or unattended synchronization are claimed.
