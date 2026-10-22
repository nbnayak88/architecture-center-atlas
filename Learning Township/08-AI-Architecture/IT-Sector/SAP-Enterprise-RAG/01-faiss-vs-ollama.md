# FAISS vs Ollama — SAP HR Example

| Aspect | FAISS | Ollama | Sentence-Transformers |
|---|---|---|---|
| Role | Vector similarity search | Runs local generative models | Produces embeddings |
| Input | Numerical vectors | Prompts and retrieved context | Text passages |
| Output | Vector IDs and distances | Generated answers | Numerical embeddings |
| Generates text? | No | Yes, via model | No |
| Stores source documents? | No; store text/metadata separately | No enterprise document store | No |
| Offline operation | Yes | Yes after model download | Yes after model download |

## Fictional HR bonus example
Employee asks why they are ineligible for a bonus. Sentence-Transformers embeds the question and policy passages; FAISS retrieves a fictional policy requiring 12 months' service; an authorized SAP SuccessFactors API provides hire date; Ollama runs a local LLM to explain the policy with citations. Actual eligibility must be determined by authoritative HR processes, not by the LLM.

## HR module illustrations
- Employee Central: job information rules and effective dates
- Global Benefits: enrollment eligibility
- Time Off: accrual policy
- Recruiting: requisition approval
- Onboarding: task routing
- Performance: rating guidelines
- Compensation: merit guidelines
- Variable Pay: proration and weights
- Learning: curriculum recommendations
- Payroll: error/runbook interpretation


---

### Curious to see this come alive?

**Could you turn this technical concept into a working enterprise experiment?**

Explore the ideas freely here, then join a SuccessLabs Academy live learning session to discuss practical applications and hands-on experiments.

**[Explore our live learning sessions](https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3?utm_source=github&utm_medium=learning_resource&utm_campaign=ai_architecture&utm_content=01-faiss-vs-ollama.md)**

*No pressure, just curiosity, community and continuous learning.*
