import os
import json
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

DATA_FILE = "data/raw/tier2_suppliers.json"

def ingest_tier2_suppliers():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found.")
        return

    with open(DATA_FILE, "r") as f:
        tier2_data = json.load(f)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()

    with driver.session() as session:
        # 1. Ensure a constraint for uniqueness
        session.run("CREATE CONSTRAINT supplier_name_unique IF NOT EXISTS FOR (s:Supplier) REQUIRE s.name IS UNIQUE")

        print(f"Ingesting {len(tier2_data)} Tier 2 suppliers...")

        for s2 in tier2_data:
            # Create/Update Tier 2 Supplier
            session.run("""
            MERGE (sup:Supplier {name: $name})
            SET sup.location = $location,
                sup.category = $category,
                sup.tier = $tier,
                sup.esg_score = $esg_score,
                sup.lastUpdated = $now,
                sup.is_synthetic = false,
                sup.source = 'T-06.2.1-Research'
            """, name=s2['name'], location=s2['location'], category=s2['category'], 
                 tier=s2['tier'], esg_score=s2['esg_score'], now=now)

            # Link to Tier 1 Suppliers
            for s1_name in s2.get('supplies', []):
                # Ensure Tier 1 exists (or merge if already there)
                # If it exists, we just set tier: 1 if not set
                session.run("""
                MERGE (s1:Supplier {name: $s1_name})
                ON CREATE SET s1.tier = 1, s1.is_synthetic = true, s1.source = 'T-06.2.2-Placeholder'
                
                MATCH (s2:Supplier {name: $s2_name})
                MATCH (s1:Supplier {name: $s1_name})
                MERGE (s2)-[r:SOURCES_TO]->(s1)
                SET r.lastUpdated = $now,
                    r.is_synthetic = true,
                    r.scor_id = 'sS',
                    r.process_level = 1,
                    r.source = 'T-09-SCOR-Ingestion'
                """, s1_name=s1_name, s2_name=s2['name'], now=now)

    driver.close()
    print("Tier 2 Ingestion Complete.")

if __name__ == "__main__":
    ingest_tier2_suppliers()
