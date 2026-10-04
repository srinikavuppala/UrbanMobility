# 🚍 UrbanMobility 360 – Smart Urban Transport Analytics

> **NYC Yellow Taxi | January 2024 | Python + Tableau**

## Overview

UrbanMobility 360 analyzes **NYC Yellow Taxi trip data** for January 2024 to identify **where, when, and why** travel demand, congestion, and inefficient transport usage occur.

The project follows an end-to-end analytics workflow:

**Raw Data → Data Cleaning → Feature Engineering → Exploratory Analysis → Mobility Priority Scoring → Tableau Dashboard → Insights**

---

## Problem Statement

Urban congestion is a critical issue in cities like New York. Transportation planners need data-driven answers to:

- **WHERE** are the mobility hotspots?
- **WHEN** does peak demand occur?
- **WHY** does congestion occur?
- **WHICH** areas are most inefficient?
- **WHAT** should be prioritized for optimization?

UrbanMobility addresses these questions using more than **2.3 million processed taxi trips**.

---

## Key Results

| Metric | Result |
|---|---:|
| Trips Analyzed | **2,338,354** |
| Taxi Zones Analyzed | **240** |
| Unique Routes | **9,187** |
| High-Priority Hotspots | **13** |
| Highest Priority Score | **64.7 / 100** |
| Peak Speed Drop | **4.6%** |
| Peak Congestion Rate | **64.5%** |

### ⭐ Top Finding

**Midtown Center at 6 PM on weekdays** is the primary mobility hotspot, with **10,890 trips**, an average speed of **7.8 mph**, and a **64.7/100 Mobility Priority Score**.

---

## Mobility Priority Score

The core analytical contribution is a **Mobility Priority Score (0–100)** that measures how urgently a specific **zone-hour combination** requires transport optimization.

### Formula

```text
Priority Score =
(0.30 × Demand_norm
+ 0.30 × Congestion_norm
+ 0.20 × Speed_Inverse_norm
+ 0.20 × Duration_norm) × 100
```

| Factor | Weight | Purpose |
|---|---:|---|
| Demand | 30% | Measures the number of trips affected |
| Congestion | 30% | Represents congestion severity |
| Speed Inverse | 20% | Gives higher priority to slower conditions |
| Duration | 20% | Captures additional travel time |

### Priority Levels

| Score | Priority |
|---:|---|
| 75–100 | Critical |
| 55–75 | High |
| 35–55 | Medium |
| 15–35 | Low |
| 0–15 | Minimal |

---

## Project Workflow

