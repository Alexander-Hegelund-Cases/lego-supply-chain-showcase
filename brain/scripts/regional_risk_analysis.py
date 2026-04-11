import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def regional_risk_clustering():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    with driver.session() as session:
        print("\n--- Phase 1: Regional Aggregation (Geographic Risk) ---")
        
        # Mapping qualitative scores for risk calculations
        # Platinum/High = Low Risk (0.2), Gold = Moderate (0.4), Silver = Elevated (0.6), Bronze/ISO = High (0.8)
        
        query_aggregate = """
        MATCH (s:Supplier)
        WITH s.location AS Location, 
             count(s) AS SupplierCount, 
             avg(CASE 
                 WHEN s.esg_score CONTAINS 'Platinum' THEN 0.2
                 WHEN s.esg_score CONTAINS 'CDP A' THEN 0.2
                 WHEN s.esg_score CONTAINS 'B Corp' THEN 0.2
                 WHEN s.esg_score CONTAINS 'High' THEN 0.4
                 WHEN s.esg_score CONTAINS 'Gold' THEN 0.4
                 WHEN s.esg_score CONTAINS 'Silver' THEN 0.6
                 WHEN s.esg_score CONTAINS 'Bronze' THEN 0.8
                 WHEN s.esg_score CONTAINS 'ISO' THEN 0.8
                 ELSE 0.5 END) AS RegionalRiskAvg
        RETURN Location, SupplierCount, RegionalRiskAvg
        ORDER BY RegionalRiskAvg DESC
        """
        
        results = session.run(query_aggregate)
        print(f"{'Location':<20} | {'Suppliers':<10} | {'Risk Index':<10}")
        print("-" * 45)
        for record in results:
            print(f"{record['Location']:<20} | {record['SupplierCount']:<10} | {record['RegionalRiskAvg']:<10.2f}")

        print("\n--- Phase 2: Macro-Disruption Impact (Taiwan Cluster) ---")
        # Taiwan is a critical hub for ABS (Chi Mei Corp)
        query_impact = """
        MATCH (s:Supplier {location: 'Taiwan'})-[:SOURCES_TO*1..3]->(f:Factory)-[:TRANSFORMS_TO]->(set:Set)
        WITH count(set) AS ImpactedSets, collect(DISTINCT f.name) AS ImpactedFactories
        RETURN ImpactedSets, ImpactedFactories
        """
        
        impact = session.run(query_impact).single()
        if impact:
            print(f"Disruption in Taiwan Impacts:")
            print(f"  - {impact['ImpactedSets']} unique Sets")
            print(f"  - Factories involved: {impact['ImpactedFactories']}")

        print("\n--- Phase 3: Regional Carbon Exposure ---")
        query_carbon = """
        MATCH (s:Supplier)-[:GENERATES]->(cc:CarbonCredit)
        RETURN s.location AS Location, sum(cc.amount) AS TotalCredits, count(cc) AS CreditProjects
        ORDER BY TotalCredits DESC
        """
        
        carbon_results = session.run(query_carbon)
        print(f"{'Location':<20} | {'Credits (tCO2e)':<15} | {'Projects':<10}")
        print("-" * 50)
        for record in carbon_results:
            print(f"{record['Location']:<20} | {record['TotalCredits']:<15.0f} | {record['CreditProjects']:<10}")

    driver.close()

if __name__ == "__main__":
    regional_risk_clustering()
