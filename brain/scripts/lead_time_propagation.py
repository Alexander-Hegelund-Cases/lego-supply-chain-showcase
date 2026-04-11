import os
from neo4j import GraphDatabase
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def lead_time_propagation():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    now = datetime.now().isoformat()
    
    with driver.session() as session:
        # 1. Initialize Base Lead Times (in days)
        print("Initializing base lead times...")
        
        # Sourcing Lead Times
        # Regional: 7 days, Global: 21 days
        session.run("""
        MATCH (s:Supplier)-[r:SOURCES_TO]->(f:Factory)
        SET r.base_lead_time = CASE 
            WHEN s.location = f.location THEN 7 
            WHEN s.location IN ['USA', 'Saudi Arabia', 'Brazil', 'Taiwan'] THEN 21 
            ELSE 14 END,
            r.current_delay = 0,
            r.lastUpdated = $now
        """, now=now)

        # Production Lead Times (Transform)
        session.run("""
        MATCH (f:Factory)-[r:TRANSFORMS_TO]->(s:Set)
        SET r.base_lead_time = 3,
            r.current_delay = 0,
            r.lastUpdated = $now
        """, now=now)

        # Tier 2 -> Tier 1 Sourcing
        session.run("""
        MATCH (s2:Supplier {tier: 2})-[r:SOURCES_TO]->(s1:Supplier {tier: 1})
        SET r.base_lead_time = 14,
            r.current_delay = 0,
            r.lastUpdated = $now,
            s2.lead_time_days = 21,
            s1.lead_time_days = 14
        """, now=now)

        # 2. Simulate Macro-Disruption: "Taiwan Logistics Bottleneck"
        print("Simulating disruption: Taiwan Logistics Bottleneck (+15 days delay)...")
        session.run("""
        MATCH (s:Supplier {location: 'Taiwan'})-[r:SOURCES_TO]->()
        SET r.current_delay = 15,
            r.lastUpdated = $now
        """, now=now)

        # 3. Calculate Propagated Lead Time Impact
        print("\n--- Lead Time Propagation Report: Impact of Taiwan Disruption (Alpha=1.2) ---")
        # Formula: Propagated_Delay = Source_Delay * (1.2 ^ Tier)
        # Tier 2 -> Tier 1 (Tier 1) -> Factory (Tier 2) -> Set (Tier 3)
        query = """
        MATCH (s2:Supplier {location: 'Taiwan'})-[r1:SOURCES_TO]->(s1:Supplier)-[r2:SOURCES_TO]->(f:Factory)-[r3:TRANSFORMS_TO]->(set:Set)
        WITH set, f, r1, r2, r3,
             (r1.current_delay * 1.0) AS d1,
             (r1.current_delay * 1.2) AS d2,
             (r1.current_delay * 1.44) AS d3
        RETURN set.name AS SetName, 
               f.name AS Factory, 
               (r1.base_lead_time + d1) + (r2.base_lead_time + d2) + (r3.base_lead_time + d3) AS TotalLeadTime,
               d3 AS FinalDelay
        ORDER BY FinalDelay DESC
        LIMIT 10
        """
        results = session.run(query)
        header = f"{'Set Name':<40} | {'Factory':<20} | {'Total LT':<8} | {'Delay':<8}"
        print(header)
        print("-" * len(header))
        for record in results:
            print(f"{record['SetName'][:40]:<40} | {record['Factory']:<20} | {record['TotalLeadTime']:<8.1f} | {record['FinalDelay']:<8.1f}")

        # Summary for Marketing/PM
        print("\n--- Summary: Portfolio Risk (Ripple Effect) ---")
        summary_query = """
        MATCH (s:Supplier)-[r:SOURCES_TO*1..2]->(f:Factory)-[r2:TRANSFORMS_TO]->(set:Set)
        WHERE any(rel IN r WHERE rel.current_delay > 0)
        WITH set, r, r2,
             CASE WHEN size(r) = 2 THEN r[0].current_delay * 1.44 ELSE r[0].current_delay * 1.2 END AS CalculatedDelay
        RETURN count(DISTINCT set) AS DelayedSets, 
               max(CalculatedDelay) AS MaxDelay
        """
        # Note: Cypher path syntax r[0] is used for clarity in simple path scenarios
        summary = session.run(summary_query).single()
        if summary:
            print(f"Total Sets with Production Delays: {summary['DelayedSets']}")
            print(f"Maximum Predicted Delay (Days): {summary['MaxDelay']}")

        # 4. Save total lead time back to Factory for QA
        session.run("""
        MATCH (s:Supplier)-[r:SOURCES_TO]->(f:Factory)
        WITH f, max(r.base_lead_time + r.current_delay) AS max_inbound
        SET f.total_lead_time_days = max_inbound + 3,
            f.lastUpdated = $now
        """, now=now)

    driver.close()

if __name__ == "__main__":
    lead_time_propagation()
