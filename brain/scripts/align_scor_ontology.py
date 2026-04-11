import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def align_scor_ontology():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Refactoring Relationships to SCOR DS v14.0...")

        # 1. SUPPLIES -> SOURCES_TO
        print("- Refactoring SUPPLIES to SOURCES_TO (Level 1: Source)")
        session.run("""
        MATCH (a)-[r:SUPPLIES]->(b)
        CREATE (a)-[r2:SOURCES_TO]->(b)
        SET r2 = properties(r),
            r2.scor_id = 'sS',
            r2.process_level = 1,
            r2.lastUpdated = $now,
            r2.source = 'T-09-Ontology-Alignment'
        WITH r
        DELETE r
        """, now=now)

        # 2. BUILDS -> TRANSFORMS_TO
        print("- Refactoring BUILDS to TRANSFORMS_TO (Level 1: Transform)")
        session.run("""
        MATCH (a)-[r:BUILDS]->(b)
        CREATE (a)-[r2:TRANSFORMS_TO]->(b)
        SET r2 = properties(r),
            r2.scor_id = 'sT',
            r2.process_level = 1,
            r2.lastUpdated = $now,
            r2.source = 'T-09-Ontology-Alignment'
        WITH r
        DELETE r
        """, now=now)

        # 3. PLANS_FOR -> FULFILLS_TO
        print("- Refactoring PLANS_FOR to FULFILLS_TO (Level 1: Fulfill)")
        session.run("""
        MATCH (a)-[r:PLANS_FOR]->(b)
        CREATE (a)-[r2:FULFILLS_TO]->(b)
        SET r2 = properties(r),
            r2.scor_id = 'sF',
            r2.process_level = 1,
            r2.lastUpdated = $now,
            r2.source = 'T-09-Ontology-Alignment'
        WITH r
        DELETE r
        """, now=now)

    driver.close()
    print("SCOR DS Ontology Alignment Complete.")

if __name__ == "__main__":
    align_scor_ontology()
