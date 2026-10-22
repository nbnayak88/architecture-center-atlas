# SAP S/4HANA RAG — Three Deployment Architectures

| Dimension | On-Premise | Cloud Private Edition | Cloud Public Edition |
|---|---|---|---|
| SAP runtime | Customer-managed | Managed private cloud | SAP-managed SaaS |
| RAG runtime | Separate local server | Separate customer-controlled environment | External side-by-side service |
| Interfaces | Released APIs; approved BAPIs/RFC where supported | Supported released APIs and approved interfaces | Released APIs, communication arrangements, events |
| Entire landscape fully local? | Possible | Generally no | No |
| Ollama local to AI environment? | Yes | Yes | Yes |
| Direct DB integration | Avoid | Avoid | Not supported |
| Clean Core | Design objective | Design objective | Strict released extensibility |

## Common logical flow
SAP S/4HANA -> secured approved integration boundary -> Python ingestion/orchestration -> Sentence-Transformers -> FAISS vector index and metadata store -> Ollama local LLM -> cited assistant. For current financial/stock/order data, perform authorized live API reads; do not use stale vector index as system of record.

## What
A reusable RAG core with three deployment-specific SAP adapters.

## Why
Improve P2P, FI/CO, SD, PP, EAM, inventory support and S/4HANA transformation knowledge while preserving ERP boundaries.

## How
Validate API availability per edition and release; provision secure connectivity; index only approved documents; enforce authorization at retrieval; evaluate groundedness, performance, and auditability. Start with a common Purchase-to-Pay scenario across all three editions. SAP BTP is an optional/preferred side-by-side platform depending on edition, not mandatory for a separately self-hosted prototype.
