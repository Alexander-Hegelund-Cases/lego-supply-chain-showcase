[�� Main README](../../README.md) ❯ 🧠 Brain ❯ 🧭 Planning ❯ 📍 Active Bet Map

# 🧭 The Active Bet Map: Now, Next, Later

> [!NOTE]
> **TL;DR**: The Cutler/Cagan Outcome-Based Roadmap assigning hypotheses, resources, and risk-gates to 9 distinct bets.

<details>
<summary><b>🗺️ Expand Table of Contents</b></summary>

- [🟡 NOW (0-90 Days): Functional Foundations](#now-0-90-days-functional-foundations)
  - [Bet 1: Stakeholder "Friction" Discovery](#bet-1-stakeholder-friction-discovery)
  - [Bet 2: The ERP/SAP Integration Pipeline](#bet-2-the-erpsap-integration-pipeline)
  - [Bet 3: Identity & RBAC Governance](#bet-3-identity-rbac-governance)
- [🟢 NEXT (Months 3-9): Cross-Functional Silo Busting](#next-months-3-9-cross-functional-silo-busting)
  - [Bet 4: S&OP to Marketing Alignment](#bet-4-sop-to-marketing-alignment)
  - [Bet 5: Finance "Dollar Risk" Engine](#bet-5-finance-dollar-risk-engine)
  - [Bet 6: Real-time EU Compliance (DPP)](#bet-6-real-time-eu-compliance-dpp)
- [🔵 LATER (Year 1+): The Agentic Moonshots](#later-year-1-the-agentic-moonshots)
  - [Bet 7: OmniGraph NLP Interface (Executive Chatbot)](#bet-7-omnigraph-nlp-interface-executive-chatbot)
  - [Bet 8: Agentic Self-Healing Procurement](#bet-8-agentic-self-healing-procurement)
  - [Bet 9: Viral Sentiment Procurement](#bet-9-viral-sentiment-procurement)
- [🎯 OKR Alignment Map](#okr-alignment-map)
  - [Objective Registry](#objective-registry)
  - [Bet → OKR Mapping View](#bet-okr-mapping-view)
  - [Coverage Validation](#coverage-validation)
- [👥 Team Trajectory: From Prototype to Platform](#team-trajectory-from-prototype-to-platform)
  - [Staffing Hypothesis](#staffing-hypothesis)
  - [Team Growth Summary](#team-growth-summary)
  - [Investment & Lean Waste Mitigation](#investment-lean-waste-mitigation)

</details>
This document formalizes the Enterprise Knowledge Platform (EKP) strategic roadmap based on [John Cutler's Outcome-Based "Bet" methodology](https://cutlefish.substack.com/p/tbm-2152-continuous-roadmapping) and [Marty Cagan's team objectives framework](https://www.svpg.com/team-objectives-empowerment/). Instead of rigid Feature Factories, each initiative is a **Bet** — a time-bounded, testable hypothesis designed to move a specific OKR.

Crucially, every Bet is protected by a **Gated Decision (If-This-Then-That)** to mitigate the "4 Big Product Risks" proactively.

> [!TIP]
> **How to read this document**: Each bet follows the **Sense → Hypothesis → Respond → Impact → OKR Link → Gate** structure. The [OKR Alignment Map](#-okr-alignment-map) at the bottom shows the full many-to-many wiring between bets and key results. For the team and budget required per phase, see the [Team Trajectory](#-team-trajectory-from-prototype-to-platform) section.

---

## 🟡 NOW (0-90 Days): Functional Foundations
*We cannot build moonshots on disconnected plumbing.*

### Bet 1: Stakeholder "Friction" Discovery
* **Stage:** 🔲 Up Next
* **Sense (The Catalyst):** S&OP and Finance spend 3 weeks resolving mismatched CSVs.
* **Hypothesis:** *If* we map exactly where cross-departmental reconciliation fails, *then* TTCFI drops from 3 days to <1 day for the top-5 query patterns identified.
* **Respond (The Task):** Conduct 30 discovery interviews spanning 3 silos.
* **Impact (The Result):** Target "Time-to-Value" reduced from weeks to seconds.
* 🎯 **OKR Link:** O2 (KR2: What-If scenarios), O3 (KR3: Cross-functional adoption) — *Discovery determines which scenarios matter and which departments to onboard first.*
* 🚫 **Gated Risk Decision (ITTT):** *If* Operations planners indicate they have zero bandwidth to adopt a new UI, *then* we pivot from building a frontend App to building "headless" pushed-email reports to bypass adoption friction entirely (Usability Risk).
* ⏱️ **Timebox:** 6 weeks · **Confidence:** High

### Bet 2: The ERP/SAP Integration Pipeline
* **Stage:** 🔲 Up Next
* **Sense:** Graph models decay instantly if untethered from operational truth.
* **Hypothesis:** *If* we integrate nightly batch ETLs from SAP Ariba and JDA, *then* graph freshness reaches >95% FAIR(EST)-Gold metadata compliance within 90 days.
* **Respond:** Integrate strictly governed semantic pipelines mapping JDA tables natively to Neo4j.
* **Impact:** 100% Graph Freshness confidence.
* 🎯 **OKR Link:** O1 (KR1: 95% FAIR(EST)-Gold metadata) — *Primary vehicle for data trust.*
* 🚫 **Gated Risk Decision:** *If* legacy SAP APIs heavily rate-limit our ETL ingestion causing >48-hour graph latency, *then* we will implement Delta-Lake CDC (Change Data Capture) caching to buffer the graph (Feasibility Risk).
* ⏱️ **Timebox:** 12 weeks · **Confidence:** Medium

### Bet 3: Identity & RBAC Governance
* **Stage:** 🔲 Up Next
* **Sense:** Enterprise data is highly sensitive and proprietary.
* **Hypothesis:** *If* we implement node/property-level RBAC, *then* Finance and Legal grant data access approval within 30 days — unblocking cross-functional adoption.
* **Respond:** Establish Role-Based Access Control (RBAC) at the Neo4j Node/Property level.
* **Impact:** Secure executive buy-in and infosec compliance.
* 🎯 **OKR Link:** O1 (KR1: FAIR(EST)-Gold), O3 (KR3: Adoption) — *No adoption without trust; no trust without access governance.*
* 🚫 **Gated Risk Decision:** *If* property-level RBAC degrades Cypher query speeds below 300ms, *then* we will segment Finance data into a completely separate "Neo4j Fabric" federated database to parallelize load (Business Viability Risk).
* ⏱️ **Timebox:** 8 weeks · **Confidence:** Medium

---

## 🟢 NEXT (Months 3-9): Cross-Functional Silo Busting
*Generating high-value $ wins using the established foundational plumbing.*

### Bet 4: S&OP to Marketing Alignment
* **Stage:** 💡 Ideas
* **Sense:** Marketing currently pushes campaigns for LEGO Sets that Logistics physically cannot deliver.
* **Hypothesis:** *If* Marketing can see tier-2 bottlenecks via automated alerts, *then* campaign-linked stockout incidents drop from ~100% undetected to <10%.
* **Respond:** Write a Graph algorithm that alerts Marketing teams if a promoted SKU has a >60% probability of Tier-2 stockout.
* **Impact:** Elimination of "Stock-out during Campaign" brand damage.
* 🎯 **OKR Link:** O2 (KR2: What-If scenarios), O4 (KR4: Stockout detection) — *Core vehicle for cross-departmental blind spot elimination.*
* 🚫 **Gated Risk Decision:** *If* Marketing teams ignore the Graph alerts to hit their own siloed KPIs, *then* we escalate the automation to forcibly disable the campaign's budget approval workflows until Logistics clears the flag (Value Risk).
* ⏱️ **Timebox:** 10 weeks · **Confidence:** Medium

### Bet 5: Finance "Dollar Risk" Engine
* **Stage:** 💡 Ideas
* **Sense:** Qualitative risk maps obscure real financial bleed.
* **Hypothesis:** *If* we map set margins directly downstream from vulnerable production nodes, *then* the CFO gains exact $-denominated Value-At-Risk per supplier disruption — reducing financial uncertainty by >50%.
* **Respond:** Map strict Set margins directly downstream from vulnerable Asian production nodes.
* **Impact:** Exact $ Value-At-Risk forecasting for the CFO.
* 🎯 **OKR Link:** O3 (KR3: Adoption — Finance department), O4 (KR4: Blind spot elimination) — *Pulls Finance into the platform via quantified risk.*
* 🚫 **Gated Risk Decision:** *If* regional currency fluctuations skew the margin models, *then* we baseline all queries in standardized EUR aggregates via an external Forex API microservice (Value Risk).
* ⏱️ **Timebox:** 12 weeks · **Confidence:** Low

### Bet 6: Real-time EU Compliance (DPP)
* **Stage:** 💡 Ideas
* **Sense:** The EU is mandating aggressive "Digital Product Passports" (DPP) for material goods.
* **Hypothesis:** *If* we leverage the graph to auto-generate lineage tokens (DPPs) for European sets, *then* 100% of EU-bound sets achieve regulatory compliance before the enforcement deadline.
* **Respond:** Leverage the graph to auto-generate holistic lineage tokens (DPPs) for every European set.
* **Impact:** Regulatory compliance secured, dodging massive regional fines.
* 🎯 **OKR Link:** O5 (KR5: 100% DPP coverage) — *Sole vehicle for EU regulatory readiness.*
* 🚫 **Gated Risk Decision:** *If* Tier-3 suppliers refuse to submit the required chain-of-custody data, *then* we alter the Graph to visually red-flag non-compliant materials so Procurement can execute supplier penalties (Business Viability Risk).
* ⏱️ **Timebox:** 16 weeks · **Confidence:** Low

---

## 🔵 LATER (Year 1+): The Agentic Moonshots
*Leveraging mature data to execute autonomous business operations.*

### Bet 7: OmniGraph NLP Interface (Executive Chatbot)
* **Stage:** 💡 Ideas
* **Sense:** C-Suite executives absolutely refuse to learn Cypher.
* **Hypothesis:** *If* we deploy a RAG-enabled NLP interface, *then* 80% of C-suite queries are resolved without Cypher knowledge — driving self-serve adoption from ~0 to 50+ executive users.
* **Respond:** Deploy a RAG-enabled "Control Tower" GenAI interface.
* **Impact:** 10x Self-Serve adoption by the Executive Board.
* 🎯 **OKR Link:** O6 (KR6: 80% self-serve resolution) — *Primary vehicle for executive self-service.*
* 🚫 **Gated Risk Decision:** *If* the LLM hallucinates incorrect Cypher queries causing bad financial data, *then* we implement a "Human-in-the-Loop" Cypher approval layer until the agent accuracy hits 99.9% (Feasibility Risk).
* ⏱️ **Timebox:** 20 weeks · **Confidence:** Low

### Bet 8: Agentic Self-Healing Procurement
* **Stage:** 💡 Ideas
* **Sense:** Humans take 7 days to process a severe shipping blockage and route around it.
* **Hypothesis:** *If* an agent monitors the graph and auto-drafts alternative POs on disruption, *then* mean-time-to-resolve drops from 7 days to <24 hours.
* **Respond:** An Agent constantly monitors the Graph; upon detecting a localized bottleneck, it automatically drafts a real Purchase Order routing to an alternate Supplier.
* **Impact:** "Zero-Delay" Supply Chain resilience.
* 🎯 **OKR Link:** O7 (KR7: MTTR <24h) — *Core vehicle for autonomous resilience.*
* 🚫 **Gated Risk Decision:** *If* the Agent aggressively over-orders resulting in bloated inventory costs, *then* we hard-cap the Agent's authorization to a $50k PO limit, passing larger re-routes to a human VP (Business Viability Risk).
* ⏱️ **Timebox:** 24 weeks · **Confidence:** Very Low

### Bet 9: Viral Sentiment Procurement
* **Stage:** 💡 Ideas
* **Sense:** Trends (e.g. TikTok "Botanicals") spike demand non-linearly.
* **Hypothesis:** *If* we stream social signals into demand nodes, *then* procurement lead-time for trend-sensitive materials (Bio-PE) is reduced by >40% versus reactive ordering.
* **Respond:** Stream social signals to dynamically inflate Set Demand nodes in the graph.
* **Impact:** "Just-in-Time" procurement perfectly timed with market zeitgeist.
* 🎯 **OKR Link:** O7 (KR7: MTTR <24h) — *Proactive variant of resilience — sensing demand before disruption hits.*
* 🚫 **Gated Risk Decision:** *If* "bot traffic" artificially spikes the graph signals, *then* we cross-validate the social sentiment with actual B2B retailer cart-adds before ordering resin (Value Risk).
* ⏱️ **Timebox:** 16 weeks · **Confidence:** Very Low

---

## 🎯 OKR Alignment Map

Each bet is wired to specific Objectives and Key Results from the [EKP Product Strategy](STRATEGY.md). The relationship is deliberately **many-to-many** — per [Cutler's continuous roadmapping](https://cutlefish.substack.com/p/tbm-2152-continuous-roadmapping) and [Cagan's team objectives](https://www.svpg.com/team-objectives-empowerment/) methodology.

> [!NOTE]
> **Reading this table**: Every bet must name at least one OKR it intends to move — or it has no place on the roadmap. Every OKR must have at least one active bet — or it's a wish, not a strategy. See the [OKR-to-Bet-Map Playbook](../../brain/context/OKR_BET_MAP_PLAYBOOK.md) for the full methodology.

### Objective Registry

| ID | Objective | Key Result | Horizon | Strategic Alignment |
| :--- | :--- | :--- | :--- | :--- |
| **O1** | Achieve Enterprise-Scale Data Trust | KR1: 95% of Tier 1/2 nodes meet FAIR(EST)-Gold metadata standards | 🟡 NOW | FAIR(EST) Governance |
| **O2** | Empower Proactive Resilience | KR2: Support 10+ "What-If" macro-disruption scenarios | 🟡 NOW | COO Priority |
| **O3** | Drive Cross-Functional Adoption | KR3: Onboard 50+ users from 3+ departments | 🟡 NOW | Value Chain Bedrock |
| **O4** | Eliminate Cross-Departmental Blind Spots | KR4: Campaign-linked stockout incidents drop from ~100% undetected to <10% | 🟢 NEXT | Revenue Protection |
| **O5** | Achieve EU DPP Regulatory Readiness | KR5: 100% of EU-bound sets have a generated Digital Product Passport | 🟢 NEXT | Compliance |
| **O6** | Enable Self-Serve Executive Intelligence | KR6: 80% of C-suite queries resolved via NLP without Cypher knowledge | 🔵 LATER | Executive Adoption |
| **O7** | Autonomous Resilience | KR7: Mean time to resolve supply disruption <24h (from 7-day baseline) | 🔵 LATER | Operational Excellence |

### Bet → OKR Mapping View

| Bet | Horizon | Stage | Primary OKR(s) | KR(s) Targeted | Confidence | Timebox |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1.** Friction Discovery | 🟡 NOW | 🔲 Up Next | O2, O3 | KR2, KR3 | High | 6 wks |
| **2.** ERP Pipeline | 🟡 NOW | 🔲 Up Next | O1 | KR1 | Medium | 12 wks |
| **3.** RBAC Governance | 🟡 NOW | 🔲 Up Next | O1, O3 | KR1, KR3 | Medium | 8 wks |
| **4.** S&OP-Marketing Alerts | 🟢 NEXT | 💡 Ideas | O2, O4 | KR2, KR4 | Medium | 10 wks |
| **5.** Finance Dollar-Risk | 🟢 NEXT | 💡 Ideas | O3, O4 | KR3, KR4 | Low | 12 wks |
| **6.** EU DPP Compliance | 🟢 NEXT | 💡 Ideas | O5 | KR5 | Low | 16 wks |
| **7.** NLP Executive Chatbot | 🔵 LATER | 💡 Ideas | O6 | KR6 | Low | 20 wks |
| **8.** Agentic Procurement | 🔵 LATER | 💡 Ideas | O7 | KR7 | Very Low | 24 wks |
| **9.** Viral Sentiment | 🔵 LATER | 💡 Ideas | O7 | KR7 | Very Low | 16 wks |

### Coverage Validation

```text
O1 (Data Trust)         ← Bet 2, Bet 3                    ✅ Covered
O2 (Resilience)         ← Bet 1, Bet 4                    ✅ Covered
O3 (Adoption)           ← Bet 1, Bet 3, Bet 5             ✅ Covered
O4 (Blind Spots)        ← Bet 4, Bet 5                    ✅ Covered
O5 (DPP Compliance)     ← Bet 6                           ✅ Covered (single bet risk — monitor)
O6 (Self-Serve Intel)   ← Bet 7                           ✅ Covered (single bet risk — monitor)
O7 (Autonomous)         ← Bet 8, Bet 9                    ✅ Covered
```

> [!WARNING]
> **Single-bet OKRs** (O5, O6) carry concentration risk. If those bets fail discovery, the OKR has no fallback. This is acceptable for NEXT/LATER horizons where bets are intentionally fuzzy — but if these OKRs become active, candidate backup bets should be identified.

---

## 👥 Team Trajectory: From Prototype to Platform

This prototype was built by **one Product Manager and a fleet of LLM agents** — proof that a single strategist with AI leverage can deliver a enterprise-grade graph, 10 validated scenarios, and a complete strategic narrative in days. For details on how this collaboration works, see the **[AI Collaboration Manifesto (4D Framework)](../../brain/governance/AI_COLLABORATION_MANIFESTO.md)**.

But prototyping is not shipping. Executing the bets above into a live enterprise platform requires **real cross-functional teams** with live system access, organisational authority, and domain certifications that no AI agent can substitute for.

Below is the staffing hypothesis — organized by the same Now / Next / Later horizons — showing how the team must scale as the platform matures.

### Staffing Hypothesis

| Phase | Role | Why This Bet Needs a Human |
| :--- | :--- | :--- |
| **🟡 NOW** | **Data & Integration Engineer** *(SAP Ariba, JDA, Apache NiFi/Kafka)* | Bet 2 (ERP Pipeline) requires enterprise credentials, infra provisioning, and on-call ownership that cannot be prototyped by AI. |
| | **Platform & Security Engineer** *(Neo4j Fabric, LDAP/SSO, ISO 27001)* | Bet 3 (RBAC Governance) demands enterprise SSO integration, infosec audit trails, and property-level access control hardening. |
| | **UX Researcher** *(JTBD Interviews, Maze/Optimal Workshop)* | Bet 1 (Friction Discovery) requires 30+ stakeholder interviews and synthesis — human rapport drives honest feedback. |
| **🟢 NEXT** | **Product Analyst** *(Amplitude/Mixpanel, A/B Testing, SQL)* | Bet 4 (S&OP-Marketing Alignment) needs continuous metric instrumentation and threshold tuning on the alert system. |
| | **Sustainability & ESG Domain Expert** *(ISCC PLUS, EU CSRD/DPP, GRI Standards)* | Bet 6 (EU Compliance) requires regulatory interpretation and chain-of-custody validation that carry legal liability. |
| | **Frontend & Visualization Engineer** *(React/D3.js, NeoDash, Grafana)* | Bet 5 (Finance Dollar-Risk Engine) needs scalable BI dashboards that go beyond notebook prototypes. |
| **🔵 LATER** | **ML / AI Engineer** *(LangChain, RAG Pipelines, MLOps/Kubeflow)* | Bet 7 (NLP Chatbot) and Bet 8 (Agentic Procurement) require fine-tuned models, guardrails, and live inference pipelines. |
| | **Data Scientist** *(NLP/Sentiment Analysis, Time-Series, PyTorch)* | Bet 9 (Viral Sentiment) demands real-time social signal processing and statistical validation to filter bot traffic. |
| | **DevOps / SRE** *(Kubernetes, Terraform, PagerDuty, Circuit Breakers)* | Bets 7-9 (Agentic Systems) require live system monitoring, automated incident response, and spend governance. |

### Team Growth Summary

```text
👤 TODAY:  1 PM + LLM Agents        (This Prototype)
│
├── 🟡 NOW:   +3 FTE  →  ~4 Total   (Foundation & Governance)
├── 🟢 NEXT:  +3 FTE  →  ~7 Total   (Cross-Functional Value)
└── 🔵 LATER: +3 FTE  →  ~10 Total  (Agentic Autonomy)
```

> **🚫 Gated Hiring Decision**: *If* the NOW bets validate that the EKP delivers measurable cross-functional value (reduced TTCFI, confirmed stakeholder adoption), *then* each subsequent phase's hiring is justified by demonstrated ROI — not speculative headcount. We staff the next horizon only when the current one proves its thesis.

### Investment & Lean Waste Mitigation

Scaling teams without budgeting for technical investments is a recipe for underperformance. Below are **rough directional estimates** for each horizon, paired with the primary [Lean waste risk](https://www.christianstrunk.com/blog/lean-methodology-guide) and its mitigation gate.

> [!NOTE]
> These figures are illustrative estimates based on Nordic enterprise benchmarks (FTE cost, SaaS licensing, cloud compute). To make them concrete, I would run a **Value Stream Map** in Sprint 1 — measuring actual time-to-value for each bet's critical path and calibrating budgets against observed cycle times. See: [10 Sources of Waste in Product Management](https://www.productcompass.pm/p/10-sources-of-waste-in-product-management).

| Phase | Key Technical Investments | Est. Budget (Quarterly) | Primary Waste Risk ([Toyota → Product](https://www.christianstrunk.com/blog/lean-methodology-guide)) | Mitigation Gate |
| :--- | :--- | :--- | :--- | :--- |
| **🟡 NOW** | Neo4j Aura Enterprise license, SAP API sandbox access, LDAP/SSO integration, UX research tooling (Maze) | ~€50-80k *(3 FTE + infra)* | **Overproduction** — Building SAP connectors for data nobody queries | Validate top-5 query patterns via stakeholder interviews (Bet 1) *before* engineering the pipeline (Bet 2). |
| **🟢 NEXT** | Analytics platform (Amplitude/Mixpanel), BI tooling (Grafana/NeoDash Pro), EU DPP regulatory counsel | ~€120-180k *(3 FTE + tooling + compliance)* | **Over-processing** — Gold-plating dashboards before validating alert thresholds | Ship "ugly but functional" alerts for 2 sprints. Measure adoption. *Then* invest in BI polish. |
| **🔵 LATER** | MLOps infrastructure (Kubeflow/Vertex AI), LLM fine-tuning compute, streaming pipeline (Kafka), SRE stack | ~€200-300k *(3 FTE + GPU/compute + monitoring)* | **Inventory** — Training ML models that never ship to users | Every ML experiment requires a pre-registered hypothesis and explicit kill criteria before compute is allocated. |

#### Lean Waste Scorecard

How Toyota's original 7 wastes translate into EKP product risks — and how our bet structure mitigates each:

```text
Toyota Waste          → EKP Product Equivalent           → Mitigation
──────────────────────────────────────────────────────────────────────
Overproduction        → Feature bloat / unused queries    → Pull-based discovery (Bet 1 gates Bet 2)
Waiting               → Handoff delays across silos       → Co-located cross-functional squads (NOW hires)
Over-processing       → Gold-plating dashboards           → "Ugly but works" MVP sprints before polish
Inventory             → Unshipped ML models               → Pre-registered experiments with kill criteria
Defects               → Rework from wrong requirements    → Build-Measure-Learn per Bet's gated decision
Motion                → Context-switching across projects  → Single-threaded horizon execution (one phase at a time)
Unused Talent         → Senior engineers doing admin       → Dedicated Platform Engineer (NOW hire)
```

---
<div align="center">
  <b><a href="../../README.md">🔙 Return to Main README</a></b>
</div>
