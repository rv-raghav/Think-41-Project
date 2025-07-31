import sqlite3
import pandas as pd

# Load CSV
df = pd.read_csv("data/products.csv")

# Add index as 'id' if not exists
if 'id' not in df.columns:
    df.reset_index(inplace=True)
    df.rename(columns={"index": "id"}, inplace=True)

# Connect to SQLite DB
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Create table with 'id' column
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    description TEXT
)
""")

# Clear table before inserting (optional)
cursor.execute("DELETE FROM products")

# Insert rows
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO products (id, name, category, price, description)
    VALUES (?, ?, ?, ?, ?)
    """, (row["id"], row["name"], row["category"], row["price"], row["description"]))

conn.commit()
print(f"Inserted {len(df)} rows.")
conn.close()
