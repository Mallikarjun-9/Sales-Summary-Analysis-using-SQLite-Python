import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Create or connect to the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# STEP 2: Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# STEP 3: Insert 15+ entries
sample_data = [
    ('Apple', 10, 2.5),
    ('Banana', 5, 1.2),
    ('Apple', 7, 2.5),
    ('Banana', 3, 1.2),
    ('Orange', 8, 3.0),
    ('Grapes', 12, 2.0),
    ('Mango', 15, 4.5),
    ('Apple', 6, 2.5),
    ('Pineapple', 4, 5.0),
    ('Mango', 10, 4.5),
    ('Orange', 6, 3.0),
    ('Banana', 7, 1.2),
    ('Grapes', 10, 2.0),
    ('Apple', 5, 2.5),
    ('Watermelon', 2, 7.0),
    ('Pomegranate', 3, 6.0),
    ('Mango', 4, 4.5)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()

# STEP 4: Run SQL query to summarize sales
query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

df = pd.read_sql_query(query, conn)

# STEP 5: Display results
print("===== Sales Summary =====")
print(df)

# STEP 6: Plot revenue by product
plt.figure(figsize=(10,6))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()

# STEP 7: Save and show the plot
plt.savefig("sales_chart.png")
plt.show()

# STEP 8: Close connection
conn.close()
