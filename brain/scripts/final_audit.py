import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def final_audit():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        # Check for Distance to 2032 metrics
        dtt_result = session.run("MATCH (n) WHERE n.distance_to_2032_target IS NOT NULL RETURN count(*) as count")
        dtt_count = dtt_result.single()["count"]
        print(f"Nodes with 'distance_to_2032_target': {dtt_count}")
        
        # Check for SCOR DS relationships
        scor_result = session.run("MATCH ()-[r:SOURCES_TO]->() RETURN count(*) as count")
        scor_count = scor_result.single()["count"]
        print(f"SCOR DS 'SOURCES_TO' relationships: {scor_count}")
        
        # Check for ESG risk scores (foundation for DtT)
        esg_result = session.run("MATCH (n:Supplier) WHERE n.esg_risk_score IS NOT NULL RETURN count(*) as count")
        esg_count = esg_result.single()["count"]
        print(f"Suppliers with 'esg_risk_score': {esg_count}")
        
        # Check for Themes with DtT
        theme_result = session.run("MATCH (n:Theme) WHERE n.distance_to_2032_target IS NOT NULL RETURN count(*) as count")
        theme_count = theme_result.single()["count"]
        print(f"Themes with 'distance_to_2032_target': {theme_count}")

    driver.close()

if __name__ == "__main__":
    final_audit()
