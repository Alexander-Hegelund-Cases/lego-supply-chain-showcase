import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(".env.local")
NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

def count_db_hits(profile_plan):
    hits = profile_plan.get('dbHits', 0) if isinstance(profile_plan, dict) else getattr(profile_plan, 'db_hits', 0)
    children = profile_plan.get('children', []) if isinstance(profile_plan, dict) else getattr(profile_plan, 'children', [])
    for child in children:
        hits += count_db_hits(child)
    return hits

def check_for_operator(profile_plan, operator_type):
    op = profile_plan.get('operatorType', '') if isinstance(profile_plan, dict) else getattr(profile_plan, 'operator_type', '')
    if operator_type in op:
        return True
    
    children = profile_plan.get('children', []) if isinstance(profile_plan, dict) else getattr(profile_plan, 'children', [])
    for child in children:
        if check_for_operator(child, operator_type):
            return True
    return False

def run_performance_audit():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    queries = [
        {
            "name": "Finance Risk-to-Volume",
            "query": """
            PROFILE
            MATCH (reg:Region)-[fc:FORECASTS_DEMAND]->(st:Set)-[:IN_THEME]->(t:Theme)
            MATCH (st)<-[:TRANSFORMS_TO]-(fact:Factory)<-[:SOURCES_TO*1..2]-(s:Supplier)
            WHERE s.esg_score CONTAINS 'Bronze' OR s.esg_score CONTAINS 'ISO'
            RETURN t.name as Theme, sum(fc.volume) as ForecastVolume, count(DISTINCT s) as RiskSuppliers
            ORDER BY ForecastVolume DESC LIMIT 5
            """,
            "expected_max_db_hits": 50000000 # High limit just for prototype, real tuning would lower this
        },
        {
            "name": "Basic Filter Check (Index Validation)",
            "query": """
            PROFILE
            MATCH (s:Supplier) WHERE s.name = 'BASF SE'
            RETURN s
            """,
            "expected_max_db_hits": 10
        }
    ]

    with driver.session() as session:
        print("Starting Neo4j Query Performance Audit...\n" + "-"*40)
        for q in queries:
            print(f"Testing: {q['name']}")
            result = session.run(q['query'])
            
            # Exhaust the result to get summary
            list(result)
            summary = result.consume()
            
            if not summary.profile:
                print("  [FAIL] PROFILE data missing from summary.")
                continue

            total_hits = count_db_hits(summary.profile)
            print(f"  Result dbHits: {total_hits}")
            
            if total_hits > q['expected_max_db_hits']:
                print(f"  [FAIL] dbHits ({total_hits}) exceeded expected maximum ({q['expected_max_db_hits']})")
            else:
                print(f"  [PASS] dbHits within acceptable limits.")

            # Look for index usage vs full scans
            if "Index Validation" in q['name']:
                if check_for_operator(summary.profile, "NodeIndexSeek"):
                    print("  [PASS] Index effectively utilized (NodeIndexSeek).")
                else:
                    print("  [WARN] Query did not use an Index. Full scan suspected.")
            
            # Check for Cartesian Products
            if check_for_operator(summary.profile, "CartesianProduct"):
                print("  [WARN] CartesianProduct detected in execution plan!")

            print("-" * 40)

    driver.close()

if __name__ == "__main__":
    run_performance_audit()
