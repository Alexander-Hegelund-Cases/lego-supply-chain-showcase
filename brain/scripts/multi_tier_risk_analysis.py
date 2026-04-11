import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def apply_multi_tier_risk_propagation():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        print("Calculating Multi-Tier Risk Propagation...")

        # 1. Tier 2 Risk Inheritance to Tier 1
        # A Tier 1 supplier inherits the MAXIMUM risk of its Tier 2 dependencies
        print("- Propagating Risk from Tier 2 to Tier 1...")
        session.run("""
        MATCH (t2:Supplier {tier: 2})-[:SOURCES_TO]->(t1:Supplier)
        WITH t1, max(t2.risk_score) as t2_max_risk, count(t2) as dependency_degree
        // Only increase the Tier 1 risk if the Tier 2 risk is higher
        SET t1.inherited_t2_risk = t2_max_risk,
            t1.dependency_degree = dependency_degree,
            t1.risk_score = CASE WHEN t2_max_risk > t1.risk_score THEN t2_max_risk ELSE t1.risk_score END,
            t1.lastUpdated = $now
        """, now=now)

        # 2. Risk Propagation from Tier 1 to Factory
        # Factory risk is affected by its most risky supplier
        print("- Propagating Risk from Tier 1 to Factory...")
        session.run("""
        MATCH (s:Supplier)-[:SOURCES_TO]->(f:Factory)
        WITH f, max(s.risk_score) as max_supplier_risk
        SET f.supply_risk_score = max_supplier_risk,
            f.lastUpdated = $now
        """, now=now)

        # 3. Risk Propagation from Factory to Set
        # Set risk is the maximum risk of the factories that build it
        print("- Propagating Supply Risk to Sets...")
        session.run("""
        MATCH (f:Factory)-[:TRANSFORMS_TO]->(s:Set)
        WITH s, max(f.supply_risk_score) as max_factory_risk
        SET s.multi_tier_risk_score = max_factory_risk,
            s.lastUpdated = $now
        """, now=now)

        # 4. Update the 'Risk Factor' string if a T2 risk was inherited
        session.run("""
        MATCH (t2:Supplier {tier: 2})-[:SOURCES_TO]->(t1:Supplier)
        WHERE t1.inherited_t2_risk = t1.risk_score AND t2.risk_factor IS NOT NULL
        SET t1.risk_factor = 'Inherited T2: ' + t2.risk_factor,
            t1.lastUpdated = $now
        """, now=now)

    driver.close()
    print("Multi-Tier Risk Propagation Complete.")

if __name__ == "__main__":
    apply_multi_tier_risk_propagation()
