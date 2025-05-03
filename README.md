# 🛒 Sales Summary Analysis using SQLite & Python

This project demonstrates how to extract, analyze, and visualize basic sales data using a **SQLite database**, **Python**, and **matplotlib**. It is part of the Data Analyst Internship tasks from Elevate Labs and MSME.

---

## 📌 Task Overview

**Objective:**  
Pull simple sales data (total quantity and revenue per product) from a SQLite database using SQL in Python, display the results using `print()` and visualize them with a basic bar chart.

---

## 📂 Project Structure

├── sales_data.db # SQLite database file (auto-created)
├── sales_analysis.py # Main Python script
├── sales_chart.png # Bar chart of revenue by product (auto-generated)
└── README.md # Project documentation

---

## 🔧 Tools & Libraries

- Python 3.x
- SQLite3 (built-in with Python)
- pandas
- matplotlib

Install required libraries using:


pip install pandas matplotlib

---

🚀 How to Run the Project
Clone or Download this repository.

Open a terminal or command prompt.

Run the script using:

python sales_analysis.py

The script will:

Create a SQLite database (sales_data.db)

Insert sample data into a sales table

Query sales summary (grouped by product)

Print the results to the console

Plot and save a bar chart as sales_chart.png

📈 Sample Output
📊 Terminal Output diff Copy Edit

===== Sales Summary =====
        product  total_qty  revenue
0         Apple         28     70.0
1        Banana         15     18.0
2        Grapes         22     44.0
3         Mango         29    130.5
4        Orange         14     42.0
5     Pineapple          4     20.0
6  Pomegranate          3     18.0
7   Watermelon          2     14.0

🖼️ Bar Chart
X-axis: Products

Y-axis: Total Revenue

File: sales_chart.png

🧠 Concepts Used
SQL (GROUP BY, SUM)

SQLite3 in Python

pandas for data manipulation

matplotlib for visualization



