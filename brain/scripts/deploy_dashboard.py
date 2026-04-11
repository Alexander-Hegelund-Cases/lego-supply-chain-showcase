import os
import json
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def deploy_dashboard():
    # Load Dashboard JSON
    dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'dashboards', 'ekp_executive_dashboard.json')
    if not os.path.exists(dashboard_path):
        print(f"Error: Dashboard file not found at {dashboard_path}")
        return

    with open(dashboard_path, 'r') as f:
        dashboard_content = f.read()
    
    # We parse it just to extract title/version for metadata, but we upload the raw string content
    config = json.loads(dashboard_content)
    title = config.get("title", "LEGO EKP Control Tower")
    version = config.get("version", "2.4")

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print(f"Deploying '{title}' (v{version}) to {NEO4J_URI}...")
        
        # NeoDash uses _NeoDash_Dashboard nodes to store loadable dashboard configurations
        # We MERGE on the title so we update the existing one rather than endlessly spawning duplicates
        query = """
        MERGE (d:_NeoDash_Dashboard {title: $title})
        SET d.content = $content,
            d.version = $version,
            d.date = $date,
            d.user = 'System Deploy'
        RETURN d.title AS title
        """
        
        result = session.run(query, 
                             title=title, 
                             content=dashboard_content, 
                             version=version, 
                             date=now)
        
        for record in result:
            print(f"Successfully saved and deployed Dashboard: '{record['title']}'")
            print("Note: To view in NeoDash, connect to DB and select 'Load from Database'.")

    driver.close()

if __name__ == "__main__":
    deploy_dashboard()
