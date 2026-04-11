# Definition of Done (DoD) for Portfolio-Ready v1.0

This document defines the criteria for "v1.0: Portfolio Ready" for the LEGO Supply-Chain & Sustainability Knowledge Graph (EKP Prototype). Meeting these criteria ensures the repository effectively demonstrates the strategic and technical capabilities required for the **Senior Product Manager - Enterprise Knowledge Platform** role.

## 1. Functional Decision-Support Scenarios
The Knowledge Graph must successfully demonstrate two high-value business scenarios:
- [x] **Scenario 1: Supply Chain Resilience (T-06)**: Identify Single Points of Failure (SPOFs) at scale (26k+ sets).
- [ ] **Scenario 2: Sustainability & ESG Propagation (T-07)**: Map ESG risk from Tier 2 suppliers to finished LEGO sets using "Mass Balance" accounting principles.

## 2. Technical Excellence & Governance (FAIR(EST))
- [x] **Scalability**: Successfully ingest and query the full Rebrickable dataset (26,467 sets, 492 themes).
- [x] **Governance Metadata**: Every node and relationship must contain `source`, `dataConfidence`, `lastUpdated`, and `is_synthetic` properties.
- [ ] **Data Catalog**: A formalized `brain/model/DATA_CATALOG.md` documenting the schema, properties, and governance rules.

## 3. High-Fidelity Storytelling (The Notebook)
The `notebooks/lego-knowledge-graph.ipynb` must be a self-contained product demo:
- [x] **Executive Context**: Markdown cells explaining the business "Why" for each query.
- [ ] **Visual Evidence**: Integrated graph visualizations (e.g., using `pyvis`) to highlight risk clusters.
- [x] **Actionable Metrics**: Clear data outputs showing specific at-risk product lines and themes.

## 4. Strategic Product Roadmap
- [x] **Strategic Narrative**: A documented link between technical execution and the Senior PM job description (`brain/context/hiring/STRATEGIC_NARRATIVE.md`).
- [ ] **Future Vision (v2.0)**: A roadmap section in the README detailing future platform capabilities (e.g., Digital Twin integration, Generative AI for ontology mapping).

## 5. Metadata & Documentation
- [x] **README.md**: Clear "Section 0" vision statement and role alignment.
- [x] **Domain Context**: Formalized expert context atoms (DCA framework) in `/brain/context/`.
- [x] **Clean Handover**: Structured session rituals and next-session prompts to demonstrate platform engineering discipline.

---
*Target Completion: End of Sprint G-01-S02 (The "Decision Support" Engine).*
