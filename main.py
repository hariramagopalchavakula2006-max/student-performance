
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Save charts to files; no interactive GUI is required.
import matplotlib.pyplot as plt

from functions import (
    SUBJECTS, load_dataset, add_student_metrics,
    subject_summary, build_summary
)

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "students.csv"
OUTPUT_DIR = ROOT / "output"

def create_charts(results, subjects):
    """Create and save charts using Matplotlib."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Chart 1: average marks by subject
    plt.figure(figsize=(8, 5))
    bars = plt.bar(subjects["Subject"], subjects["Average"])
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average marks out of 100")
    plt.ylim(0, 100)
    plt.bar_label(bars, fmt="%.1f", padding=3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "subject_averages.png", dpi=150)
    plt.close()

    # Chart 2: top five students by average
    top_five = results.nlargest(5, "Average_Marks").sort_values("Average_Marks")
    plt.figure(figsize=(9, 5))
    bars = plt.barh(top_five["Name"], top_five["Average_Marks"])
    plt.title("Top 5 Students by Average Marks")
    plt.xlabel("Average marks out of 100")
    plt.xlim(0, 100)
    plt.bar_label(bars, fmt="%.1f", padding=3)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_five_students.png", dpi=150)
    plt.close()

    # Chart 3: pass/fail distribution
    counts = results["Result"].value_counts().reindex(["PASS", "FAIL"], fill_value=0)
    plt.figure(figsize=(6, 5))
    plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Pass / Fail Distribution")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "pass_fail_distribution.png", dpi=150)
    plt.close()

def main():
    try:
        df = load_dataset(DATA_FILE)
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Dataset error: {error}")
        return

    results = add_student_metrics(df)
    summary = build_summary(df)
    subjects = subject_summary(df)
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("\\n" + "=" * 62)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 62)
    print(f"Students analysed       : {summary['student_count']}")
    print(f"Class average           : {summary['class_average']:.2f}/100")
    print(f"Passed / Failed         : {summary['pass_count']} / {summary['fail_count']}")
    print(f"Average attendance      : {summary['average_attendance']:.2f}%")
    print(f"Top performer           : {summary['top_name']} ({summary['top_average']:.2f})")
    print(f"Lowest average          : {summary['lowest_name']} ({summary['lowest_average']:.2f})")

    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Attendance_Percent", "Result"
    ]
    print("\\n--- Student Results (highest average first) ---")
    print(results[display_columns].sort_values(
        "Average_Marks", ascending=False
    ).to_string(index=False))

    print("\\n--- Subject-wise Summary ---")
    print(subjects.to_string(index=False))

    print("\\n--- Top 5 Students ---")
    print(results.nlargest(5, "Average_Marks")[
        ["Name", "Department", "Average_Marks", "Grade"]
    ].to_string(index=False))

    results.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
    subjects.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)
    create_charts(results, subjects)

    print("\\nFiles created in the output folder:")
    for name in [
        "student_results.csv", "subject_summary.csv",
        "subject_averages.png", "top_five_students.png",
        "pass_fail_distribution.png"
    ]:
        print(f"- {name}")
    print("\\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()
