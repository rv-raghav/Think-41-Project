import pandas as pd
print(pd.__version__)
import sqlite3

# Step 1: Load and analyze the CSV
csv_path = r"D:\Think-41-Project\products.csv"
df = pd.read_csv(csv_path)
print("Data preview:\n", df.head())
print("\nColumn info:\n", df.dtypes)

# Step 2: Create SQLite database and table
conn = sqlite3.connect("products.db")  # Creates SQLite DB file
cursor = conn.cursor()

# Generate CREATE TABLE statement based on CSV column types
# Customize data types if needed
column_defs = []
for col, dtype in zip(df.columns, df.dtypes):
    if pd.api.types.is_integer_dtype(dtype):
        col_type = "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        col_type = "REAL"
    else:
        col_type = "TEXT"
    column_defs.append(f'"{col}" {col_type}')

create_table_sql = f"""
CREATE TABLE IF NOT EXISTS products (
    {', '.join(column_defs)}
);
"""

cursor.execute(create_table_sql)
conn.commit()

# Step 3: Load data into the table
df.to_sql("products", conn, if_exists="append", index=False)

# Step 4: Verify the data
print("\nSample rows from the database:")
for row in cursor.execute("SELECT * FROM products LIMIT 5"):
    print(row)

# Cleanup
conn.close()
