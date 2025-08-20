# Fundamentals of Data Engineering Lab

## Overview

This lab demonstrates an end-to-end data pipeline (ETL and Machine
Learning) for healthcare data. It extracts doctor, patient, and feedback
data, cleans and merges them, calculates per-doctor revenue and
feedback, identifies the top 5 doctors by revenue, and visualizes
results.

Additionally, a machine learning workflow is included to classify VIP
patients based on treatment and feedback patterns, and a reverse ETL
process exports enriched data for business use.

## Workflow Stages

### Stage 1 -- Business Analyst Task

### Stage 2 -- Data Engineer Task (ETL Pipeline)

-   Extract: Load data from CSV and JSON using pandas.
-   Cleanse:
    -   Standardize dates.
    -   Handle missing values.
    -   Ensure numeric data types.
-   Transform:
    -   Filter treatments to last quarter (May--July 2025).
    -   Merge patients, feedback, and doctor info.
    -   Compute per-doctor revenue and average feedback.
-   Load: Save processed dataset to:
    `data_warehouse/top5_doctor_revenue_feedback.csv`

### Stage 3 -- Data Analyst Task

### Stage 4 -- Reporting and Insights (Business Analyst)


### Stage 5 -- ML Engineer Task (VIP Patient Classification)

-   Objective: Identify VIP patients for loyalty programs and targeted
    care.
-   Features:
    -   Total spend, treatment frequency, average feedback score,
        average treatment value.
-   Model: Logistic Regression or K-Means clustering.
-   Enrichment: Add new column `is_VIP` to patient dataset.
-   Reverse ETL: Export enriched dataset to CSV or CRM for business
    use:\
    `data_warehouse/patients_with_vip_status.csv`


## Repository Structure

    Data-Engg-Lab/
    │
    ├── raw_data/
    │   ├── doctors_info.csv
    │   ├── patients_data_with_doctor.csv
    │   └── patient_feedback.json
    │
    ├── data_warehouse/
    │   ├── processed_sales_data.csv
    │   ├── top5_doctor_revenue_feedback.csv
    │   └── patients_with_vip_status.csv
    │
    ├── etl_pipeline.py          # Doctor–Patient ETL pipeline
    ├── vip_classification.py    # Machine Learning pipeline for VIP patients
    └── README.md                # Documentation

## How to Run

1.  Clone the repository:

    ``` bash
    git clone https://github.com/kruth-s/Data-Engg-Lab.git
    cd Data-Engg-Lab
    ```

2.  Install dependencies:

    ``` bash
    pip install pandas matplotlib scikit-learn
    ```

3.  Run ETL pipeline:

    ``` bash
    python etl_pipeline.py
    ```

