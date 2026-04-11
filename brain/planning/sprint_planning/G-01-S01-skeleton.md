 # Sprint G-01-S01: The FAIR(EST) Foundation (Skeleton & Ingestion)

   ## 1. Mission Objectives
   **Goal**: Establish the structural "Knowledge Graph" foundation using real Rebrickable data and the LEGO Supplier list, demonstrating FAIR(EST) principles from Day 1.

   ## 2. Success Criteria (Definition of Done)
   - [ ] **Environment**: Neo4j (AuraDB or Desktop) is reachable via Python.
   - [ ] **Schema**: Node/Relationship model (Supplier, Factory, Set, Theme, Part) is defined in Cypher.
   - [ ] **Ingestion**:
       - [ ] Rebrickable `sets.csv` and `themes.csv` ingested.
       - [ ] LEGO Supplier List (Public PDF data) ingested as `Supplier` nodes.
   - [ ] **Governance**: Every node has `source`, `dataConfidence`, and `lastUpdated` properties.
   - [ ] **FAIR(EST) Assessment**: Initial "Data Inventory" table drafted in the notebook.

   ## 3. High-Signal Tasks
   | Task | Description | Priority |
   | :--- | :--- | :--- |
   | **T-01: Environment Setup** | Initialize Neo4j connection and test driver connectivity. | High |
   | **T-02: Schema Design** | ASCII/Mermaid diagram of the Graph model (Nodes/Edges). | High |
   | **T-03: Rebrickable Ingestion** | Script to pull/load CSVs into Neo4j with constraints. | Medium |
   | **T-04: Supplier Bootstrap** | Manual/Scraped entry of top 10-20 LEGO Suppliers. | Medium |
   | **T-05: Synthetic Wiring** | Create `(:Supplier)-[:SUPPLIES]->(:Factory)` links for scenario analysis. | Medium |

   ## 4. Risks & Mitigations
   - **Risk**: Rebrickable data is too large for Neo4j Free Tier.
   - **Mitigation**: Filter for specific "Themes" (e.g., Star Wars, Technic) to keep node count low (<50k).
   - **Risk**: Supplier-to-Factory mapping isn't public.
   - **Mitigation**: Explicitly label these relationships as `synthetic: true` for "Scenario Modelling."

   ## 5. Next Session Focus
   - Execute the `neo4j` connection script.
   - Load the first 1,000 nodes from Rebrickable.

   # 6. Future Potential Sprints (Project Roadmap)

  These sprints are designed to move the project from a static database to a dynamic Enterprise Knowledge Platform (EKP), demonstrating the maturity needed for the LEGO role.


  Sprint G-01-S02: The "Decision Support" Engine (High Priority)
   * Focus: Transforming the Graph into an "Answer Machine" for Supply Chain and Sustainability.
   * Key Tasks:
       * T-06: Supply Chain Risk Query: Implement a Cypher query to identify "Single Points of Failure" (e.g., Which Themes rely on a single Factory/Supplier?).
       * T-07: Sustainability Propagation: Model a "Carbon Tax" or "ESG Risk" score that flows from Supplier → Part → Set.
       * T-08: In-Notebook Visualization: Use pyvis or ipycytoscape to create interactive "Impact Maps" for the user.
   * JD Hook: "Aligning partners across technology and business" (Decision Support).


  Sprint G-01-S03: The "FAIR(EST)" Maturity & Governance (Medium Priority)
   * Focus: Demonstrating how the EKP handles data quality, lineage, and interoperability.
   * Key Tasks:
       * T-09: Metadata Catalog: Create a "Data Quality Dashboard" node in the graph that tracks Freshness, Completeness, and Source Reliability for every ingestion job.
       * T-10: Schema Evolution: Implement "Versioned Nodes" to show how the KG handles changes in LEGO's supplier network over time.
       * T-11: FAIR(EST) Scorecard: A programmatic assessment (in Python/Pandas) that scores the graph's data against FAIR(EST) principles.
   * JD Hook: "Collaborating on knowledge graphs, semantic data models, data cataloguing and governance."


  Sprint G-01-S04: The "Adoption & Metrics" Layer (Final Polish)
   * Focus: Proving the business value and "Product Thinking" behind the platform.
   * Key Tasks:
       * T-12: Usage Simulation: Mock up "Search Query Logs" to show which parts of the Graph are most used by LEGO Planners.
       * T-13: ROI Calculator: A markdown-based narrative explaining how the Graph reduces "Time-to-Insight" for the Sustainability team.
       * T-14: 12-Month Roadmap: A visual roadmap (Mermaid Gantt chart) showing the EKP's expansion (e.g., adding "Consumer Sentiment" or "Logistics Latency" nodes).
   * JD Hook: "Promoting adoption, monitoring usage, and iterating based on metrics."