```text
Raw NYC TLC Data
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
Mobility Priority Scoring
       ↓
Insights & Recommendations
       ↓
Interactive Tableau Dashboard
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.12** | Data processing and analysis |
| **Pandas** | Cleaning, transformation, aggregation |
| **NumPy** | Numerical operations |
| **Scikit-learn** | Feature normalization |
| **Matplotlib** | Data visualization |
| **Seaborn** | Heatmaps and statistical plots |
| **PyArrow** | Parquet data processing |
| **Jupyter Notebook** | Interactive analysis |
| **Tableau Public** | Interactive dashboard |

---

## Dataset

**Source:** NYC Taxi & Limousine Commission (TLC) Trip Record Data  
**Period:** January 2024  
**Format:** Parquet

| Dataset Stage | Records |
|---|---:|
| Raw Dataset | 2,964,624 |
| Clean Dataset | 2,352,078 |
| Final Analytical Dataset | 2,338,354 |

### Original Columns

```text
VendorID, tpep_pickup_datetime, tpep_dropoff_datetime,
passenger_count, trip_distance, RatecodeID, store_and_fwd_flag,
PULocationID, DOLocationID, payment_type, fare_amount, extra,
mta_tax, tip_amount, tolls_amount, improvement_surcharge,
total_amount, congestion_surcharge, Airport_fee
```

---

## Project Structure

The repository is organized into separate directories for the dataset, analysis notebooks, Tableau work, and generated visualizations.

```text
UrbanMobility360/
│
├── .venv/                         # Python virtual environment
├── data/                          # Raw and processed datasets
├── notebooks/                     # Jupyter notebooks
├── tableau/                       # Tableau dashboard files
├── venv/                          # Python virtual environment
├── visuals/                       # Generated charts and visualizations
├── .gitignore                     # Git ignore configuration
└── UrbanMobility360_info.html     # Project documentation
```

> **Note:** `.venv/` and `venv/` are local Python environments and should normally be excluded from version control using `.gitignore`.

---

## Notebook Details

### 01 — Data Loading

- Loads NYC TLC Parquet data and taxi-zone lookup data.
- Inspects dimensions, columns, data types, and missing values.
- Validates date ranges and location IDs.
- Identifies invalid dates and missing values.

### 02 — Data Cleaning

Applies an 8-step preprocessing pipeline:

1. Date filtering
2. Duplicate removal
3. Trip-distance validation
4. Fare validation
5. Passenger-count validation
6. Trip-duration validation
7. Zone validation
8. IQR-based outlier removal

**Output:** 2,352,078 clean records with **79.3% retention**.

### 03 — Feature Engineering

Creates **19 additional features** covering:

- Time and date information
- Weekday/weekend classification
- Peak-period indicators
- Average speed
- Fare efficiency
- Congestion indicators
- Pickup/drop-off zone names
- Boroughs
- Route and zone-pair identifiers

**Output:** 2,338,354 rows × 39 columns.

### 04 — Exploratory Analysis

Performs analysis using eight major visualizations:

- Hourly demand
- Weekday vs. weekend demand
- Top pickup zones
- Borough analysis
- Speed vs. trip duration
- Zone-hour demand heatmap
- Priority distribution
- Peak vs. off-peak comparison

**Key finding:** Average speed decreases by **4.6%** during peak periods.

### 05 — Advanced Analysis

Generates:

- Zone-hour aggregation
- Route-level statistics
- Congestion classification
- Route Efficiency Score
- **Mobility Priority Score**
- Tableau-ready CSV datasets

### 06 — Insights Report

Answers the five core mobility questions:

**WHERE → WHEN → WHY → WHICH → WHAT TO PRIORITIZE**

The notebook produces key findings and recommendations from the analytical results.

---

## Tableau Dashboard

The project includes an interactive Tableau dashboard containing eight worksheets.

| Worksheet | Visualization | Purpose |
|---|---|---|
| **KPI Trips** | Big Number | Total trip count |
| **KPI Speed** | Big Number | Average trip speed |
| **Hourly Demand** | Line Chart | Demand by hour |
| **Demand Heatmap** | Zone × Hour Grid | Spatial-temporal demand |
| **Priority Zones** | Bar Chart | Mobility priority areas |
| **Speed vs Duration** | Scatter Plot | Speed-duration relationship |
| **Borough Stats** | Bar Chart | Borough-level comparison |
| **Priority Dist** | Bar Chart | Priority-level distribution |

### Interactive Filters

- **PU_borough**
- **day_type**
- **peak_period**

These filters allow users to explore mobility conditions across different geographical and temporal segments.

---

## Key Insights

### 1. WHERE

**Midtown Center, Upper East Side South, and Penn Station** emerge as major mobility hotspots.

**Brownsville** shows a high per-zone priority level associated with a low average speed of approximately **7.6 mph**.

### 2. WHEN

The busiest hours are **6 PM, 5 PM, and 7 PM**.

Average daily demand is approximately:

- **Weekday:** 75,191 trips/day
- **Weekend:** 76,118 trips/day

### 3. WHY

Peak-period conditions show:

- Average speed: **9.4 mph**
- Off-peak average speed: **9.9 mph**
- Speed reduction: **4.6%**
- Peak congestion: approximately **64.5%**

### 4. WHICH

**Midtown Center** has six high-priority hours. During the evening peak, it handles approximately **10,000 trips at around 7 mph**.

---

## Recommendations

| Area | Recommendation |
|---|---|
| **Midtown Center** | Dedicated bus/taxi lanes during 4–8 PM and signal optimization during peak hours |
| **Upper East Side South** | Consider transit signal priority during afternoon peak periods |
| **Brownsville** | Improve transportation infrastructure to raise average speed above 10 mph |

---

## How to Run

### 1. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn pyarrow scikit-learn jupyter
```

### 2. Download the Dataset

Download the **January 2024 NYC Yellow Taxi Trip Record** and place it inside:

```text
data/raw/
```

### 3. Start Jupyter Notebook

```bash
jupyter notebook
```

### 4. Run the Notebooks

Execute the notebooks in order:

```text
01 → 02 → 03 → 04 → 05 → 06
```

### 5. Open Tableau

Connect Tableau to the processed CSV files in:

```text
data/processed/
```

Build the dashboard using the worksheets and filters described above.

---

## Data Source

**NYC Taxi & Limousine Commission — TLC Trip Record Data**

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

---

## Project Highlights

- **2.3M+** taxi trips analyzed
- **39** analytical features
- **9,187** unique routes
- **13** high-priority hotspots
- **8** Tableau worksheets
- **0–100** Mobility Priority Score
- End-to-end **Python + Tableau** analytics pipeline

---

## Author

**UrbanMobility 360 – Smart Urban Transport Analytics Project**

---

## License

This project uses publicly available data from the **NYC Taxi & Limousine Commission (TLC)**. Data usage is subject to the applicable NYC Open Data terms of use.
