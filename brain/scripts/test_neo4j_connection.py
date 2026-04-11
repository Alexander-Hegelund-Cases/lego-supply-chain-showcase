import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(".env.local")

# Use variables from .env.local
NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def test_connection():
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            result = session.run("RETURN 'Connection Successful!' AS message")
            message = result.single()["message"]
            print(f"Neo4j: {message}")
        driver.close()
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}")

if __name__ == "__main__":
    test_connection()
