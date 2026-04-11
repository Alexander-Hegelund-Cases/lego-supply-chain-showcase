# ROADMAP: Context Ingestion for the LEGO EKP

> **Goal**: Close the "Knowledge Voids" (KV) identified in the initial audit to achieve **Expert Frontier** status.

## 1. Priority Ingestion Roadmap

| Target Gap | Source Reference | Source Type | Expected $\Delta H$ Impact | Status |
| :--- | :--- | :--- | :--- | :--- |
| **[KV-001] SCOR DS** | **ASCM SCOR Digital Standard (v14.0)** | Standard | **+0.60** (Critical) | 📅 Planned |
| **[KV-002] Carbon Removal** | **LEGO Group: Sustainability Progress 2024** | Report | **+0.45** (High) | 📅 Planned |
| **[KV-003] Material Precision** | **ISO 20400: Sustainable Procurement** | Standard | **+0.30** (Medium) | 📅 Planned |

## 2. Source Details and Ingestion Strategy

### A. ASCM SCOR Digital Standard (v14.0)
- **Reference**: [ASCM SCOR DS](https://www.ascm.org/scor-ds/)
- **Core Concepts**: Plan, Source, Make, Deliver, Return, Enable, Resilience.
- **Ingestion Strategy**: 
    - Map existing `SUPPLIES` relationships to `SOURCE`.
    - Map `BUILDS` to `MAKE`.
    - Formalize **Resilience** metrics (MTTF, MTTR) as properties on `Factory` nodes.
- **Impact**: Enables "Enterprise-Interoperable" supply chain analysis.

### B. LEGO Group Sustainability Progress 2024 (and 2025 Targets)
- **Reference**: [LEGO Sustainability Reports](https://www.lego.com/en-us/aboutus/sustainability/reporting)
- **Core Concepts**: 52% sustainable material (Renewable/Recycled), $2.8M Carbon Removal, 56% paper-based secondary packaging.
- **Ingestion Strategy**: 
    - Create a **"Sustainability Balance Sheet"** node in the graph.
    - Implement the **Mass Balance Accounting** logic in Python scripts for the EKP.
- **Impact**: Provides "Expert-Level" ESG reporting for the Sustainability persona.

### C. ISCC PLUS (International Sustainability & Carbon Certification)
- **Reference**: [ISCC PLUS Standard](https://www.iscc-system.org/certification/iscc-plus/)
- **Core Concepts**: Chain of Custody, Mass Balance, Circular Economy.
- **Ingestion Strategy**: 
    - Formalize the **ISCC PLUS Certification** as a property on `Supplier` nodes.
    - Link `Supplier` nodes to the `Mass Balance Accounting` Context Atom.
- **Impact**: Validates the "Sustainable Resin" claim with global audit standards.

## 3. Current Status (Sprint G-01-S04 Completed)
- [x] Ingest **SCOR DS** process hierarchy into `/brain/context/`.
- [x] Integrate **FAIR(EST)** principles across documentation.
- [x] Masterful Storytelling & UX Overhaul (`README.md` revamp, Glossary creation).

## 4. Phase 2: Predictive Orchestration (Roadmap)

### Tier 4: Advanced Planning & Optimisation (APS, PSI, CPFR)
- **APS (Advanced Planning and Scheduling)**: Move from simple lead-time propagation to machine-level constraint modelling (Molding Machine Capacity, Cooling Time Precision).
- **PSI (Purchases, Sales, and Inventory)**: Implement a real-time balance sheet for all 20,000+ LEGO parts, predicting "Stock-Out" events 6 months in advance based on Tier 2 disruptions.
- **CPFR (Collaborative Planning)**: Build an "External Partner Portal" where suppliers (e.g., Chi Mei, Braskem) can securely share production forecasts directly into the EKP via Federated Graph (Neo4j Fabric).
- **Impact**: Transforms the EKP from a "Knowledge Graph" into a "Digital Twin Control Tower."
