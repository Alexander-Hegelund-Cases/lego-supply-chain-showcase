# G-01: The LEGO Supply-Chain & Sustainability KG

## 1. Project Goal: The Core Job (JTBD)
"When I am a LEGO decision-maker navigating a complex, multi-tier supply chain, I want a **Graph-based Semantic Layer**, so that I can see the connections that are invisible in our legacy ERP silos."

### Reasoning for the Graph Deliverable:
Graph is the *only* technology that treats relationships as first-class citizens, making it the bedrock for cross-functional decision support and mitigating the **Business Viability Risk** of data fragmentation.

## 2. Risk Mitigation Strategy (The 4 Big Risks)
| Risk | Mitigation in G-01 |
| :--- | :--- |
| **Value Risk** | Selecting "SPOF" and "2032 Target" scenarios that provide immediate ROI to the COO/CTO. |
| **Usability Risk** | Designing the "Guided Tour" notebook UX for non-technical stakeholders. |
| **Feasibility Risk** | Proving Neo4j can handle 26k+ nodes and multi-tier cascades in a single ingestion. |
| **Business Viability** | Aligning with SCOR DS v14.0 and official LEGO sustainability goals. |

## 3. Primary Personas & Their Jobs
*   **Supply Chain Planner / S&OP Analyst**: "Identify the ripple effect of a supplier outage."
*   **Sustainability Analyst**: "Verify our distance to the 2032 100% sustainable materials target."
*   **Knowledge Platform Engineer**: "Ensure enterprise data is FAIR(EST) and interoperable."

## 3. Key Decision-Support Questions
1.  **Risk Exposure**: If Supplier X fails, which sets/themes/regions are affected?
2.  **Downstream Impact**: If Factory Y goes offline, what is the downstream impact on product availability?
3.  **Concentration Risk**: How concentrated are we on specific suppliers/factories per theme or region?
4.  **Sustainability Propagation**: Which products are most exposed to sustainability risk via high-risk suppliers?

## 4. Target Data Model
*   **Nodes**: `Supplier`, `Factory`, `Region`, `Set`, `Theme`, `Part` (+ optional `Material`, `RiskEvent`).
*   **Relationships**:
    *   `Supplier -[:SUPPLIES]-> Factory`
    *   `Factory -[:BUILDS]-> Set`
    *   `Factory -[:SERVES]-> Region`
    *   `Set -[:CONTAINS {qty}]-> Part`
    *   `Set -[:IN_THEME]-> Theme`

## 5. Metadata & Governance (FAIR(EST) Alignment)
Every node and relationship must include:
*   `source`: The origin of the data (e.g., Rebrickable, LEGO Supplier List).
*   `lastUpdated`: ISO timestamp of the last modification.
*   `dataConfidence`: A score (0.0-1.0) or label (e.g., `verified`, `simulated`) to reflect data quality.
*   `is_synthetic`: Boolean flag to distinguish between source-backed and simulated data.

## 6. Business Metrics (EKP Success Indicators)
*   **Coverage**: % of LEGO themes or product lines mapped in the graph.
*   **Freshness**: Time since the last data ingestion.
*   **Query Latency**: Speed of impact analysis queries.
*   **Scenario Support**: Number of distinct supply-chain or sustainability scenarios modelled.

## 7. Current Progress Tracking

| Milestone | Status | Date | Note |
| :--- | :--- | :--- | :--- |
| **Foundation** | ✅ Done | 2026-04-06 | Ingested Rebrickable & Supplier data. |
| **SPOF Analysis** | ✅ Done | 2026-04-07 | Implemented scaled risk scoring and SPOF detection. |
| **Sustainability** | ✅ Done | 2026-04-07 | Implemented ESG Propagation (Mass Balance). |
| **Visualization** | ✅ Done | 2026-04-07 | In-notebook interactive pyvis network graphs. |
