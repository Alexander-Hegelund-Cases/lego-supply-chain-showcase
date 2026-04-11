import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def apply_semantic_reframing():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Reframing Sustainability Metrics (Distance to 2032 Target)...")

        # 1. Reframe Materials (Base SC%)
        # Bio-PE and Recycled Paper are considered "Sustainable" (SC% = 100)
        # ABS is considered "Non-Sustainable" (SC% = 0)
        session.run("""
        MATCH (m:Material)
        SET m.sustainability_completion_pct = CASE 
            WHEN m.name IN ['Bio-PE', 'Recycled Paper'] THEN 100.0
            ELSE 0.0
        END,
        m.distance_to_2032_target = 100.0 - m.sustainability_completion_pct,
        m.lastUpdated = $now
        """, now=now)

        # 2. Reframe Suppliers based on ESG Risk
        # SC% = (1 - esg_risk_score) * 100
        session.run("""
        MATCH (s:Supplier)
        WHERE s.esg_risk_score IS NOT NULL
        SET s.sustainability_completion_pct = (1.0 - s.esg_risk_score) * 100.0,
            s.distance_to_2032_target = 100.0 - ((1.0 - s.esg_risk_score) * 100.0),
            s.lastUpdated = $now
        """, now=now)

        # 3. Propagate to Theme (Strategic View)
        # If a theme DEPENDS_ON_MATERIAL, we factor that in
        print("Calculating Theme-level DtT...")
        session.run("""
        MATCH (t:Theme)-[r:DEPENDS_ON_MATERIAL]->(m:Material)
        WITH t, avg(m.sustainability_completion_pct) as mat_sc_pct
        SET t.material_sustainability_pct = mat_sc_pct,
            t.sustainability_completion_pct = mat_sc_pct,
            t.distance_to_2032_target = 100.0 - mat_sc_pct,
            t.lastUpdated = $now
        """, now=now)

        # 4. Refine Theme SC% based on Offsets
        # If a Theme OFFSETS_WITH a CarbonCredit, reduce DtT
        session.run("""
        MATCH (t:Theme)-[r:OFFSETS_WITH]->(c:CarbonCredit)
        WITH t, sum(r.offset_amount) as total_offset
        // Simple logic: each offset amount reduces DtT by 5% (synthetic scaling)
        SET t.sustainability_completion_pct = t.sustainability_completion_pct + (total_offset / 100.0),
            t.distance_to_2032_target = 100.0 - (t.sustainability_completion_pct + (total_offset / 100.0)),
            t.offset_impact = total_offset,
            t.lastUpdated = $now
        """, now=now)

        # 5. Propagate to Set (Tactical View)
        print("Calculating Set-level DtT...")
        session.run("""
        MATCH (s:Set)-[:IN_THEME]->(t:Theme)
        SET s.sustainability_completion_pct = t.sustainability_completion_pct,
            s.distance_to_2032_target = t.distance_to_2032_target,
            s.lastUpdated = $now
        """, now=now)

        # 6. Final Polish: Ensure no DtT is below 0 or SC% above 100
        session.run("""
        MATCH (n) WHERE n:Theme OR n:Set OR n:Supplier OR n:Material
        SET n.sustainability_completion_pct = CASE WHEN n.sustainability_completion_pct > 100 THEN 100 ELSE n.sustainability_completion_pct END,
            n.distance_to_2032_target = CASE WHEN n.distance_to_2032_target < 0 THEN 0 ELSE n.distance_to_2032_target END
        """)

    driver.close()
    print("Semantic reframing (DtT) complete.")

if __name__ == "__main__":
    apply_semantic_reframing()
