[🏠 Main README](../README.md) ❯ 📚 Docs ❯ �� Sandbox Setup

# 💻 EKP Sandbox: Technical Setup

> [!NOTE]
> **TL;DR**: Technical instructions for spinning up the local graph database and Jupyter Notebook.

<details>
<summary><b>🗺️ Expand Table of Contents</b></summary>

  - [Prerequisites](#prerequisites)
  - [Step 1: Environment Configuration](#step-1-environment-configuration)
  - [Step 2: Database Connection](#step-2-database-connection)
  - [Step 3: Run the Guided Initialization](#step-3-run-the-guided-initialization)
  - [Step 4: The CI/CD Pipeline & Governance](#step-4-the-cicd-pipeline-governance)

</details>
This repository contains a full codebase allowing technical stakeholders to natively replicate the graph architecture. 

If you wish to run the ingestion logic and view the Cypher propagation live on your local machine, follow the technical instructions below.

---

### Prerequisites
*   **Python 3.10+**
*   **Neo4j Desktop** or a free [Neo4j AuraDB Cloud](https://neo4j.com/cloud/platform/aura-graph-database/) instance.

### Step 1: Environment Configuration
Clone the repository and install the data processing requirements.
```bash
git clone https://github.com/lego-supply-chain-showcase.git
cd lego-supply-chain-showcase
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Database Connection
You must provide your Neo4j credentials via an environment file. 
Create a `.env` file in the root directory:
```env
NEO4J_URI=neo4j+s://<your-instance>.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=<your-secure-password>
```

### Step 3: Run the Guided Initialization
The easiest way to populate your Graph Database and witness the mathematical propagation of supply chain delays (The Ripple Effect) is to utilise the interactive Jupyter Notebook.

```bash
jupyter notebook notebooks/lego-knowledge-graph.ipynb
```

Within the Notebook, you will step through:
1. Connecting to Neo4j.
2. Ingesting 20,000+ LEGO Sets from Rebrickable.
3. Ingesting Regional/Factory logic.
4. Executing the Advanced Supply Chain Risk simulations.

### Step 4: The CI/CD Pipeline & Governance
To ensure enterprise-grade reliability, this repository implements a continuous integration protocol (`.github/workflows/ci.yml`). 
Whenever a Pull Request is pushed, GitHub Actions automatically provisions a runner and executes:
1. **Flake8 Linting**: Blocking fatal syntax errors or variable collisions.
2. **Black Formatting**: Enforcing normalized PEP-8 coding standards across the data science teams.
3. **Graph Integrity Checks**: Validating `Cypher` query execution speeds and ontological health.

---
<div align="center">
  <b><a href="../README.md">🔙 Return to the Main Showcase</a></b> | <b><a href="GLOSSARY.md">📖 View the Ecosystem Glossary</a></b>
</div>
