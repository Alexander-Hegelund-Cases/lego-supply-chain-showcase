import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def apply_risk_scoring():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Applying Risk Scores to Suppliers...")
        
        # High Risk for Volatile Materials
        session.run("""
        MATCH (s:Supplier) WHERE s.category CONTAINS 'Petrochemicals' 
           OR s.category CONTAINS 'Polymers' 
           OR s.category CONTAINS 'Chemicals'
        SET s.risk_score = 0.85,
            s.risk_factor = 'Market Volatility',
            s.lastUpdated = $now
        """, now=now)

        # High Risk for China/Mexico (Simulated Logistics/Geopolitical risk)
        session.run("""
        MATCH (s:Supplier) WHERE s.location IN ['China', 'Mexico'] AND s.risk_score IS NULL
        SET s.risk_score = 0.65,
            s.risk_factor = 'Logistics Complexity',
            s.lastUpdated = $now
        """, now=now)

        # Low Risk for others
        session.run("""
        MATCH (s:Supplier) WHERE s.risk_score IS NULL
        SET s.risk_score = 0.15,
            s.risk_factor = 'Stable Region',
            s.lastUpdated = $now
        """, now=now)

    driver.close()
    print("Risk scoring complete.")

if __name__ == "__main__":
    apply_risk_scoring()
