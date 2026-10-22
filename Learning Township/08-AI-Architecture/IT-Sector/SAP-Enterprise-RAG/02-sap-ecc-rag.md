# RAG for SAP ECC — What, Why, How

## What
A separate customer-hosted Python RAG application integrating with SAP ECC 6.0 using approved read-only RFC/BAPI, OData where available, IDoc-based extracts, and curated documentation. Embeddings: Sentence-Transformers; search: FAISS-CPU; local LLM runtime: Ollama.

## Why
Reduce dependence on undocumented custom processes; speed support, configuration discovery, ABAP knowledge transfer, and S/4HANA transformation readiness.

## How
1. Discover use case and permissions.
2. Expose approved interfaces, avoid unrestricted direct table reads.
3. Normalize approved policy, configuration, ABAP and incident documents.
4. Embed and index with metadata, source IDs and ACLs.
5. Retrieve authorized context; call SAP live for current transactional state.
6. Run local Ollama inference and return citations.
7. Evaluate correctness, access control, latency, freshness and recovery.

## Five examples
| Use case | Question | Sources |
|---|---|---|
| Procurement | Why is a PO blocked? | MM APIs + release strategy docs |
| Finance | Why did posting fail? | FI diagnostics + posting runbooks |
| ABAP | What does Z enhancement do? | Approved code and specs |
| AMS | How was an incident fixed? | Ticket history and runbooks |
| Transformation | Which custom dependencies matter? | Interface inventory, custom code docs |

## Deployment
Customer data center can operate without public LLM APIs after provisioning. Production requires authentication, encryption, access-aware retrieval, monitoring, model governance and backup.
