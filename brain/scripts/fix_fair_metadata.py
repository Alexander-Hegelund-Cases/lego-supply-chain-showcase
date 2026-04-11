import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(".env.local")
driver = GraphDatabase.driver(os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687"), auth=(os.getenv("NEO4J_USERNAME", "neo4j"), os.getenv("NEO4J_PASSWORD", "password")))
now = datetime.now().isoformat()
with driver.session() as session:
    session.run("""
    MATCH (n)
    WHERE n:Supplier OR n:Factory OR n:Material OR n:CarbonCredit OR n:Region
    SET n.is_synthetic = coalesce(n.is_synthetic, true),
        n.dataSource = coalesce(n.dataSource, 'T-09-Synthetic-Data'),
        n.lastUpdated = coalesce(n.lastUpdated, $now)
    """, now=now)
driver.close()
print("Fixed missing FAIR metadata on remaining nodes.")
