import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def verify_risk():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    with driver.session() as session:
        print("\n--- Scenario: Bio-PE Supply Chain Risk (Braskem Disruption) ---")
        
        query = """
        MATCH (mat:Material {name: 'Bio-PE'})<-[:PRODUCES]-(s:Supplier {name: 'Braskem'})
        OPTIONAL MATCH (mat)<-[:DEPENDS_ON_MATERIAL]-(t:Theme)
        OPTIONAL MATCH (s)-[:GENERATES]->(cc:CarbonCredit)<-[:OFFSETS_WITH]-(t)
        RETURN s.name AS Supplier, 
               mat.name AS Material, 
               t.name AS ImpactedTheme, 
               cc.id AS CarbonCreditID, 
               cc.amount AS CreditAmount
        """
        
        results = session.run(query)
        for record in results:
            print(f"Supplier: {record['Supplier']}")
            print(f"Material: {record['Material']}")
            print(f"Impacted Theme: {record['ImpactedTheme']}")
            print(f"Linked Carbon Credit: {record['CarbonCreditID']} ({record['CreditAmount']} {record.get('unit', 'tCO2e')})")
            print("-" * 30)

        print("\n--- Summary: KV-002 Granular Carbon Accounting ---")
        query_cc = """
        MATCH (t:Theme)-[r:OFFSETS_WITH]->(cc:CarbonCredit)<-[:GENERATES]-(s:Supplier)
        RETURN t.name AS Theme, sum(r.offset_amount) AS TotalOffset, collect(s.name) AS CreditProviders
        """
        results_cc = session.run(query_cc)
        for record in results_cc:
            print(f"Theme: {record['Theme']} | Total Offset: {record['TotalOffset']} tCO2e | Provided by: {record['CreditProviders']}")

    driver.close()

if __name__ == "__main__":
    verify_risk()
