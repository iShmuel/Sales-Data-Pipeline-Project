import pandas as pd
import psycopg2

# Load the CSV file
file_path = r"D:\Sales Data Pipeline Project\pizza_sales.csv"
df = pd.read_csv(file_path)

# Convert date and time columns to appropriate types
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce').dt.date  # Convert to date, NaT for invalid
df['order_time'] = pd.to_datetime(df['order_time'], format='%H:%M:%S', errors='coerce').dt.time  # Convert to time, NaT for invalid

# Handle NaT values by replacing with a default value (or use 'dropna' to remove rows)
df['order_date'].fillna(pd.Timestamp('1900-01-01').date(), inplace=True)  # Replace NaT with default date
df['order_time'].fillna(pd.Timestamp('00:00:00').time(), inplace=True)  # Replace NaT with default time

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="273322"
)
cursor = conn.cursor()

# Insert data into the table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO pizza_sales (pizza_id, order_id, pizza_name_id, quantity, order_date, order_time, unit_price, total_price, pizza_size, pizza_category, pizza_ingredients, pizza_name)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['pizza_id'], row['order_id'], row['pizza_name_id'], row['quantity'], row['order_date'], row['order_time'],
        row['unit_price'], row['total_price'], row['pizza_size'], row['pizza_category'],
        row['pizza_ingredients'], row['pizza_name']
    ))

# Commit and close the connection
conn.commit()
cursor.close()
conn.close()
