import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def create_vulnerabilities():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Creating Scaled SPOF Vulnerabilities...")

        # 1. Force 10 random sets to be SPOF at Jiaxing Factory
        session.run("""
        MATCH (s:Set)
        WITH s, rand() AS r
        WHERE r < 0.05
        WITH s LIMIT 10
        MATCH (f:Factory {name: 'Jiaxing Factory'})
        OPTIONAL MATCH (f_other:Factory)-[r1:TRANSFORMS_TO]->(s)
        DELETE r1
        WITH s, f
        MERGE (f)-[r2:TRANSFORMS_TO]->(s)
        SET r2.is_synthetic = true,
            r2.source = 'Scenario_Simulation',
            r2.notes = 'Scaled SPOF Set',
            r2.lastUpdated = $now
        """, now=now)

        # 2. Force 5 random sets to be SPOF at Monterrey Factory
        session.run("""
        MATCH (s:Set)
        WITH s, rand() AS r
        WHERE r < 0.02
        WITH s LIMIT 5
        MATCH (f:Factory {name: 'Monterrey Factory'})
        OPTIONAL MATCH (f_other:Factory)-[r1:TRANSFORMS_TO]->(s)
        DELETE r1
        WITH s, f
        MERGE (f)-[r2:TRANSFORMS_TO]->(s)
        SET r2.is_synthetic = true,
            r2.source = 'Scenario_Simulation',
            r2.notes = 'Scaled SPOF Set',
            r2.lastUpdated = $now
        """, now=now)

        # 3. Create a critical factory (Vietnam Factory) with only one supplier
        session.run("""
        MATCH (f:Factory {name: 'Vietnam Factory'})
        MATCH (s:Supplier {name: 'Vietnam Petrochemical'})
        WITH f, s
        OPTIONAL MATCH (s_other:Supplier)-[r3:SOURCES_TO]->(f)
        DELETE r3
        WITH f, s
        MERGE (s)-[r4:SOURCES_TO]->(f)
        SET r4.is_synthetic = true,
            r4.source = 'Scenario_Simulation',
            r4.notes = 'Critical Supplier SPOF (Scaled)',
            r4.lastUpdated = $now
        """, now=now)

        # 4. Link some sets to Vietnam Factory to show propagation
        session.run("""
        MATCH (f:Factory {name: 'Vietnam Factory'})
        MATCH (s:Set)
        WITH f, s, rand() AS r
        WHERE r < 0.01
        WITH f, s LIMIT 3
        OPTIONAL MATCH (f_other:Factory)-[r1:TRANSFORMS_TO]->(s)
        DELETE r1
        WITH f, s
        MERGE (f)-[r2:TRANSFORMS_TO]->(s)
        SET r2.is_synthetic = true,
            r2.source = 'Scenario_Simulation',
            r2.notes = 'Chain of Failure (Scaled)',
            r2.lastUpdated = $now
        """, now=now)

    driver.close()
    print("Scaled vulnerabilities injected.")

if __name__ == "__main__":
    create_vulnerabilities()
