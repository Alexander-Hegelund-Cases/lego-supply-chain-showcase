import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

suppliers = [
    {"name": "A.M. RAMP & CO GMBH", "location": "Germany", "category": "General Supplier"},
    {"name": "All4Labels", "location": "Denmark", "category": "Labels/Packaging"},
    {"name": "AMB INDUSTRI AB", "location": "Sweden", "category": "General Supplier"},
    {"name": "AMERICAN POLY DEL NORTE S.A DE C.V.", "location": "Mexico", "category": "Polymer/Plastic"},
    {"name": "ARTIGRAF SA DE CV", "location": "Mexico", "category": "Printing/Graphics"},
    {"name": "Avient China Co., Ltd.", "location": "China", "category": "Colorants/Materials"},
    {"name": "Avient Colorants", "location": "Mexico", "category": "Colorants/Materials"},
    {"name": "Balyfa Hungary Kft.", "location": "Hungary", "category": "General Supplier"},
    {"name": "Basell Sales & Marketing B.V.", "location": "Sweden", "category": "Sales & Marketing"},
    {"name": "BORDING A/S", "location": "Denmark", "category": "General Supplier"},
    {"name": "Braskem BV International", "location": "Brazil", "category": "Petrochemicals/Plastics"},
    {"name": "BROADWAY PRECISION TECHNOLOGY", "location": "China", "category": "Precision Technology"},
    {"name": "C C Joint Printing Co.", "location": "China", "category": "Printing"},
    {"name": "CAJAS DE CARTON SULTANA S.A. DE C.V", "location": "Mexico", "category": "Cardboard Boxes/Packaging"},
    {"name": "CARTA MUNDI NORDIC AB", "location": "Sweden", "category": "Cards/Printing"},
    {"name": "Shin-Etsu Chemical Co., Ltd.", "location": "Japan", "category": "Specialty Chemicals"},
    {"name": "Sumitomo Chemical", "location": "Japan", "category": "Petrochemicals"},
    {"name": "Formosa Plastics Corp.", "location": "Taiwan", "category": "Polymers"},
    {"name": "Reliance Industries Ltd.", "location": "India", "category": "Petrochemicals"},
    {"name": "PTT Global Chemical", "location": "Thailand", "category": "Polymers"},
    {"name": "LG Chem", "location": "South Korea", "category": "Chemicals/Materials"},
    {"name": "SABIC", "location": "Saudi Arabia", "category": "Petrochemicals"},
    {"name": "LyondellBasell Industries", "location": "Netherlands", "category": "Polymers"},
    {"name": "Borealis AG", "location": "Austria", "category": "Polymers"},
    {"name": "Arkema S.A.", "location": "France", "category": "Specialty Chemicals"},
    {"name": "Covestro AG", "location": "Germany", "category": "Polymers"},
    {"name": "Stora Enso", "location": "Finland", "category": "Packaging"},
    {"name": "Mondi Group", "location": "UK", "category": "Packaging"},
    {"name": "Smurfit Kappa", "location": "Ireland", "category": "Packaging"},
    {"name": "International Paper", "location": "USA", "category": "Packaging"},
    {"name": "WestRock", "location": "USA", "category": "Packaging"},
    {"name": "Eastman Chemical Company", "location": "USA", "category": "Specialty Materials"},
    {"name": "DuPont de Nemours, Inc.", "location": "USA", "category": "Advanced Materials"},
    {"name": "Mitsui Chemicals", "location": "Japan", "category": "Petrochemicals"},
    {"name": "Lotte Chemical", "location": "South Korea", "category": "Polymers"},
    {"name": "Wanhua Chemical Group", "location": "China", "category": "Specialty Chemicals"},
    {"name": "Braskem Idesa", "location": "Mexico", "category": "Petrochemicals"},
    {"name": "Indorama Ventures", "location": "Thailand", "category": "Polymers"},
    {"name": "Alpek", "location": "Mexico", "category": "Petrochemicals"},
    {"name": "Vietnam Petrochemical", "location": "Vietnam", "category": "Polymers"}
]

def bootstrap_suppliers():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    with driver.session() as session:
        # Create Constraint
        session.run("CREATE CONSTRAINT supplier_name_unique IF NOT EXISTS FOR (s:Supplier) REQUIRE s.name IS UNIQUE")

        for s in suppliers:
            session.run("""
            MERGE (sup:Supplier {name: $name})
            SET sup.location = $location,
                sup.category = $category,
                sup.source = 'LEGO_2024_Supplier_PDF',
                sup.dataConfidence = 1.0,
                sup.lastUpdated = $now,
                sup.is_synthetic = false
            """, name=s['name'], location=s['location'], category=s['category'], now=datetime.now().isoformat())
    
    driver.close()
    print(f"Bootstrapped {len(suppliers)} suppliers.")

if __name__ == "__main__":
    bootstrap_suppliers()
