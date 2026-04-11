import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def check_aura():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        # Check Node Counts
        result = session.run("MATCH (n) RETURN labels(n) as labels, count(*) as count")
        print("\n--- Neo4j Aura Status Report ---")
        total_nodes = 0
        nodes_found = False
        for record in result:
            labels = record["labels"]
            count = record["count"]
            total_nodes += count
            print(f"- {labels}: {count}")
            nodes_found = True
        
        if not nodes_found:
            print("No nodes found in the database.")
        else:
            print(f"\nTotal Nodes in Aura: {total_nodes}")
        
        # Check Relationship Types
        rel_result = session.run("MATCH ()-[r]->() RETURN type(r) as type, count(*) as count")
        print("\n--- Relationship Types in Aura ---")
        rels_found = False
        for record in rel_result:
            print(f"- {record['type']}: {record['count']}")
            rels_found = True
            
        if not rels_found:
            print("No relationships found in the database.")
            
    driver.close()

if __name__ == "__main__":
    check_aura()
