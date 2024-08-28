# Sales-Data-Pipeline-Project
move data from csv to postgresql and do sum anlysis (in short)

Project Documentation: Pizza Sales Data Analysis
1. Project Overview
1.1 Objective
The goal of this project is to analyze a dataset of pizza sales to gain insights into sales trends, identify popular pizza categories, and understand sales patterns over time. This analysis will help in making informed business decisions and optimizing sales strategies.

1.2 Dataset
Source: Pizza Sales Dataset
Description: The dataset contains information about pizza sales, including order details, pizza categories, and pricing.
Columns:
pizza_id (integer): Unique identifier for each pizza.
order_id (integer): Unique identifier for each order.
pizza_name_id (string): Identifier for the pizza name.
quantity (integer): Number of pizzas ordered.
order_date (date): Date when the order was placed.
order_time (time): Time when the order was placed.
unit_price (float): Price per pizza.
total_price (float): Total price for the order.
pizza_size (string): Size of the pizza.
pizza_category (string): Category of the pizza.
pizza_ingredients (text): Ingredients used in the pizza.
pizza_name (string): Name of the pizza.
2. Data Loading and Preparation
2.1 Data Loading
The data was loaded from a CSV file into a PostgreSQL database. The table structure was created with appropriate data types to match the CSV data.

2.2 Data Preparation
Table Creation:
sql:

CREATE TABLE pizza_sales (
    pizza_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    pizza_name_id VARCHAR,
    quantity INTEGER,
    order_date DATE,
    order_time TIME,
    unit_price NUMERIC,
    total_price NUMERIC,
    pizza_size VARCHAR(50),
    pizza_category VARCHAR(50),
    pizza_ingredients TEXT,
    pizza_name VARCHAR(100)
);
Data Insertion: Data from the CSV file was inserted into the PostgreSQL table.
3. Data Exploration
3.1 Summary Statistics
Total Sales by Pizza Category:
sql:

SELECT pizza_category, SUM(total_price) AS total_sales
FROM pizza_sales
GROUP BY pizza_category
ORDER BY total_sales DESC;
Number of Orders Per Day:
sql:

SELECT order_date, COUNT(*) AS num_orders
FROM pizza_sales
GROUP BY order_date
ORDER BY order_date;
3.2 Data Quality Check
Missing Values:
sql:

SELECT COUNT(*) - COUNT(order_date) AS missing_order_date
FROM pizza_sales;
4. Data Analysis
4.1 Analysis with SQL
Total Sales by Pizza Category:

sql:

SELECT pizza_category, SUM(total_price) AS total_sales
FROM pizza_sales
GROUP BY pizza_category
ORDER BY total_sales DESC;
Number of Orders Per Day:

sql:

SELECT order_date, COUNT(*) AS num_orders
FROM pizza_sales
GROUP BY order_date
ORDER BY order_date;
4.2 Analysis with Python
Total Sales by Pizza Category:

python:

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="your_database_name",
    user="postgres",
    password="your_password"
) (*)

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM pizza_sales", conn)

# Close the connection
conn.close()

# Total sales by pizza category
sales_by_category = df.groupby('pizza_category')['total_price'].sum().sort_values(ascending=False)
sales_by_category.plot(kind='bar')
plt.title('Total Sales by Pizza Category')
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.show()
Sales Over Time:

python:

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Sales over time
sales_over_time = df.groupby('order_date')['total_price'].sum()
sales_over_time.plot(kind='line')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()
5. Data Visualization
5.1 Visualizations
Total Sales by Pizza Category:
A bar chart showing the total sales for each pizza category.
Sales Over Time:
A line chart showing sales trends over time.
6. Insights and Recommendations
6.1 Key Insights
Popular Pizza Categories: Identify the pizza categories with the highest total sales.

Sales Trends: Analyze sales trends over time to identify peak sales periods and any seasonal patterns.



*(For safety reasons I gave some of the data a general name of what should be put(
