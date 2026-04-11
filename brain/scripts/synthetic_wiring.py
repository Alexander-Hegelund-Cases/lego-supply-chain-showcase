import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def wire_graph():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        # 0. Create Regions
        print("Creating Regions...")
        regions = ['Americas', 'EMEA', 'APAC']
        session.run("""
        UNWIND $regions AS r
        MERGE (reg:Region {name: r})
        SET reg.lastUpdated = $now
        """, regions=regions, now=now)

        print("Wiring Suppliers to Factories (Geographic + Global)...")
        # Regional Suppliers
        for region in ['Mexico', 'China', 'Denmark', 'Hungary', 'Sweden', 'Czech Republic', 'Japan', 'Taiwan', 'South Korea', 'Thailand', 'India']:
            session.run("""
            MATCH (s:Supplier {location: $region})
            MATCH (f:Factory) WHERE f.location = $region OR (f.location IN ['Denmark', 'Hungary', 'Czech Republic'] AND $region IN ['Denmark', 'Germany', 'Sweden', 'Finland', 'Netherlands', 'Austria', 'France', 'UK', 'Ireland'])
            MERGE (s)-[r:SOURCES_TO]->(f)
            SET r.is_synthetic = true,
                r.source = 'Scenario_Simulation',
                r.dataConfidence = 0.7,
                r.inbound_volume = 1000 + (rand() * 5000),
                r.is_collaborative = (rand() > 0.5),
                r.lastUpdated = $now
            """, region=region, now=now)

        # Global Suppliers (US, Saudi Arabia, Brazil) - Supply all major factories
        session.run("""
        MATCH (s:Supplier) WHERE s.location IN ['USA', 'Saudi Arabia', 'Brazil', 'Netherlands']
        MATCH (f:Factory) WHERE f.capacity = 'High'
        MERGE (s)-[r:SOURCES_TO]->(f)
        SET r.is_synthetic = true,
            r.source = 'Scenario_Simulation',
            r.dataConfidence = 0.8,
            r.inbound_volume = 10000 + (rand() * 20000),
            r.is_collaborative = true,
            r.lastUpdated = $now
        """, now=now)

        print("Wiring Factories to Sets (Distributed Production)...")
        # Most sets built by at least two factories
        session.run("""
        MATCH (s:Set)
        WITH s, rand() AS r
        MATCH (f:Factory)
        WHERE (r < 0.8 AND f.name IN ['Billund Factory', 'Monterrey Factory', 'Nyíregyháza Factory', 'Jiaxing Factory'])
        MERGE (f)-[rel:TRANSFORMS_TO]->(s)
        SET rel.is_synthetic = true,
            rel.source = 'Scenario_Simulation',
            rel.dataConfidence = 0.3,
            rel.production_capacity = 5000 + (rand() * 10000),
            rel.lead_time = 14 + (rand() * 21),
            rel.lastUpdated = $now
        """, now=now)

        # Ensure every set has at least one factory
        session.run("""
        MATCH (s:Set) WHERE NOT (:Factory)-[:TRANSFORMS_TO]->(s)
        WITH s, rand() AS r
        MATCH (f:Factory)
        WHERE (r < 0.25 AND f.name = 'Billund Factory') 
           OR (r >= 0.25 AND r < 0.5 AND f.name = 'Monterrey Factory')
           OR (r >= 0.5 AND r < 0.75 AND f.name = 'Nyíregyháza Factory')
           OR (r >= 0.75 AND f.name = 'Jiaxing Factory')
        MERGE (f)-[rel:TRANSFORMS_TO]->(s)
        SET rel.is_synthetic = true,
            rel.source = 'Scenario_Simulation',
            rel.dataConfidence = 0.3,
            rel.production_capacity = 5000 + (rand() * 10000),
            rel.lead_time = 14 + (rand() * 21),
            rel.lastUpdated = $now
        """, now=now)

        # 4. Wiring Regions to Sets (Demand Forecast)
        print("Wiring Regions to Sets (Demand Forecast)...")
        session.run("""
        MATCH (s:Set)
        MATCH (reg:Region)
        WITH s, reg, rand() AS r
        WHERE r < 0.4
        MERGE (reg)-[f:FORECASTS_DEMAND]->(s)
        SET f.volume = 1000 + (rand() * 10000),
            f.history = [1000 * rand(), 2000 * rand(), 3000 * rand()],
            f.is_synthetic = true,
            f.lastUpdated = $now
        """, now=now)

        # 5. Wiring Factories to Regions (PSI Planning)
        print("Wiring Factories to Regions (PSI Planning)...")
        # Mapping: Americas -> Monterrey, EMEA -> Billund/Nyíregyháza, APAC -> Jiaxing
        session.run("""
        MATCH (f:Factory {name: 'Monterrey Factory'})
        MATCH (reg:Region {name: 'Americas'})
        MERGE (f)-[p:PLANS_FOR]->(reg)
        SET p.inventory_level = 50000, p.safety_stock = 15000, p.is_synthetic = true, p.lastUpdated = $now
        """, now=now)

        session.run("""
        MATCH (f:Factory) WHERE f.name IN ['Billund Factory', 'Nyíregyháza Factory']
        MATCH (reg:Region {name: 'EMEA'})
        MERGE (f)-[p:PLANS_FOR]->(reg)
        SET p.inventory_level = 40000, p.safety_stock = 12000, p.is_synthetic = true, p.lastUpdated = $now
        """, now=now)

        session.run("""
        MATCH (f:Factory {name: 'Jiaxing Factory'})
        MATCH (reg:Region {name: 'APAC'})
        MERGE (f)-[p:PLANS_FOR]->(reg)
        SET p.inventory_level = 35000, p.safety_stock = 10000, p.is_synthetic = true, p.lastUpdated = $now
        """, now=now)

    driver.close()
    print("Synthetic wiring complete.")

if __name__ == "__main__":
    wire_graph()
