# SAP Enterprise RAG — IT Sector | AI Architecture

SuccessLabs Academy | Architecture Stream 08 — AI | GICS Information Technology

## What
A self-hosted retrieval-augmented generation reference architecture using Python, Sentence-Transformers, FAISS-CPU and Ollama. Covers SAP ECC, SAP S/4HANA On-Premise, Cloud Private Edition, Cloud Public Edition, and SAP SuccessFactors.

## Why
Evidence-grounded SAP support, configuration knowledge discovery, integration troubleshooting, HR policy explanation, transformation discovery and knowledge transfer. Not a replacement for SAP transactional processing or authoritative business decisions.

## Contents
- [Technology comparison](01-faiss-vs-ollama.md)
- [ECC reference architecture](02-sap-ecc-rag.md)
- [S/4HANA deployment architectures](03-s4hana-three-deployments.md)
- [SuccessFactors: 66 use cases](04-successfactors-66-use-cases.md)
- [Implementation and security](05-implementation-blueprint.md)

## Architecture decision
Keep SAP as system of record. Deploy Python RAG separately; use supported APIs, source-level permissions, authorized live reads, citations, auditing, and read-only initial operation. Fully local end-to-end operation is possible for on-premises SAP, but not for SaaS SAP SuccessFactors or S/4HANA Public Cloud.


---

### Curious to see this come alive?

**What if the next architecture you study becomes something you can demonstrate?**

Explore the ideas freely here, then join a SuccessLabs Academy live learning session to discuss practical applications and hands-on experiments.

**[Explore our live learning sessions](https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3?utm_source=github&utm_medium=learning_resource&utm_campaign=ai_architecture&utm_content=README.md)**

*No pressure, just curiosity, community and continuous learning.*
