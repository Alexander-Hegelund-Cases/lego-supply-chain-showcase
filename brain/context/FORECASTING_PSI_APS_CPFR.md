---
title: "Advanced SCM: Forecasting, PSI, APS, and CPFR"
domain: "supply_chain"
ontology_alignment: "SCOR DS v14.0, APICS, IBF"
confidence_score: 0.95
hardening_delta: 0.45
source_lineage:
  - type: "external"
    reference: "ASCM (Association for Supply Chain Management)"
    notes: "SCOR DS v14.0 'Plan' and 'Orchestrate' levels."
  - type: "external"
    reference: "IBF (Institute of Business Forecasting)"
    notes: "Demand planning and PSI synchronization."
relationship_mapping:
  parents: ["SCOR_DS_v14_0_ONTOLOGY.md"]
  children: ["lead_time_propagation.py"]
  peers: ["CALCULATION_LOGIC.md"]
rag_metadata:
  chunk_type: "concept"
  semantic_keys: ["PSI", "APS", "CPFR", "Forecasting", "Demand Planning"]
last_validated: "2026-04-08"
success_impact:
  metrics: ["G-01-O2", "G-01-O3"]
  notes: "Enables predictive resilience and margin protection."
---

# Definition
Advanced SCM focuses on the synchronization of supply and demand through predictive modelling (**Forecasting**), constraint-based optimisation (**APS**), and collaborative data sharing (**CPFR**) to maintain a healthy balance of **Purchases, Sales, and Inventory (PSI)**.

## Scope and Boundaries
This context covers the strategic planning layer of the EKP, moving beyond reactive "What happened?" to proactive "What will happen?" and "What should we do?"

## Industry Standard Alignment

### 1. Forecasting & Demand Planning
- **Statistical Forecast**: Baseline demand based on historical theme popularity (e.g., Star Wars vs. Botanicals).
- **Consensus Forecast**: Integration of Sales, Marketing, and Supply Chain inputs (S&OP).
- **KG Implementation**: `(Region)-[:FORECASTS_DEMAND {volume, confidence}]->(Set)`.

### 2. PSI (Purchases, Sales, and Inventory) Planning
- **Purchases (P)**: Inbound material/component flow from Tier 1/2 suppliers.
- **Sales (S)**: Outbound finished goods to regions.
- **Inventory (I)**: The "Buffer" or "Stock on Hand" at Factories and Hubs.
- **Balance Equation**: $Ending\_Inventory = Beginning\_Inventory + Purchases - Sales$.
- **KG Implementation**: Attributes on `Factory` and `Hub` nodes: `inventory_level`, `safety_stock`, `reorder_point`.

### 3. APS (Advanced Planning and Scheduling)
- Constraint-based production scheduling.
- **Constraints**: Molding machine capacity (e.g., 24/7 run-time), mold availability, material constraints (ABS vs. Bio-PE).
- **KG Implementation**: `(Factory)-[:HAS_CAPACITY {machine_hours, throughput_rate}]->(Machine)`.

### 4. CPFR (Collaborative Planning, Forecasting, and Replenishment)
- A business practice where supply chain partners (e.g., LEGO and Braskem) share information and synchronize their planning.
- **Collaboration Atoms**: Shared demand signals, visibility into Tier 2 production schedules.
- **KG Implementation**: `(Supplier)-[:COLLABORATES_WITH {shared_forecast: true}]->(LEGO)`.

## LEGO Implementation Nuance
- **The "Clutch Power" Constraint**: APS must account for cooling times in molding to maintain precision.
- **Theme-Level PSI**: High-volatility themes (e.g., licensed IP like Marvel) require more aggressive safety stock in PSI planning compared to "Evergreen" themes (e.g., City).

## Implementation Guidance
- **Scenario Planning**: Use "What-If" scenarios to test PSI balance under disruption (e.g., "If Taiwan delay = 21 days, calculate Stock-Out risk for Technic theme").
- **Value Offering**: The EKP should provide a "PSI Dashboard" query that identifies themes where $Sales > (Inventory + Purchases)$.
