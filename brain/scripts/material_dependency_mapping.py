import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def material_dependency_mapping():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        # 1. Create Material Nodes
        print("Creating Material nodes...")
        materials = [
            {"name": "ABS", "carbon_intensity": 2.5, "unit": "kgCO2e/kg"},
            {"name": "Bio-PE", "carbon_intensity": 0.1, "unit": "kgCO2e/kg"},
            {"name": "Recycled Paper", "carbon_intensity": 0.05, "unit": "kgCO2e/kg"}
        ]
        session.run("""
        UNWIND $materials AS m
        MERGE (mat:Material {name: m.name})
        SET mat.carbon_intensity = m.carbon_intensity,
            mat.unit = m.unit,
            mat.lastUpdated = $now
        """, materials=materials, now=now)

        # 2. Map Suppliers to Materials (based on category)
        print("Mapping Suppliers to Materials...")
        session.run("""
        MATCH (s:Supplier) WHERE s.category CONTAINS 'ABS' OR s.category CONTAINS 'Polymer' OR s.category CONTAINS 'Styrenics'
        MATCH (m:Material {name: 'ABS'})
        MERGE (s)-[r:PRODUCES]->(m)
        SET r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        session.run("""
        MATCH (s:Supplier) WHERE s.category CONTAINS 'Bio-PE' OR s.category CONTAINS 'Bioplastics'
        MATCH (m:Material {name: 'Bio-PE'})
        MERGE (s)-[r:PRODUCES]->(m)
        SET r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        session.run("""
        MATCH (s:Supplier) WHERE s.category CONTAINS 'Packaging' OR s.category CONTAINS 'Eco-Packaging'
        MATCH (m:Material {name: 'Recycled Paper'})
        MERGE (s)-[r:PRODUCES]->(m)
        SET r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        # 3. Map Themes to Material Dependency (Strategic Scenarios)
        print("Mapping Themes to Material Dependency...")
        # Botanical Collection -> Bio-PE
        session.run("""
        MATCH (t:Theme {name: 'Botanicals'})
        MATCH (m:Material {name: 'Bio-PE'})
        MERGE (t)-[r:DEPENDS_ON_MATERIAL]->(m)
        SET r.ratio = 0.8, r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        # Technic -> ABS
        session.run("""
        MATCH (t:Theme {name: 'Technic'})
        MATCH (m:Material {name: 'ABS'})
        MERGE (t)-[r:DEPENDS_ON_MATERIAL]->(m)
        SET r.ratio = 0.9, r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        # Creator Expert -> Mixed
        session.run("""
        MATCH (t:Theme {name: 'Creator Expert'})
        MATCH (m:Material {name: 'ABS'})
        MERGE (t)-[r:DEPENDS_ON_MATERIAL]->(m)
        SET r.ratio = 0.7, r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        # 4. Addressing KV-002: Carbon Credits
        print("Creating Carbon Credits & Offsetting...")
        credits = [
            {"id": "CC-2026-DK-01", "supplier": "INEOS Styrolution", "amount": 500, "unit": "tCO2e", "year": 2026, "type": "Renewable Energy"},
            {"id": "CC-2026-BR-01", "supplier": "Braskem", "amount": 1200, "unit": "tCO2e", "year": 2026, "type": "Carbon Capture (Bio-feedstock)"},
            {"id": "CC-2026-IT-01", "supplier": "Novamont", "amount": 300, "unit": "tCO2e", "year": 2026, "type": "Soil Sequestration"}
        ]
        
        for cred in credits:
            session.run("""
            MERGE (c:CarbonCredit {id: $id})
            SET c.amount = $amount,
                c.unit = $unit,
                c.year = $year,
                c.type = $type,
                c.lastUpdated = $now
            WITH c
            MATCH (s:Supplier {name: $supplier})
            MERGE (s)-[r:GENERATES]->(c)
            SET r.lastUpdated = $now, r.is_synthetic = true
            """, id=cred['id'], amount=cred['amount'], unit=cred['unit'], 
                 year=cred['year'], type=cred['type'], supplier=cred['supplier'], now=now)

        # Offsetting Botanicals with Braskem & Novamont credits
        session.run("""
        MATCH (t:Theme {name: 'Botanicals'})
        MATCH (c:CarbonCredit) WHERE c.id IN ['CC-2026-BR-01', 'CC-2026-IT-01']
        MERGE (t)-[r:OFFSETS_WITH]->(c)
        SET r.offset_amount = 200, r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        # 5. Link Carbon Credits to Factories (Green Production Capacity)
        print("Linking Carbon Credits to Factories...")
        # Link credits to factories in the same region or strategically
        session.run("""
        MATCH (c:CarbonCredit) WHERE c.id = 'CC-2026-BR-01'
        MATCH (f:Factory {name: 'Monterrey Factory'})
        MERGE (f)-[r:ALLOCATED_OFFSET]->(c)
        SET r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

        session.run("""
        MATCH (c:CarbonCredit) WHERE c.id = 'CC-2026-DK-01'
        MATCH (f:Factory {name: 'Billund Factory'})
        MERGE (f)-[r:ALLOCATED_OFFSET]->(c)
        SET r.lastUpdated = $now, r.is_synthetic = true
        """, now=now)

    driver.close()
    print("Material mapping & carbon accounting complete.")

if __name__ == "__main__":
    material_dependency_mapping()
