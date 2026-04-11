# Protocol: Domain Context Architecture (LEGO Supply-Chain & Sustainability)

> **"The Clerk of Context"**: Ensuring all Knowledge Atoms are FAIR(EST)-compliant, RAG-optimised, and industry-standardized.

## 1. The Context Atom Specification (RAG-Optimised)

Every file in `/brain/context/*.md` is an **Atomic Unit of Knowledge**. It MUST represent a single, tightly-scoped concept, pattern, or standard.

### 1.1 Mandatory YAML Frontmatter
The YAML block MUST start every file to enable automated indexing and confidence scoring.

```yaml
---
title: "<Unique human-readable title>"
domain: "<supply_chain|sustainability|kg_modeling|governance>"
ontology_alignment: "<e.g., SCOR DS, ISCC PLUS, FAIR(EST), GHG Protocol>"
confidence_score: <float 0.0 - 1.0>
hardening_delta: <float Cr - Cp>
source_lineage:
  - type: "<internal|external>"
    reference: "<file path, URL, or citation>"
    notes: "<how this source supports the atom>"
relationship_mapping:
  parents: ["<links to broader concepts>"]
  children: ["<links to sub-concepts>"]
  peers: ["<links to related atoms>"]
rag_metadata:
  chunk_type: "<concept|procedure|metric|standard>"
  semantic_keys: ["<term1>", "<term2>"]
last_validated: "<ISO 8601 Date>"
success_impact:
  metrics: ["<goal IDs from G-01-goals.md>"]
  notes: "<impact on project success>"
---
```

### 1.2 Markdown Body Structure
Following the YAML, the body MUST follow this RAG-friendly format:

```markdown
# Definition
<2-4 sentences defining the concept in precise, implementation-ready language.>

## Scope and Boundaries
<What this concept covers and explicitly does not cover.>

## Industry Standard Alignment (e.g., SCOR DS)
<Mapping to global industry standards: Plan, Source, Make, Deliver, Return, Enable.>

## LEGO Implementation Nuance
<LEGO-specific technical details: e.g., 0.002mm tolerances, "clutch power", Mass Balance resin procurement.>

## Implementation Guidance
<How to use this in Neo4j schemas, Cypher queries, or ESG reporting pipelines.>
```

## 2. The Context Hardening Delta ($\Delta H$)

Agents MUST evaluate the **Context Hardening Delta** to quantify value-add:
- **$C_{p}$ (Parametric Confidence)**: The agent's general training knowledge.
- **$C_{r}$ (Retrieval-Augmented Confidence)**: Confidence when using the repository's internal data.
- **$\Delta H = C_{r} - C_{p}$**: 
    - **$\Delta H > 0$**: The repository adds unique, specific value.
    - **$\Delta H \approx 0$**: The repository only contains generic information.
    - **$\Delta H < 0$**: The internal context is stale, incorrect, or contradictory.

## 3. RAG Optimisation Rules
- **Semantic Chunking**: Atoms should be between 300-900 words to ensure complete logical units in vector embeddings.
- **Contextual Prepending**: Every chunk MUST carry the atom's `title` and `domain` to avoid "Context Loss" in the vector store.
- **Hierarchical RAG**: Index the `rag_metadata.semantic_keys` but return the full parent atom for the LLM's final reasoning.

## 4. Governance Enforcement
- **No Direct Creation**: Context Atoms are generated/refined during the **Context Hardening Loop** by an authorized DCA agent.
- **Validation Mandate**: Atoms with a `confidence_score` < 0.6 are flagged as **Knowledge Voids** and require external ingestion (roadmap) or expert review.
- **Lineage over Logic**: Citations to official LEGO reports or industry standards (ISO/[SCOR-DS](../../docs/GLOSSARY.md#scor-ds)) always supersede synthetic assumptions.

<br>
<div align="center">
  <b><a href="../../README.md">🔙 Return to Main README</a></b> | <b><a href="../../docs/GLOSSARY.md">📖 Open the Glossary</a></b>
</div>
