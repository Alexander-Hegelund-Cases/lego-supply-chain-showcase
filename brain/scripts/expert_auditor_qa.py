import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv(".env.local")

NEO4J_URI = os.getenv("NEO4J_INSTANCE_CONNECTION_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

class ExpertAuditor:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def run_query(self, title, cypher, description):
        print(f"\n--- [QA] {title} ---")
        print(f"Goal: {description}")
        with self.driver.session() as session:
            result = session.run(cypher)
            records = list(result)
            if not records:
                print("Status: [FAIL] No records found.")
            else:
                print("Status: [PASS] Sample Records Found:")
                for i, record in enumerate(records[:3]):
                    print(f"  {i+1}. {dict(record)}")
                if len(records) > 3:
                    print(f"  ... (+ {len(records)-3} more)")
        print("-" * 40)

    def audit_metadata(self):
        print("\n--- [QA] FAIR Governance & Metadata Audit ---")
        print("Goal: Confirm 100% adherence to FAIR metadata standards (is_synthetic, dataSource, lastUpdated).")
        cypher = """
        MATCH (n)
        WHERE n.is_synthetic IS NULL OR n.dataSource IS NULL OR n.lastUpdated IS NULL
        RETURN labels(n) as NodeLabel, count(*) as MissingCount
        """
        with self.driver.session() as session:
            result = session.run(cypher)
            records = list(result)
            if not records:
                print("Status: [PASS] 100% Metadata Coverage Verified.")
            else:
                print("Status: [FAIL] Missing Metadata Found:")
                for record in records:
                    print(f"  - Label: {record['NodeLabel']}, Missing: {record['MissingCount']}")
        print("-" * 40)

    def audit_scor_alignment(self):
        print("\n--- [QA] SCOR DS v14.0 Alignment Audit ---")
        print("Goal: Confirm core L1 relationships (SOURCES_TO, TRANSFORMS_TO, FULFILLS_TO).")
        cypher = """
        MATCH ()-[r]->()
        WHERE type(r) IN ['SOURCES_TO', 'TRANSFORMS_TO', 'FULFILLS_TO']
        RETURN type(r) as RelType, count(*) as RelCount
        """
        with self.driver.session() as session:
            result = session.run(cypher)
            records = list(result)
            if len(records) >= 3:
                print("Status: [PASS] All core L1 SCOR DS relationship types present.")
            else:
                print(f"Status: [FAIL] Only {len(records)} out of 3 core L1 types found.")
            for record in records:
                print(f"  - {record['RelType']}: {record['RelCount']}")
        print("-" * 40)

def main():
    auditor = ExpertAuditor()

    # Category 1: Semantic Integrity & SCOR-DS
    auditor.audit_scor_alignment()
    auditor.run_query(
        "Source-Make-Deliver Flow",
        """
        MATCH (s:Supplier)-[:SOURCES_TO]->(f:Factory)-[:TRANSFORMS_TO]->(st:Set)-[:IN_THEME]->(t:Theme)
        RETURN s.name as Supplier, f.name as Factory, t.name as Theme, count(st) as SetCount
        LIMIT 5
        """,
        "Verify the L1 SCOR DS flow from Supplier to Theme."
    )

    # Category 2: Multi-Tier Risk
    auditor.run_query(
        "Tier-2 Risk to Portfolio",
        """
        MATCH (s2:Supplier {tier: 2})-[r1:SOURCES_TO]->(s1:Supplier)-[r2:SOURCES_TO]->(f:Factory)-[r3:TRANSFORMS_TO]->(st:Set)-[:IN_THEME]->(t:Theme)
        RETURN s2.name as Tier2, s2.esg_risk_score as Risk, t.name as Theme, count(st) as SetsImpacted
        ORDER BY Risk DESC LIMIT 5
        """,
        "Identify Themes exposed to high Tier-2 risk."
    )

    # Category 3: Sustainability DtT
    auditor.run_query(
        "Material-Theme DtT Correlation",
        """
        MATCH (t:Theme)-[:DEPENDS_ON_MATERIAL]->(m:Material)
        RETURN t.name as Theme, t.distance_to_2032_target as Theme_DtT, m.name as Material, m.distance_to_2032_target as Material_DtT
        ORDER BY Theme_DtT DESC LIMIT 5
        """,
        "Verify that a Theme's DtT is driven by its component materials."
    )

    # Category 4: FAIR Governance
    auditor.audit_metadata()

    # Category 5: Ops/Logistics
    auditor.run_query(
        "Regional Delay Propagation",
        """
        MATCH (f:Factory)-[:FULFILLS_TO]->(r:Region)
        WHERE f.total_lead_time_days IS NOT NULL
        RETURN f.name as Factory, f.total_lead_time_days as Factory_LT, r.name as Region
        ORDER BY Factory_LT DESC LIMIT 5
        """,
        "Trace factory lead times through to fulfillment regions."
    )

    # Category 6: Marketing & PR (Negative ESG Exposure)
    auditor.run_query(
        "Marketing ESG Exposure",
        """
        MATCH (s:Supplier)
        WHERE s.esg_score CONTAINS 'Bronze' OR s.esg_score CONTAINS 'ISO'
        MATCH (s)-[:SOURCES_TO*1..2]->(f:Factory)-[:TRANSFORMS_TO]->(st:Set)-[:IN_THEME]->(t:Theme)
        RETURN t.name as Theme, count(DISTINCT s) as HighRiskSuppliers
        ORDER BY HighRiskSuppliers DESC LIMIT 5
        """,
        "Identify themes exposed to high-risk ESG suppliers for PR mitigation."
    )

    # Category 7: Finance (Risk vs Volume)
    auditor.run_query(
        "Finance Risk-to-Volume",
        """
        MATCH (reg:Region)-[fc:FORECASTS_DEMAND]->(st:Set)-[:IN_THEME]->(t:Theme)
        MATCH (st)<-[:TRANSFORMS_TO]-(fact:Factory)<-[:SOURCES_TO*1..2]-(s:Supplier)
        WHERE s.esg_score CONTAINS 'Bronze' OR s.esg_score CONTAINS 'ISO'
        RETURN t.name as Theme, sum(fc.volume) as ForecastVolume, count(DISTINCT s) as RiskSuppliers
        ORDER BY ForecastVolume DESC LIMIT 5
        """,
        "Analyze the financial volume at risk due to poor-performing tier-level suppliers."
    )

    auditor.close()

if __name__ == "__main__":
    main()
