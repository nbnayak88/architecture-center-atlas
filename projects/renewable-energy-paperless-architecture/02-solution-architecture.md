# 02 — Application and Integration Architecture

[← Home](README.md) · [Next →](03-data-security.md)

## Logical application responsibilities
| Platform | Primary responsibility | Boundary |
|---|---|---|
| Sitecore web/mobile/partner portals | Digital experience and guided submissions | Not the authoritative workflow state |
| Newgen | Tier-based workflow, application state, approvals, handoffs | Not customer billing ledger |
| SAP C4C | Service enquiries, complaints, escalations and communications | Not authoritative engineering approval |
| GIS | Geospatial network asset reference | Not grid-study calculation engine |
| CYME | Hosting capacity and grid-impact analysis | Not application case manager |
| SAP IS-U | Customer utility accounts, metering, billing and settlement | Not front-end workflow orchestration |
| SAP PM / IFS FSM | Maintenance, field activity and inspection execution | Not regulatory rule owner |
| IBM DMS | Submitted documents, evidence and archival | Not application business-state authority |
| Enterprise integration layer | API mediation, routing, transformation and transport | Not business system of record |
| Cloudera | Governed historical / analytical data | Not transactional master by default |
| Power BI | Dashboards, operational KPIs and reporting | Not source-of-truth transactional store |

## Core integration catalog (proposed interface contracts)
| ID | Producer → Consumer | Payload / trigger | Pattern | Key controls |
|---|---|---|---|---|
| INT-01 | Portal → Newgen | New application and attachments | API | Idempotency key, schema validation |
| INT-02 | Portal → SAP C4C | Inquiry / complaint | API | Case correlation ID |
| INT-03 | Newgen ↔ SAP IS-U | Account, meter and service point validation | API | Authoritative identifiers |
| INT-04 | Newgen ↔ GIS/CYME | Capacity check, study request, result | API + async | Study version, expiry, engineer sign-off |
| INT-05 | Newgen ↔ Registries | License and contractor validation | API | Credential validity and consent |
| INT-06 | Newgen ↔ Authorities | Permit request, decision and evidence | API or controlled interim manual | Correlation, legal evidence |
| INT-07 | Newgen ↔ Payment gateway | Fee request and receipt confirmation | API + callback | Reconciliation, duplicate protection |
| INT-08 | Newgen ↔ Field systems | Inspection/installation work orders | API + events | Safety hold, completion evidence |
| INT-09 | Commissioning → SAP IS-U | Connection activation and billing configuration | API/event | Meter mapping, acknowledgement |
| INT-10 | Operational sources → Cloudera | Governed data ingestion | Batch/stream | Lineage, DQ rules, latency |
| INT-11 | Cloudera → Power BI | Curated reporting datasets | Governed datasets | KPI definitions, row security |
| INT-12 | Newgen ↔ SAP C4C | Application status, cases, escalations | Events/APIs | No dual workflow ownership |

Patterns are **recommendations** pending API/platform verification; they are not guaranteed existing interfaces.

## Integration quality
- Publish OpenAPI specifications, payload examples and version policy.
- Require correlation IDs across application, customer case, grid study, work order and invoice.
- Use retries with exponential backoff and dead-letter handling for transient failures.
- Implement idempotent create/update operations and explicit duplicate detection.
- Reconcile asynchronous messages against authoritative operational systems.
- Classify integrations by real-time, near-real-time or batch requirement.
- Protect public-facing endpoints with authentication, throttling, bot protection and audit trails.
- Monitor latency, failure rate, backlog, business exceptions and end-to-end completion.

## Architecture decision records
**ADR-001 — Workflow:** Newgen owns the renewable application lifecycle; SAP C4C owns service cases.  
**ADR-002 — Technical study:** GIS supplies network reference; CYME supplies engineering calculations.  
**ADR-003 — Billing:** SAP IS-U remains billing system of record.  
**ADR-004 — Data:** Cloudera supports governed analytics; source applications retain operational authority.  
**ADR-005 — Integration:** Prefer enterprise integration services to point-to-point coupling.  
**ADR-006 — Regulation:** Version tier rules and approval policy outside hardcoded journey logic.

Each ADR needs alternatives, trade-offs, approver, status and review date before final acceptance.

## Open decisions
Confirm C4C edition, Newgen implementation scope, API gateways and middleware variants, real-time capacity freshness, authoritative state machine, document signature mechanism, disaster recovery topology and external authority integration readiness.
