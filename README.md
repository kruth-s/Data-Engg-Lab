# Doctor--Patient Data Engineering Lab

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

-   Business Question:\
    "Who are the top 5 doctors by revenue in the last quarter, and how
    does patient feedback vary for these doctors?"
-   Data Sources:
    -   `doctors_info.csv` → doctor details.\
    -   `patients_data_with_doctor.csv` → patient treatments.\
    -   `patient_feedback.json` → patient reviews and sentiment.\
-   Required Data Points:
    -   `doctor_id`, `doctor_name`, `treatment_cost`, `treatment_date`,
        `patient_id`, `treatment_id`, `patient_feedback_score`.\
-   Outcome: Report with top doctors by revenue and their average
    feedback score.

### Stage 2 -- Data Engineer Task (ETL Pipeline)

-   Extract: Load data from CSV and JSON using pandas.\
-   Cleanse:
    -   Standardize dates.\
    -   Handle missing values.\
    -   Ensure numeric data types.\
-   Transform:
    -   Filter treatments to last quarter (May--July 2025).\
    -   Merge patients, feedback, and doctor info.\
    -   Compute per-doctor revenue and average feedback.\
-   Load: Save processed dataset to:\
    `data_warehouse/top5_doctor_revenue_feedback.csv`

### Stage 3 -- Data Analyst Task

-   Access processed dataset.\
-   Group by doctor to compute total revenue and average feedback.\
-   Select top 5 doctors by revenue.\
-   Visualization:
    -   Blue bars = revenue per doctor.\
    -   Red line = average feedback scores.

### Stage 4 -- Reporting and Insights (Business Analyst)

-   Findings:
    -   Identifies top-performing doctors.\
    -   Shows whether high revenue aligns with high patient
        satisfaction.\
-   Example Insights:
    -   "Dr. A generates the highest revenue but has low feedback,
        indicating potential patient dissatisfaction."\
    -   "Dr. C has both high revenue and excellent feedback, making them
        a role model doctor."\
-   Recommendations:
    -   Improve service quality for revenue-heavy doctors with poor
        feedback.\
    -   Recognize and reward doctors excelling in both revenue and
        satisfaction.

### Stage 5 -- ML Engineer Task (VIP Patient Classification)

-   Objective: Identify VIP patients for loyalty programs and targeted
    care.\
-   Features:
    -   Total spend, treatment frequency, average feedback score,
        average treatment value.\
-   Model: Logistic Regression or K-Means clustering.\
-   Enrichment: Add new column `is_VIP` to patient dataset.\
-   Reverse ETL: Export enriched dataset to CSV or CRM for business
    use:\
    `data_warehouse/patients_with_vip_status.csv`

## Example Visualization

Top 5 Doctors by Revenue (Last Quarter) and Average Feedback

-   Blue Bars = Revenue\
-   Red Line = Average Feedback

(Generated automatically by pipeline using matplotlib)

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

4.  Run VIP classification:

    ``` bash
    python vip_classification.py
    ```

## Learning Outcomes

-   Apply ETL (Extract--Transform--Load) in healthcare data.\
-   Handle data quality issues (missing values, inconsistent formats).\
-   Use business analysis to drive technical decisions.\
-   Build visualizations to communicate insights.\
-   Implement reverse ETL for enriching operational datasets.\
-   Apply machine learning models to classify VIP patients.
