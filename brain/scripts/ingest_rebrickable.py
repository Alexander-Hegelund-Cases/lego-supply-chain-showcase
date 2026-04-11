import os
import pandas as pd
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def ingest_data():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    # Load CSVs
    themes_df = pd.read_csv("data/raw/themes.csv")
    sets_df = pd.read_csv("data/raw/sets.csv")

    print(f"Preparing to ingest {len(themes_df)} themes and {len(sets_df)} sets...")
    now = datetime.now().isoformat()

    with driver.session() as session:
        # 1. Create Constraints
        session.run("CREATE CONSTRAINT theme_id_unique IF NOT EXISTS FOR (t:Theme) REQUIRE t.id IS UNIQUE")
        session.run("CREATE CONSTRAINT set_num_unique IF NOT EXISTS FOR (s:Set) REQUIRE s.set_num IS UNIQUE")

        # 2. Batch Ingest Themes
        print("Ingesting Themes...")
        themes_data = themes_df.to_dict('records')
        session.run("""
        UNWIND $data AS row
        MERGE (t:Theme {id: toInteger(row.id)})
        SET t.name = row.name,
            t.parent_id = toInteger(row.parent_id),
            t.source = 'Rebrickable',
            t.dataSource = 'Rebrickable',
            t.dataConfidence = 1.0,
            t.lastUpdated = $now,
            t.is_synthetic = false
        """, data=themes_data, now=now)

        # 3. Batch Ingest Sets (Chunked for memory safety)
        print("Ingesting Sets...")
        sets_data = sets_df.to_dict('records')
        batch_size = 5000
        for i in range(0, len(sets_data), batch_size):
            batch = sets_data[i:i + batch_size]
            session.run("""
            UNWIND $data AS row
            MERGE (s:Set {set_num: row.set_num})
            SET s.name = row.name,
                s.year = toInteger(row.year),
                s.num_parts = toInteger(row.num_parts),
                s.source = 'Rebrickable',
                s.dataSource = 'Rebrickable',
                s.dataConfidence = 1.0,
                s.lastUpdated = $now,
                s.is_synthetic = false
            WITH s, row
            MATCH (t:Theme {id: toInteger(row.theme_id)})
            MERGE (s)-[r:IN_THEME]->(t)
            SET r.source = 'Rebrickable',
                r.dataSource = 'Rebrickable',
                r.dataConfidence = 1.0,
                r.lastUpdated = $now,
                r.is_synthetic = false
            """, data=batch, now=now)
            print(f"  Processed {min(i + batch_size, len(sets_data))} / {len(sets_data)} sets")

    driver.close()
    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_data()
