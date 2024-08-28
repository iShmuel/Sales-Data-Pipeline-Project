import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="273322"
)
cursor = conn.cursor()

# Query the data
cursor.execute("SELECT * FROM pizza_sales LIMIT 10;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# -- Get summary statistics for numerical columns
cursor.execute("SELECT MIN(total_price) AS min_price,MAX(total_price) AS max_price,AVG(total_price) AS avg_price FROM pizza_sales;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")

# -- Get counts of unique values in categorical columns
cursor.execute("SELECT pizza_category, COUNT(*) FROM pizza_sales GROUP BY pizza_category;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")

# -- Count missing values for each column
cursor.execute("SELECT SUM(CASE WHEN pizza_name IS NULL THEN 1 ELSE 0 END) AS missing_pizza_name,SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS missing_order_date FROM pizza_sales;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")

# -- Total sales by pizza category
cursor.execute("SELECT pizza_category, SUM(total_price) AS total_sales FROM pizza_sales GROUP BY pizza_category ORDER BY total_sales DESC")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")

# -- Number of orders per day
cursor.execute("SELECT order_date, COUNT(*) AS num_orders FROM pizza_sales GROUP BY order_date ORDER BY order_date;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")

# --must selling pizza category 
cursor.execute("SELECT MAX(pizza_category) AS must_category FROM pizza_sales;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

print("---------------------")


# Close the connection
cursor.close()
conn.close()
