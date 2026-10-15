# 03 — Data, Security and Non-functional Architecture

[← Home](README.md) · [Next →](04-process-journeys.md)

## Information domains and ownership
| Domain | Key entities | Proposed authoritative owner |
|---|---|---|
| Customer | Customer ID, utility account, service point | SAP IS-U |
| Application | Application ID, tier, status, timestamps, approvals | Newgen |
| Service | Inquiry, complaint, case, communication | SAP C4C |
| Network | Feeder, transformer, substation, location | GIS |
| Engineering | Study, calculated hosting capacity, constraints | CYME / engineering |
| Contractor | Organization, license, qualification, validity | Approved registry |
| Documents | Drawings, permits, inspection evidence | IBM DMS |
| Field work | Work order, visit, inspection, completion | SAP PM / IFS FSM |
| Metering and billing | Meter, import/export energy, credit, invoice | SAP IS-U |
| Analytics | Curated dimensions, facts, KPI snapshots | Cloudera |

**Cross-system keys:** application_id, account_id, meter_id, network_asset_id, study_id, contractor_id, case_id, work_order_id and invoice_id. Maintain a governed cross-reference rather than copying authoritative attributes without controls.

## Hosting capacity information
Expose available, reserved, connected and pending capacity as separately defined measures. The data model must distinguish physical capacity, planning assumptions, study validity, capacity reservation and pending application demand. Define calculation ownership, refresh cadence, stale-data warning, reservation timeout and release/recalculation triggers.

## Data lifecycle
Capture → Validate → Persist in authoritative system → Integrate → Reconcile → Curate for analytics → Retain/archive → Dispose under approved policy.

## Security controls (recommended)
- Central identity federation and MFA for privileged or partner access.
- RBAC/ABAC separating consumers, contractors, consultants, engineers, reviewers and service agents.
- Tenant / account-level authorization; no cross-customer exposure.
- Encryption in transit and at rest, managed keys and secrets rotation.
- Data minimization, masking, privacy notices and approved retention schedules.
- Immutable or tamper-evident evidence for regulatory decisions and approvals.
- Signed or legally valid consent and agreement capture where required.
- Full audit chain for rule versions, capacity studies, decisions, fee changes and billing adjustments.
- Vulnerability scanning, secure SDLC, penetration testing and third-party access reviews.

## Non-functional requirement register — targets to be agreed
| NFR | Acceptance criterion template |
|---|---|
| Availability | Define monthly uptime target per critical journey |
| Response time | Define p95 API and portal latency by operation |
| Scalability | Test peak applications, concurrent sessions and study jobs |
| Reliability | Define delivery guarantee, retry and reconciliation limits |
| Recovery | Approve RTO/RPO by platform and integration tier |
| Accessibility | Verify WCAG level and bilingual interface requirements |
| Observability | Trace every request with end-to-end correlation ID |
| Auditability | Retrieve complete evidence chain by application ID |
| Data freshness | Define maximum age of hosting-capacity and meter datasets |
| Security | Pass threat-model, penetration and access-control tests |

No numeric service targets are asserted because they require business and infrastructure validation.

## Data quality tests
Validate uniqueness, completeness, referential integrity, license validity, meter/account matching, study version, network-asset consistency, duplicate payment detection and invoice reconciliation. Publish owners, exception queues and remediation SLAs.
