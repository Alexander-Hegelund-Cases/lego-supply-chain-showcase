# AI Collaboration Manifesto: The 4D Framework

> **Role**: Senior Product Manager - Enterprise Knowledge Platform (EKP)
> **Platform**: Gemini CLI (LLM-Co-Piloted Development)
> **Goal**: Demonstrate responsible, transparent, and high-leverage AI collaboration.

This repository is a co-production between **Alexander Hegelund (Strategic Lead)** and **Gemini CLI (Autonomous Engineering Agent)**. We utilise the **4D Framework** to ensure high-quality, business-viable outcomes.

---

## 1. Delegation (Strategic Split)
*   **Human (Alexander)**: Provided the strategic vision, defined the primary/secondary personas, identified the COO/CTO priorities, and provided the "Expert Frontier" domain logic (SCOR DS v14.0, Mass Balance ISCC PLUS).
*   **AI (Gemini CLI)**: Executed the data engineering (ETL), generated the Neo4j Cypher queries, implemented the Python visualization scripts, and provided initial structural drafting for documentation.
*   **Reasoning**: High-leverage PMs delegate **Execution** to AI while retaining **Vision, Strategy, and Moral/Strategic Oversight**.

## 2. Description (Effective Communication)
*   **Structured Context**: We use the `Gemini.md` manifest as "Working RAM" to maintain state across sessions.
*   **Workflow Automation**: Reusable workflows in `.agents/workflows/` and `.antigravity/commands/` ensure the AI follows consistent, high-standard protocols (e.g., `discovery.md`, `plan.md`).
*   **High-Fidelity Prompting**: Strategic requirements were communicated using JTBD (Jobs to be Done) and Cagan’s 4 Big Risks to ensure the AI's output remained business-aligned.

## 3. Discernment (Critical Evaluation)
*   **Domain Audits**: The `KNOWLEDGE_GAP_REPORT.md` acts as a critical evaluation layer. Alexander audit's the AI's "Parametric Knowledge" against "Expert Frontier" reality.
*   **Technical Verification**: All AI-generated code was executed and verified in a local environment.
*   **Data Confidence**: We implemented a `dataConfidence` and `is_synthetic` property on every node to clearly distinguish between AI-simulated hypotheses and real-world source data.

## 4. Diligence (Responsible AI Collaboration)
*   **FAIR(EST) Alignment**: We use FAIR(EST) principles (Findable, Accessible, Interoperable, Reusable) to ground AI outputs in structured, governed metadata.
*   **Ethics & Transparency**: No proprietary LEGO data was used. Synthetic data is used only to demonstrate "Platform Potential" (e.g., Tier 2 risks) and is explicitly labeled to prevent misinformation.
*   **Human-in-the-Loop (HITL)**: Every major architectural change (e.g., the SCOR DS ontology shift) was preceded by a human review of the plan.

---
*This manifesto serves as a blueprint for how the Enterprise Knowledge Platform will be governed: a synergy of human strategic intent and AI-driven operational scale.*
