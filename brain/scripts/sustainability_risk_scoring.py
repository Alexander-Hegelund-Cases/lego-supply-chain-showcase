import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def apply_sustainability_scoring():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Applying Sustainability ESG Risk Scores to Suppliers...")
        
        # 1. Base ESG Risk by Category
        session.run("""
        MATCH (s:Supplier)
        SET s.esg_risk_score = CASE 
            WHEN s.category CONTAINS 'Petrochemicals' OR s.category CONTAINS 'Polymers' OR s.category CONTAINS 'Chemicals' THEN 0.9
            WHEN s.category CONTAINS 'Packaging' OR s.category CONTAINS 'Cardboard' THEN 0.4
            ELSE 0.2
        END,
        s.mass_balance_certified = false,
        s.lastUpdated = $now
        """, now=now)

        # 2. Assign Mass Balance Certification (60% of high-impact suppliers)
        # We do this in Python to handle the random sampling more easily or via Cypher
        session.run("""
        MATCH (s:Supplier)
        WHERE s.category CONTAINS 'Petrochemicals' OR s.category CONTAINS 'Polymers' OR s.category CONTAINS 'Chemicals'
        WITH s, rand() as r
        WHERE r < 0.6
        SET s.mass_balance_certified = true,
            s.certification_standard = 'ISCC PLUS',
            s.esg_risk_score = s.esg_risk_score - 0.5
        """)

        print("Propagating ESG Scores to Factories...")
        # 3. Propagate to Factory
        session.run("""
        MATCH (s:Supplier)-[:SOURCES_TO]->(f:Factory)
        WITH f, avg(s.esg_risk_score) as avg_esg
        SET f.avg_esg_risk = avg_esg,
            f.lastUpdated = $now
        """, now=now)

        print("Propagating ESG Scores to Sets...")
        # 4. Propagate to Set (Sustainability Risk based on building factories)
        session.run("""
        MATCH (f:Factory)-[:TRANSFORMS_TO]->(s:Set)
        WITH s, max(f.avg_esg_risk) as max_factory_risk
        SET s.sustainability_risk = max_factory_risk,
            s.lastUpdated = $now
        """, now=now)

        print("Propagating ESG Scores to Themes...")
        # 5. Propagate to Theme
        session.run("""
        MATCH (s:Set)-[:IN_THEME]->(t:Theme)
        WITH t, avg(s.sustainability_risk) as avg_theme_risk
        SET t.sustainability_risk = avg_theme_risk,
            t.lastUpdated = $now
        """, now=now)

    driver.close()
    print("Sustainability risk propagation complete.")

if __name__ == "__main__":
    apply_sustainability_scoring()
