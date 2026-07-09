# Education Data Analyst Portfolio Project

A data analysis project exploring what factors are associated with student academic performance — built to showcase data cleaning, exploratory analysis, and visualization skills using Python.

## 📌 Overview

This project analyzes a student performance dataset (500 students) to answer:
- Does completing a test prep course improve scores?
- Does parental education level correlate with student performance?
- How do weekly study hours and attendance rate relate to scores?

## 🛠️ Tools Used
- Python
- pandas (data manipulation)
- matplotlib & seaborn (visualization)

## 📁 Project Structure
```
education-data-analyst-portfolio/
├── data/
│   ├── generate_data.py       # generates the synthetic dataset
│   └── student_performance.csv
├── images/                    # output charts
├── analysis.py                # main analysis script
└── README.md
```

## 🚀 How to Run
```bash
pip install pandas numpy matplotlib seaborn
python data/generate_data.py   # creates the dataset
python analysis.py             # runs analysis, saves charts to images/
```

## 📊 Key Findings
- Students who completed a **test prep course** scored **~8 points higher** on average than those who didn't.
- **Parental education level** shows a positive relationship with average scores.
- **Weekly study hours** and **attendance rate** both show a positive (though moderate) correlation with performance.

## 📈 Sample Visualizations
See the `images/` folder for:
- Score distribution histogram
- Test prep course impact (boxplot)
- Parental education impact (bar chart)
- Study hours vs. score (scatter plot)
- Attendance vs. score (scatter plot)

## 📝 Notes
The dataset used here is synthetically generated (see `data/generate_data.py`) to resemble realistic student performance data, since no personal student data is used. This keeps the project fully reproducible and safe to share publicly.

---
*This project was built as a portfolio piece to demonstrate education data analysis skills.*
