---
title: "OKR-to-Bet-Map Mapping Playbook"
domain: "governance"
ontology_alignment: "Cutler Bet Maps, Cagan Team Objectives, OKR Framework"
confidence_score: 0.85
hardening_delta: 0.40
source_lineage:
  - type: "external"
    reference: "https://www.linkedin.com/pulse/mastering-okrs-product-management-lessons-from-marty-cagans-mene-xz5fc"
    notes: "Synthesized playbook combining Cagan SVPG and Cutler continuous roadmapping"
  - type: "external"
    reference: "https://www.svpg.com/team-objectives-empowerment/"
    notes: "Cagan's canonical framing of team objectives as problems-to-solve"
  - type: "external"
    reference: "https://cutlefish.substack.com/p/tbm-2152-continuous-roadmapping"
    notes: "Cutler's continuous roadmapping and 'beautiful mess' philosophy"
  - type: "external"
    reference: "https://www.youtube.com/watch?v=XUbpY9275No"
    notes: "Cutler talk on bet-based roadmapping"
  - type: "external"
    reference: "https://www.productplan.com/learn/prioritize-product-roadmap-with-okrs/"
    notes: "ProductPlan OKR-roadmap integration patterns"
  - type: "external"
    reference: "https://www.getjop.com/blog/okr-product-roadmap"
    notes: "JOP OKR-roadmap alignment templates"
  - type: "internal"
    reference: "brain/planning/STRATEGY.md"
    notes: "Existing FY2026 OKRs (O1-O3) that need wiring to the bet map"
  - type: "internal"
    reference: "brain/planning/ACTIVE_BET_MAP.md"
    notes: "9-bet Now/Next/Later map currently disconnected from OKRs"
relationship_mapping:
  parents: ["brain/planning/STRATEGY.md"]
  children: []
  peers: ["brain/planning/ACTIVE_BET_MAP.md", "brain/context/ROADMAP.md"]
rag_metadata:
  chunk_type: "concept"
  semantic_keys: ["OKR", "bet map", "outcome roadmap", "team objectives", "empowerment", "continuous roadmapping", "Cagan", "Cutler", "key results", "many-to-many mapping"]
last_validated: "2026-04-10"
success_impact:
  metrics: ["G-01"]
  notes: "Bridges the gap between STRATEGY.md OKRs and the ACTIVE_BET_MAP.md, turning the portfolio from a feature list into an outcome-driven system."
---

# Definition

The OKR-to-Bet-Map Mapping Playbook is a synthesis of Marty Cagan's (SVPG) team objectives framework and John Cutler's continuous roadmapping methodology. It defines how to wire Objectives & Key Results (OKRs) — which express desired business and user outcomes — to a Bet Map — which expresses the team's best current hypotheses for achieving those outcomes. The relationship is many-to-many: a single bet may influence multiple key results, and a single key result may depend on multiple bets.

## Scope and Boundaries

**Covers**: OKR design principles, bet map structure (Ideas → Up Next → In Progress → Live), mapping mechanics, cadence/governance rituals, failure modes (feature factories with OKR lipstick, over-engineered mapping, no real empowerment), and lightweight templates.

**Does not cover**: Implementation-level OKR tooling (Workboard, Lattice, etc.), company-wide OKR rollout change management, or HR performance management integration.

## Core Principles

### 1. Outcomes Over Outputs
OKRs describe desired changes in user or business behaviour, not features to build. Anti-patterns: "Launch feature X" or "Ship v2" as key results — these track effort, not impact. Key results must be quantifiable indicators (conversion, retention, engagement, time-to-value).

### 2. Empowered Product Teams (Cagan)
Team objectives assign **problems to solve**, not features to build. Empowered teams receive a small number of significant problems plus strategic context ("the why"), then use product discovery to determine solutions. If the team cannot change the roadmap in response to learning, OKRs are theater.

### 3. Embracing the "Beautiful Mess" (Cutler)
Alignment is never purely top-down through OKR documents. It also happens through influence, narratives, personas, and constraints. The OKR–roadmap mapping is inherently approximate. The goal is to make relationships visible enough to support decisions — not to force artificial one-to-one mapping.

## OKR Design Anti-Patterns

| Anti-Pattern | Example | Why It Fails |
| :--- | :--- | :--- |
| **Output KRs** | "Ship redesign" | Tracks activity, not success |
| **Vanity Metrics** | "Increase page views" | No link to value or strategy |
| **Too Many OKRs** | 10 objectives per team | Dilutes focus to meaninglessness |
| **Misaligned OKRs** | Random aspirational goals | Don't roll up to company strategy |
| **OKR Lipstick** | Retrofitting metrics onto a fixed feature list | Decorating a feature factory |

## Bet Map Structure (Cutler Model)

Bets move through lifecycle stages:

1. **Ideas / Options** — High-level opportunities, loosely defined, not staffed.
2. **Up Next** — Small number under active discovery, shaped into outcome-oriented one-pagers.
3. **In Progress** — Under delivery, with clear success metrics tied to OKRs.
4. **Live / Monitoring** — Shipped, monitored for impact against KRs; candidates for iteration or retirement.

Only "Up Next" and "In Progress" bets need detail; farther-out bets stay intentionally fuzzy.

## Mapping Mechanics

### Many-to-Many Relationship
- A single bet may contribute to several key results (e.g., improving onboarding affects activation *and* retention).
- A key result may depend on multiple bets (e.g., "reduce churn by 15%" may need onboarding, pricing, and support work).

### Pragmatic Mapping View

| Bet | Stage | Primary OKR(s) | Key Result(s) Targeted | Confidence | Timebox |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *[Example]* | Up Next | O1 | KR1, KR2 | Medium | 6 weeks |

### Guardrails
- Every bet must name at least one OKR and specific KRs it intends to move, or it should not be on the roadmap.
- Every team-level OKR must have at least one active or planned bet; otherwise it is a wish, not a strategy.
- Avoid "OKR washing" — retrofitting superficial metrics onto pre-committed features.

## Cadence and Governance

| Frequency | Activity |
| :--- | :--- |
| **Annually** | Company strategy + high-level company OKRs |
| **Quarterly** | Product/team OKRs negotiated between leadership and teams |
| **Weekly** | Check progress on KRs, review active bets, adjust scope |
| **Continuously** | Bets discovered, prioritized, started, stopped, updated |

## Lightweight Templates

### Team OKR Template
- **Objective**: Problem to solve / outcome to achieve (short, user-centric)
- **Key Results** (2-4): Metric, baseline, target, timeframe
- **Strategic Context**: Which company objective does this support? Why now?

### Bet One-Pager Template
- **Bet Title**: Short phrase
- **Hypothesis**: "If we do X for Y segment, then Z metric will improve from A to B in timeframe T"
- **Linked OKR(s)**: Objective(s) and specific KRs
- **Discovery Plan**: Research/experiments to de-risk value, usability, feasibility, viability
- **Measures**: How impact will be tracked

## Implementation Guidance

For the EKP repository specifically, this playbook should be used to:
1. Wire the existing FY2026 OKRs in `STRATEGY.md` (O1, O2, O3) directly into the `ACTIVE_BET_MAP.md` bets.
2. Add a mapping view showing which bets target which KRs.
3. Structure each bet with a formal hypothesis statement and explicit linked OKRs.
4. Use the Lean Waste Mitigation gates (already implemented) as the "kill criteria" for each bet's Build-Measure-Learn cycle.
