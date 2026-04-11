---
title: "Mass Balance Accounting for Sustainable Resin"
domain: "sustainability"
ontology_alignment: "ISCC PLUS, SCOR DS (Source)"
confidence_score: 0.85
hardening_delta: 0.42
source_lineage:
  - type: "external"
    reference: "LEGO Group Annual Report 2024"
    notes: "Confirmed 52% renewable/recycled content in products, largely via mass balance."
  - type: "external"
    reference: "ISCC PLUS System Document v3.4"
    notes: "Canonical framework for mass balance chain of custody."
relationship_mapping:
  parents: ["Sustainability Frameworks"]
  children: ["Resin Procurement Protocols"]
  peers: ["Carbon Accounting", "Supplier Risk Scores"]
rag_metadata:
  chunk_type: "procedure"
  semantic_keys: ["mass balance", "renewable resin", "ISCC PLUS", "circular economy"]
last_validated: "2026-04-07"
success_impact:
  metrics: ["G-01-ESG-COMPLIANCE", "G-01-REPORT-QUALITY"]
  notes: "Ensures the KG accurately models the 52% sustainable material claim without assuming physical segregation."
---

# Definition
Mass Balance Accounting is a chain-of-custody model that tracks the total amount of sustainable content (e.g., renewable or recycled feedstock) entering a complex production system and ensures it is allocated correctly to the final output. It allows for the mixing of sustainable and fossil-based materials during manufacturing while maintaining an auditable record of the sustainable volume.

## Scope and Boundaries
This concept covers the **administrative and economic allocation** of sustainable materials within the LEGO supply chain. It explicitly does **not** guarantee that every individual LEGO brick contains a specific percentage of recycled molecules, as materials are mixed at the supplier level.

## Industry Standard Alignment (ISCC PLUS)
The LEGO Group utilises the **ISCC PLUS (International Sustainability and Carbon Certification)** standard. This aligns with the **SCOR DS "Source"** process, where "Certified Sustainable" inputs are tracked via credits and volume balances rather than physical segregation.

## LEGO Implementation Nuance
In 2024, the LEGO Group achieved **52% renewable/recycled content**, a significant increase from 33% in 2023. This is primarily achieved by purchasing **certified mass balance resin** (e.g., derived from used cooking oil or plant-based waste). 
- **Technical Nuance**: 60% of all materials purchased in 2024 were certified mass balance.
- **Precision**: This approach allows LEGO to utilise existing injection molding infrastructure (0.002mm tolerances) without the performance degradation sometimes seen in pure mechanical recycling.

## Implementation Guidance
- **Neo4j Modelling**: Relationships between `Supplier` and `Factory` should carry properties for `mass_balance_certified: true` and `certification_standard: 'ISCC PLUS'`.
- **Query Logic**: When calculating a "Set Sustainability Score," the logic must aggregate the `mass_balance_credits` flowing through the `Part -> Factory -> Supplier` path.
- **Reporting**: Distinguish between "Segregated" (3% of LEGO materials) and "Mass Balance" (52% of LEGO materials) in all EKP dashboards.
