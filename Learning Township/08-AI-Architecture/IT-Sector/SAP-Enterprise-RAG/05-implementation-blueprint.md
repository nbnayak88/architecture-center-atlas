# Implementation Blueprint and Controls

## 20-hour sprint per domain
| Stage | Hours | Deliverable |
|---|---:|---|
| Discover | 4 | Use cases, data classification, access matrix |
| Connect | 4 | Supported API and source contract |
| Build | 4 | Python + embeddings + FAISS + Ollama prototype |
| Validate | 4 | Groundedness, ACL leakage, freshness, latency tests |
| Showcase | 4 | Demo, architecture decisions, evidence |

## Mandatory controls
- Read-only pilot, least privilege, per-user authorization, no unrestricted service-account data disclosure.
- Data minimization for HR, payroll, compensation, candidate and succession records.
- Source text and metadata stored separately from FAISS index; access filters before retrieval and generation.
- Live SAP API calls for mutable business facts; source timestamps and citations in responses.
- Prompt injection defense, secrets management, TLS, retention, encryption, audit and monitoring.
- Explicit human oversight for employment, pay, hiring and promotion decisions.
- Check specific SAP release, licensing, API availability and integration support before production.

## References
- SAP Business Accelerator Hub: https://api.sap.com/
- SAP Help Portal: https://help.sap.com/
- FAISS: https://github.com/facebookresearch/faiss
- Ollama: https://ollama.com/
- Sentence-Transformers: https://www.sbert.net/


---

### Curious to see this come alive?

**What if you could build and validate this architecture in a focused learning sprint?**

Explore the ideas freely here, then join a SuccessLabs Academy live learning session to discuss practical applications and hands-on experiments.

**[Explore our live learning sessions](https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3?utm_source=github&utm_medium=learning_resource&utm_campaign=ai_architecture&utm_content=05-implementation-blueprint.md)**

*No pressure, just curiosity, community and continuous learning.*
