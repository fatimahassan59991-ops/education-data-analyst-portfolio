"""
Generates a synthetic student performance dataset for the portfolio project.
Run this once to create data/student_performance.csv
"""
import numpy as np
import pandas as pd

np.random.seed(42)

n = 500

genders = np.random.choice(["Male", "Female"], size=n)
parental_education = np.random.choice(
    ["High School", "Some College", "Bachelor's", "Master's"],
    size=n, p=[0.35, 0.30, 0.25, 0.10]
)
lunch = np.random.choice(["Standard", "Free/Reduced"], size=n, p=[0.6, 0.4])
test_prep = np.random.choice(["Completed", "Not Completed"], size=n, p=[0.4, 0.6])
study_hours = np.round(np.random.normal(5, 2, n).clip(0, 15), 1)
attendance_rate = np.round(np.random.normal(90, 8, n).clip(50, 100), 1)

# Build scores with some realistic relationships baked in
base = np.random.normal(65, 12, n)
base += (test_prep == "Completed") * 8
base += (lunch == "Standard") * 5
base += (parental_education == "Bachelor's") * 4
base += (parental_education == "Master's") * 7
base += (study_hours - 5) * 1.5
base += (attendance_rate - 90) * 0.4

math_score = np.round((base + np.random.normal(0, 5, n)).clip(0, 100), 1)
reading_score = np.round((base + np.random.normal(0, 5, n)).clip(0, 100), 1)
writing_score = np.round((base + np.random.normal(0, 5, n)).clip(0, 100), 1)

df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "gender": genders,
    "parental_education": parental_education,
    "lunch_type": lunch,
    "test_prep_course": test_prep,
    "weekly_study_hours": study_hours,
    "attendance_rate": attendance_rate,
    "math_score": math_score,
    "reading_score": reading_score,
    "writing_score": writing_score,
})

df.to_csv("data/student_performance.csv", index=False)
print("Saved data/student_performance.csv with", len(df), "rows")
