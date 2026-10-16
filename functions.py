"""Reusable data processing functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Python", "NumPy", "Pandas", "Statistics"]
REQUIRED_COLUMNS = [
    "Student_ID", "Name", "Department", *SUBJECTS,
    "Attendance_Percent", "Assignment_Percent"
]

def load_dataset(file_path):
    """Load and validate the student CSV file."""
    df = pd.read_csv(file_path)
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError("Missing columns: " + ", ".join(missing))
    if df.empty:
        raise ValueError("The dataset is empty.")

    numeric_columns = SUBJECTS + ["Attendance_Percent", "Assignment_Percent"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    if df[numeric_columns].isna().any().any():
        raise ValueError("Numeric fields contain missing or invalid values.")
    if ((df[SUBJECTS] < 0) | (df[SUBJECTS] > 100)).any().any():
        raise ValueError("Subject marks must be between 0 and 100.")
    percentage_columns = ["Attendance_Percent", "Assignment_Percent"]
    if ((df[percentage_columns] < 0) | (df[percentage_columns] > 100)).any().any():
        raise ValueError("Percentages must be between 0 and 100.")
    return df

def assign_grade(average):
    """Assign a grade using the documented grading scale."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"

def add_student_metrics(df):
    """Calculate total, average, grade and pass/fail for every student."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = result[SUBJECTS].mean(axis=1).round(2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    passed = result[SUBJECTS].ge(40).all(axis=1) & result["Attendance_Percent"].ge(75)
    result["Result"] = np.where(passed, "PASS", "FAIL")
    return result

def subject_summary(df):
    """Calculate subject-wise average, maximum and minimum marks."""
    rows = []
    for subject in SUBJECTS:
        rows.append({
            "Subject": subject,
            "Average": round(float(df[subject].mean()), 2),
            "Highest": int(df[subject].max()),
            "Lowest": int(df[subject].min())
        })
    return pd.DataFrame(rows)

def build_summary(df):
    """Calculate class-level statistics and top/lowest student."""
    results = add_student_metrics(df)
    top = results.loc[results["Average_Marks"].idxmax()]
    lowest = results.loc[results["Average_Marks"].idxmin()]
    return {
        "student_count": len(results),
        "class_average": round(float(results["Average_Marks"].mean()), 2),
        "pass_count": int(results["Result"].eq("PASS").sum()),
        "fail_count": int(results["Result"].eq("FAIL").sum()),
        "average_attendance": round(float(results["Attendance_Percent"].mean()), 2),
        "top_name": str(top["Name"]),
        "top_average": float(top["Average_Marks"]),
        "lowest_name": str(lowest["Name"]),
        "lowest_average": float(lowest["Average_Marks"])
    }
