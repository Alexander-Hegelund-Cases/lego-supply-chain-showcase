import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

factories = [
    {"name": "Billund Factory", "location": "Denmark", "capacity": "High"},
    {"name": "Nyíregyháza Factory", "location": "Hungary", "capacity": "High"},
    {"name": "Kladno Factory", "location": "Czech Republic", "capacity": "Medium"},
    {"name": "Monterrey Factory", "location": "Mexico", "capacity": "High"},
    {"name": "Jiaxing Factory", "location": "China", "capacity": "High"},
    {"name": "Vietnam Factory", "location": "Vietnam", "capacity": "Planned"}
]

def bootstrap_factories():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    with driver.session() as session:
        # Create Constraint
        session.run("CREATE CONSTRAINT factory_name_unique IF NOT EXISTS FOR (f:Factory) REQUIRE f.name IS UNIQUE")

        for f in factories:
            session.run("""
            MERGE (fac:Factory {name: $name})
            SET fac.location = $location,
                fac.capacity = $capacity,
                fac.source = 'LEGO_Official_Locations',
                fac.dataConfidence = 1.0,
                fac.lastUpdated = $now,
                fac.is_synthetic = false
            """, name=f['name'], location=f['location'], capacity=f['capacity'], now=datetime.now().isoformat())
    
    driver.close()
    print(f"Bootstrapped {len(factories)} factories.")

if __name__ == "__main__":
    bootstrap_factories()
