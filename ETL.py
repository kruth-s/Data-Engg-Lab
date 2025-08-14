import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# -------------------
# 1. Setup
# -------------------
os.makedirs("data_warehouse", exist_ok=True)

# -------------------
# 2. Extract
# -------------------
doctors_df = pd.read_csv("doctors_info.csv")
patients_df = pd.read_csv("patients_data_with_doctor.csv")
feedback_df = pd.read_json("patient_feedback.json")

# -------------------
# 3. Transform
# -------------------

# Parse date columns
patients_df['treatment_date'] = pd.to_datetime(patients_df['treatment_date'], errors='coerce')
feedback_df['review_date'] = pd.to_datetime(feedback_df['review_date'], errors='coerce')

# Define last quarter range (example: Aug 2025 → May–July 2025)
start_qtr = datetime(2025, 5, 1)
end_qtr = datetime(2025, 7, 31)

# Filter for last quarter
patients_qtr = patients_df[
    (patients_df['treatment_date'] >= start_qtr) &
    (patients_df['treatment_date'] <= end_qtr)
]

# Merge feedback with patient data
merged_df = pd.merge(
    patients_qtr,
    feedback_df,
    on=['patient_id', 'treatment_id'],
    how='left'
)

# Merge with doctor info
merged_df = pd.merge(
    merged_df,
    doctors_df,
    on='doctor_id',
    how='left'
)

# Calculate revenue & feedback per doctor
revenue_per_doc = merged_df.groupby(
    ['doctor_id', 'doctor_name'], as_index=False
).agg(
    total_revenue=('treatment_cost', 'sum'),
    avg_feedback=('patient_feedback_score', 'mean')
)

# Get Top 5 by revenue
top5_doctors = revenue_per_doc.sort_values(
    by='total_revenue', ascending=False
).head(5)

# -------------------
# 4. Load
# -------------------
output_path = "data_warehouse/top5_doctor_revenue_feedback.csv"
top5_doctors.to_csv(output_path, index=False)
print(f"Top 5 doctors saved to: {output_path}")

# -------------------
# 5. Visualize
# -------------------
fig, ax1 = plt.subplots(figsize=(10, 6))

# Revenue bars
ax1.bar(top5_doctors['doctor_name'], top5_doctors['total_revenue'], color='skyblue', label='Total Revenue')
ax1.set_xlabel("Doctor Name")
ax1.set_ylabel("Total Revenue", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title("Top 5 Doctors by Revenue (Last Quarter) & Avg Feedback")

# Feedback line
ax2 = ax1.twinx()
ax2.plot(top5_doctors['doctor_name'], top5_doctors['avg_feedback'], color='red', marker='o', label='Avg Feedback Score')
ax2.set_ylabel("Avg Feedback Score", color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
plt.show()
