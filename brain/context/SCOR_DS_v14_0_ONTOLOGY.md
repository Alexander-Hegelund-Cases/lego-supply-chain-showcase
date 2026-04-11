---
title: "ASCM SCOR DS v14.0 Process Ontology"
ontology_alignment: "SCOR DS v14.0"
confidence_score: 1.0
last_updated: 2026-04-07
---

# SCOR DS v14.0 Process Hierarchy (Level-1 & 2)

This document defines the process ontology for the LEGO Supply-Chain Knowledge Graph, aligning with the ASCM SCOR Digital Standard (v14.0).

## 1. Core Level-1 Processes

| Process | Definition | KG Relationship Map |
| :--- | :--- | :--- |
| **Orchestrate** | Integration of supply chain strategy and execution. | `(Region)-[:FORECASTS_DEMAND {volume, history}]->(Set)` |
| **Plan** | Balancing aggregate demand and supply (PSI). | `(Factory)-[:PLANS_FOR {inventory_level, safety_stock}]->(Region)` |
| **Order** | Managing customer orders and inventory allocations. | `(Set)-[:ORDERED_IN {order_volume}]->(Region)` |
| **Source** | Procurement of materials and components. | `(Supplier)-[:SOURCES_TO {inbound_volume, is_collaborative}]->(Factory)` |
| **Transform** | Conversion of materials into finished products. | `(Factory)-[:TRANSFORMS_TO {production_capacity, lead_time}]->(Set)` |
| **Fulfill** | Storage, transportation, and delivery to customer. | `(Factory)-[:FULFILLS_TO]->(Region)` |
| **Return** | Reverse logistics and circular economy flows. | `(Set)-[:RETURNS_FROM]->(Factory)` |

## 2. Level-2 Process Categories (Source & Transform Focus)

### sS: Source Processes
- **sS1: Direct Procure**: Procurement of production materials (e.g., ABS, Bio-PE).
- **sS2: Strategic Source**: Sourcing from key Tier 1/2 partners.

### sT: Transform Processes
- **sT1: Produce & Test**: Manufacturing finished LEGO sets.
- **sT2: Package**: Final packaging and kitting.

## 3. Implementation in Neo4j
To align the prototype with this standard, existing relationships must be refactored:
1.  `SUPPLIES` → `SOURCES_TO`
2.  `BUILDS` → `TRANSFORMS_TO`
3.  `SERVES` → `FULFILLS_TO`

## 4. Governance
All relationships using these labels MUST include:
- `process_level`: (Int) 1 or 2.
- `scor_id`: (String) e.g., "sS1", "sT1".
- `source`: (String) The origin of the data.
