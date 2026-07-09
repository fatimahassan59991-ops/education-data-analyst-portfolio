"""
Education Data Analyst Portfolio Project
Analyzes student performance data and produces summary stats + charts.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("data/student_performance.csv")

print("=== Dataset Overview ===")
print(df.head())
print("\n=== Summary Statistics ===")
print(df.describe())

df["avg_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)

# --- Chart 1: Score distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(df["avg_score"], bins=25, kde=True, color="#4C72B0")
plt.title("Distribution of Average Student Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("images/score_distribution.png", dpi=150)
plt.close()

# --- Chart 2: Test prep impact ---
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="test_prep_course", y="avg_score", palette="Set2")
plt.title("Test Prep Course Completion vs Average Score")
plt.xlabel("Test Prep Course")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("images/test_prep_impact.png", dpi=150)
plt.close()

# --- Chart 3: Parental education vs score ---
plt.figure(figsize=(8, 5))
order = ["High School", "Some College", "Bachelor's", "Master's"]
sns.barplot(data=df, x="parental_education", y="avg_score", order=order, palette="Blues_d")
plt.title("Average Score by Parental Education Level")
plt.xlabel("Parental Education")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("images/parental_education_impact.png", dpi=150)
plt.close()

# --- Chart 4: Study hours vs score (scatter) ---
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="weekly_study_hours", y="avg_score", hue="test_prep_course", alpha=0.7)
plt.title("Weekly Study Hours vs Average Score")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("images/study_hours_vs_score.png", dpi=150)
plt.close()

# --- Chart 5: Attendance vs score ---
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="attendance_rate", y="avg_score", color="#55A868", alpha=0.7)
plt.title("Attendance Rate vs Average Score")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("images/attendance_vs_score.png", dpi=150)
plt.close()

print("\nAll charts saved to images/ folder.")

# --- Key insights printed to console ---
print("\n=== Key Insights ===")
prep_diff = df.groupby("test_prep_course")["avg_score"].mean()
print(f"Avg score with test prep: {prep_diff['Completed']:.1f}")
print(f"Avg score without test prep: {prep_diff['Not Completed']:.1f}")

corr = df[["weekly_study_hours", "attendance_rate", "avg_score"]].corr()
print("\nCorrelation with avg_score:")
print(corr["avg_score"])
