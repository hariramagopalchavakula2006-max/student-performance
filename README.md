# Student Performance Analytics System

A Python data-analysis project built with **only the libraries specified for this assignment plus Matplotlib**:
- Python standard library
- NumPy
- Pandas
- Matplotlib

No Streamlit, Flask, Seaborn, scikit-learn, or other third-party libraries are used.

## Features
- Reads a CSV dataset with Pandas.
- Validates required columns and numeric ranges.
- Uses NumPy and Pandas to calculate totals, averages and pass/fail results.
- Assigns grades using a documented rule.
- Finds class average, pass/fail counts, top/lowest performers and attendance average.
- Produces subject-wise statistics.
- Exports student and subject summaries as CSV.
- Uses Matplotlib to create three charts: subject averages, top five students, and pass/fail distribution.

## Project structure
```text
student_performance_analytics_matplotlib/
├── data/
│   └── students.csv
├── output/                      # Generated after running main.py
├── main.py
├── functions.py
├── requirements.txt
├── Project_Documentation.md
└── README.md
```

## Run
Install the three required packages:
```bash
python -m pip install -r requirements.txt
```
Run the program:
```bash
python main.py
```

## Dataset
The sample CSV contains 20 fictional student records with Student ID, name, department, marks in Python, NumPy, Pandas and Statistics, attendance percentage, and assignment percentage.

## Rules
- Total marks: sum of four subjects (maximum 400).
- Average marks: mean of the four subject marks (maximum 100).
- Grade: A+ >= 90; A >= 80; B >= 70; C >= 60; D >= 50; F < 50.
- PASS: every subject mark is at least 40 and attendance is at least 75%.
- Assignment percentage is stored in the dataset but does not affect the current pass/fail rule.

## Output
The `output/` folder contains two CSV reports and three PNG charts. All data is fictional and intended for an educational assignment.
