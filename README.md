# SU_ResearchTask_USPresidentalElection2024
US Presidential Election 2024 Analysis

# Task 04 — Descriptive Statistics System

This project performs descriptive statistical analysis on datasets related to the 2024 U.S. Presidential Election using three different approaches:

- Pure Python (no libraries)
- Pandas
- Polars

---

## 📁 Dataset

> Dataset is **NOT** committed to the repo as instructed.  
You can download it from:  
https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view

---

## 📂 Directory Structure

```
Task_04_Descriptive_Stats/
├── data/                            # (excluded) place .csv files here
├── src/
│   ├── pure_python_stats.py
│   ├── pandas_stats.py
│   └── polars_stats.py
├── .gitignore
└── README.md
```

---

## 🛠 How to Run

```bash
cd src

# Pure Python
python3 pure_python_stats.py

# Pandas
python3 pandas_stats.py

# Polars (for Apple Silicon)
python3 polars_stats.py
```

Install dependencies first:

```bash
pip install pandas polars-lts-cpu
```

---

## 📊 Output Summary

Each script generates:
- Overall column stats (mean, min, max, count)
- Top frequent values (for categorical columns)
- Grouped statistics by `Facebook_Id` (and `ad_id` for ads dataset)

---

## 💡 Observations

| Method        | Strengths                              | Challenges                           |
|---------------|-----------------------------------------|---------------------------------------|
| Pure Python   | Transparent, dependency-free            | Slower, verbose grouping logic       |
| Pandas        | Rich API, fast development              | Slower on large data                 |
| Polars        | Extremely fast and memory-efficient     | Minor quirks (e.g., Apple Silicon)   |

---

## 🧠 AI Reflection

When asked for code to perform descriptive stats, tools like ChatGPT typically recommend using **Pandas**.  
That’s a good choice for beginner to intermediate use cases. However, for performance and speed, **Polars** is often better.  
Pure Python is still important when environments restrict package use or for deeper understanding of data processing.

---

---

## 📦 Week 2 Extension – Generalization to Public Datasets

In Week 2, the system was extended to demonstrate flexibility beyond the election datasets. A widely used public dataset, `titanic_train.csv` from the Kaggle Titanic competition, was chosen.

The same statistical scripts were reused with small modifications:
- Changed `FILE_PATH` to point to `data/titanic_train.csv`
- Replaced `Facebook_Id` with appropriate grouping columns like `Pclass` and `Sex`

### 🔁 Modified Scripts for Titanic Dataset
- `pure_python_stats.py` → grouped by `Pclass`
- `pandas_stats.py` → grouped by `Sex`
- `polars_stats.py` → grouped by `Pclass`

This validated the design’s modularity and generality — confirming that:
- All numeric and non-numeric stats worked without changes to core logic
- Grouping and value count logic handled new column names smoothly
- Outputs were consistent across formats

This shows that the system is capable of handling **arbitrary structured datasets** with minimal adjustments, making it reusable for other real-world CSV files.

