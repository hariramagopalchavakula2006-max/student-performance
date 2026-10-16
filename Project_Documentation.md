# Project Documentation — Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**  
Student name: [Enter your name]  
Student ID: [Enter your ID]  
Course: Python with AI

## 2. Objective
To build a Python program that reads student records, analyses marks and attendance, and presents understandable results and visual summaries.

## 3. Technologies Used
- **Python:** variables, conditions, loops, functions and file paths.
- **Pandas:** CSV loading, DataFrame operations, summaries and CSV export.
- **NumPy:** numerical operations and pass/fail classification.
- **Matplotlib:** charts for subject averages, top students and pass/fail distribution.
- **Python standard library:** `pathlib` for file paths.

No other third-party libraries are used.

## 4. Dataset Description
The CSV contains 20 fictional students. Fields include Student ID, name, department, marks in Python/NumPy/Pandas/Statistics, attendance percentage and assignment percentage.

## 5. Implementation
1. `load_dataset()` reads the CSV with Pandas and validates columns and numeric values.
2. `add_student_metrics()` calculates total marks and average marks.
3. `assign_grade()` assigns grades using the grading scale.
4. NumPy `where()` assigns PASS if every subject mark is at least 40 and attendance is at least 75%; otherwise FAIL.
5. `subject_summary()` calculates average, highest and lowest marks for each subject.
6. `build_summary()` calculates class statistics and identifies top and lowest performers.
7. `create_charts()` uses Matplotlib to save three charts as PNG images.
8. Pandas exports the detailed results and subject summary as CSV reports.

## 6. Key Features
- Dataset loading and validation.
- Student totals, averages, grades and pass/fail results.
- Overall class statistics and top five performers.
- Subject-wise average, highest and lowest marks.
- Two CSV reports and three Matplotlib charts.
- Basic error handling for missing files, invalid data and missing columns.

## 7. Output / Screenshots
Run `python main.py` and capture:
- The class summary in the terminal.
- The student results and subject summary tables.
- `subject_averages.png`, `top_five_students.png` and `pass_fail_distribution.png`.
- The generated CSV files in the `output/` directory.

## 8. Final Outcome
The program demonstrates the use of Python, NumPy and Pandas for structured data analysis, and Matplotlib for visualizing the results. It produces reproducible tabular reports and charts from the input dataset.

## Grading Rule
| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Limitations and Future Improvements
- Dataset records are fictional.
- Grade and pass/fail thresholds are sample rules and can be adjusted to institutional requirements.
- The program is a command-line project; a dashboard is intentionally not included to keep within the assignment's library restrictions.
