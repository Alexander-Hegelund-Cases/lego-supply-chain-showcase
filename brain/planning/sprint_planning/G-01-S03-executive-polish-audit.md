# HD-Audit: G-01-S03 (Executive Polish & Proactive Scenarios)

> **Status**: 🔴 Pending (User: [Alexander])
> **Sprint**: G-01-S03
> **Goal**: G-01

## Phase A: Strategic Clarity (The Agile Coach)
1.  **The 'North Star' Outcome**: Transition the LEGO Knowledge Graph from a technical "data repository" to a functional "Digital Twin Control Tower" supporting executive-level scenario analysis and ESG strategy.
2.  **Boundary Definition (The 'No-Go' Zone)**:
    - **No New External Data**: We will not attempt to scrape additional public sources for Tier 3+ suppliers in this sprint.
    - **No Web UI**: We stay strictly within the Jupyter Notebook ecosystem for visualization.
    - **No Real-Time Monitoring**: This remains a decision-support prototype, not a real-time operational dashboard.
3.  **The Handshake (Inter-Goal Trigger)**: Completion of PR #10 (Multi-Tier Risk Engine) serves as the trigger for S03.
4.  **ADR Cross-Check**: Consulted `brain/context/PROTOCOL.md` (Domain Atoms) and `brain/context/CALCULATION_LOGIC.md` (Ripple Effects).

## Phase B: Tactical Precision (The System Architect)
5.  **The Data Trail**:
    - `notebooks/lego-knowledge-graph.ipynb`: Major narrative and visual overhaul (Sections 11+).
    - `brain/scripts/`: Update existing scripts (e.g., `risk_scoring.py`) for ESG alignment.
    - `brain/planning/sprint_planning/00_SPRINT_LEDGER.md`: Track task completion.
6.  **The 'Success' Metric**: Executing Section 11 of the notebook produces a coherent "EKP Maturity Scorecard" and "Sawdust" Query narrative without manual code intervention.
7.  **Model Selection Rationale**: **Gemini 1.5 Pro** (High Reasoning) for balancing complex SCM logic with high-level business storytelling.

## Phase C: System Integrity (The Governor)
8.  **Reversibility (The Abort Plan)**: All changes are tracked on `feat/G-01-S03-executive-polish`. Reverting to `main` restores the functional Portfolio v1.1 state.
9.  **Human-in-the-Loop (HITL) Checkpoints**:
    - **T-12 Checkpoint**: Review the "Distance to 2032 Target" (DtT) calculation logic before updating the graph.
    - **T-15 Checkpoint**: Review the EKP Maturity Scorecard visual layout before final sign-off.
10. **Context Neutrality**: Archive S01 and S02 planning files once S03 is fully hardened and accepted.

## Phase D: The Pre-Mortem (The UX Researcher)
*Imagine the plan has failed and we are looking at the wreckage.*
- **Failure Scenario**: The notebook becomes a "Wall of Text/Charts" that obscures the core business insight ("So What?").
- **UX Friction Check**: Does the executive user have to scroll through 100 lines of Python to see a risk report?
- **Preventative Countermeasure**: Use `IPython.display.Markdown` for narrative blocks and `plotly` for interactive, clean charts.
- **Detection Trigger**: If the notebook's "Guided Tour" takes more than 5 minutes to explain, we have failed the "Executive Polish" mandate.
