# CALCULATION_LOGIC.md - The EKP Analytical Engine

> **Status**: 🏗️ Active (Draft v1.0)
> **Mandate**: Define the mathematical and semantic formulas powering the LEGO Supply-Chain KG.

## 1. Supply Chain Risk Metrics

### 1.1 Regional Risk Index ($RRI$)
**Purpose**: Convert qualitative ESG certifications into a normalized, queryable risk metric.
**Formula**: 
$RRI = \frac{\sum (Score_{Mapping})}{n}$
**Mapping Table**:
- **Platinum / CDP A / B Corp**: 0.2 (Low Risk)
- **High / Gold / ISCC PLUS**: 0.4 (Moderate)
- **Silver / Standard**: 0.6 (Elevated)
- **Bronze / ISO 14001 / Placeholder**: 0.8 (High Risk)
- **Unknown / No Data**: 0.5 (Neutral)

### 1.2 The Ripple Effect Multiplier ($\alpha$)
**Purpose**: Model the non-linear amplification of delays across $n$ tiers of the supply chain.
**Formula**: 
$Delay_{Propagated} = Delay_{Source} 	imes \alpha^{Tier}$
**Assumptions**:
- **Default $\alpha = 1.2$**: Represents a 20% "friction tax" per tier due to re-planning, logistics buffering, and administrative latency.
- **Example**: A 10-day delay at Tier 2 ($\alpha^{2}$) results in a 14.4-day impact at the Factory.

---

## 2. Sustainability & ESG Metrics

### 2.1 Carbon Removal Offset ($CRO$)
**Purpose**: Balance production emissions against high-integrity carbon credits.
**Logic**: 
- **Factory Level**: Credits are linked to `Factory` nodes to represent "Green Production Capacity."
- **Theme Level**: Credits can be strategically allocated to specific themes (e.g., *Botanicals*) to meet marketing claims.
- **Rule**: $NetEmissions_{Theme} = (\sum Emissions_{Parts}) - (\sum Credits_{Allocated})$

### 2.2 ESG Propagation Score ($EPS$)
**Purpose**: Calculate the aggregate ESG "health" of a product line based on Mass Balance principles.
**Logic**:
- Uses **Max-Risk Propagation**: A set is only as sustainable as its most critical non-certified material supplier.
- **Formula**: $EPS_{Set} = \max(Supplier_{Risk})$ within the `SOURCES_TO` path.

### 2.3 Sustainability Completion % ($SC\%$) & Distance to 2032 Target ($DtT$)
**Purpose**: Strategic reframing of technical risk data into executive-level progress tracking.
**Formula**:
- $SC\%_{Supplier} = (1 - RRI) \times 100$
- $SC\%_{Material} = \begin{cases} 100 & \text{if Sustainable (Bio-PE, Recycled)} \\ 0 & \text{if Petro-based (ABS)} \end{cases}$
- $SC\%_{Theme} = \text{avg}(SC\%_{Material}) + \text{Offsets}$
- $DtT = 100 - SC\%$

---

## 3. Lead-Time Baselines
**Standard Assumptions (used in `lead_time_propagation.py`):**
- **Regional Sourcing**: 7 Days
- **Global Sourcing (Cross-Continent)**: 21 Days
- **Standard Sourcing (Intra-Continent)**: 14 Days
- **Production (Transform)**: 3 Days per Batch
