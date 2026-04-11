import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(".env.local")
NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def bootstrap_indexes():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        print("Bootstrapping Constraints and Indexes for Performance Tuning...")
        
        queries = [
            "CREATE INDEX set_name_index IF NOT EXISTS FOR (s:Set) ON (s.name)",
            "CREATE INDEX theme_name_index IF NOT EXISTS FOR (t:Theme) ON (t.name)",
            "CREATE INDEX supplier_name_index IF NOT EXISTS FOR (s:Supplier) ON (s.name)",
            "CREATE INDEX factory_name_index IF NOT EXISTS FOR (f:Factory) ON (f.name)",
            "CREATE INDEX supplier_location_index IF NOT EXISTS FOR (s:Supplier) ON (s.location)",
            "CREATE INDEX factory_location_index IF NOT EXISTS FOR (f:Factory) ON (f.location)",
            "CREATE INDEX supplier_tier_index IF NOT EXISTS FOR (s:Supplier) ON (s.tier)"
        ]
        
        for q in queries:
            try:
                session.run(q)
                print(f"Executed: {q}")
            except Exception as e:
                print(f"Skipped/Error on {q}: {e}")

    driver.close()
    print("Optimization Initialization Complete.")

if __name__ == "__main__":
    bootstrap_indexes()
