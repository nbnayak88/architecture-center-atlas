# 01 — Business Architecture

[← Home](README.md) · [Next →](02-solution-architecture.md)

## Problem statement
Multiple regulatory regimes, static technical connection limits, complex approvals and qualification journeys, weak application tracking, and fragmented communications inhibit renewable energy self-consumption adoption. The target state harmonizes regulation, uses engineering studies and actual hosting capacity, simplifies tier-specific journeys and digitizes stakeholder interaction.

## Strategic objectives
| Objective | Target business capability | Proposed success indicator |
|---|---|---|
| Unified regulation | Regulatory policy and rules management | Rules harmonized and version-controlled |
| Reduced application friction | Application and approval management | Median cycle time; number of customer steps |
| Safe capacity allocation | Grid hosting-capacity management | Accurate capacity allocation; oversubscription incidents |
| Contractor enablement | Qualification and registry management | Qualification lead time |
| Reliable settlement | Metering, billing and reconciliation | Correct invoices and credits |
| Better experience | Customer service and communication | Satisfaction; complaints resolved within SLA |

These KPIs are proposed measures; no numeric targets are assumed.

## Personas (roles only; no individual identities)
- **Applicant / consumer:** explores eligibility, submits request, pays fees, monitors progress, receives connection outcome.
- **Engineering consultant:** prepares design and feasibility submissions and responds to technical queries.
- **Qualified contractor:** executes installation, submits completion evidence and schedules inspections.
- **Network planning engineer:** evaluates feeder, transformer and substation capacity and approves technical studies.
- **Regulatory reviewer:** checks policy, permits, exceptions and compliance evidence.
- **Field inspector:** records inspection results, safety observations and rework.
- **Customer service agent:** handles enquiries, complaints and escalation.
- **Billing specialist:** verifies import/export readings, credits and billing exceptions.
- **Operations administrator:** monitors queues, workload, SLA and exceptions.
- **Executive / auditor:** reviews service outcomes, regulatory adherence and benefits.

## Business capabilities
1. Regulatory policy and eligibility management
2. Customer identity and account validation
3. Renewable energy application intake
4. Tier classification and journey selection
5. Network capacity discovery and reservation
6. Technical study and engineering assessment
7. Consultant and contractor registration
8. Permit and authority coordination
9. Document, evidence and agreement management
10. Fee assessment and payment confirmation
11. Installation and inspection orchestration
12. Commissioning and grid activation
13. Metering, net billing and settlement
14. Customer enquiries, complaints and communications
15. Monitoring, analytics and compliance reporting
16. Training, certification and stakeholder enablement

## Value stream
Discover eligibility → Authenticate account → Classify tier → Submit application → Validate evidence → Evaluate network capacity → Perform required study → Obtain approvals and permits → Pay fees → Install → Inspect → Commission → Activate billing → Monitor / support.

## As-is versus to-be
| As-is concern | To-be architecture response |
|---|---|
| Multiple regulatory references | Unified, effective-dated rule catalog |
| Fixed technical limits | Engineering-led hosting capacity assessment |
| Repeated forms and approvals | Once-only intake and tier-based orchestration |
| Limited contractor tracking | Self-service portal and transparent status |
| Weak escalation | Customer case management and SLA |
| Limited awareness | Public guidance, learning and feedback services |

## Policy constraints
Capacity tiers and exact legal thresholds must be taken from the approved regulatory framework. This wiki intentionally does not invent thresholds, fees or entitlement rules.

## Ownership model
Business owners approve regulatory and service policies; network engineering owns technical eligibility; billing owns settlement rules; enterprise architecture owns design assurance; delivery teams implement components; security and compliance independently review controls.
