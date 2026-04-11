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

def deploy_native_dashboard():
    # Load Dashboard JSON
    dashboard_path = os.path.join(os.path.dirname(__file__), '..', 'dashboards', 'ekp_native_dashboard.json')
    if not os.path.exists(dashboard_path):
        print(f"Error: Dashboard file not found at {dashboard_path}")
        return

    with open(dashboard_path, 'r') as f:
        dashboard_content = f.read()
    
    config = json.loads(dashboard_content)
    title = config.get("title", "LEGO EKP Control Tower (Native)")
    version = config.get("version", "3.0")

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print(f"Deploying Native Dashboard '{title}' (v{version}) to {NEO4J_URI}...")
        
        # Native AuraDB Dashboards (Workspace) often look for specific metadata.
        # We push to labels that both NeoDash and Native Import detect.
        query = """
        MERGE (d:_Dashboard {title: $title})
        SET d.content = $content,
            d.version = $version,
            d.lastUpdated = $date,
            d.user = 'System Deploy'
        // Add NeoDash label too for multi-tool compatibility
        SET d:_NeoDash_Dashboard
        RETURN d.title AS title
        """
        
        result = session.run(query, 
                             title=title, 
                             content=dashboard_content, 
                             version=version, 
                             date=now)
        
        for record in result:
            print(f"Successfully saved and deployed Native Dashboard: '{record['title']}'")
            print("To view: Aura Console > Workspace > Dashboards > Import from Database")

    driver.close()

if __name__ == "__main__":
    deploy_native_dashboard()
