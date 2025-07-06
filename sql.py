import pandas as pd
import sqlite3

df = pd.read_csv("swiggy_cleaned.csv")

print(df)

conn = sqlite3.connect(":memory:")

df.to_sql("orders", conn,  if_exists="replace")

result = pd.read_sql_query("SELECT * FROM orders", conn)
print(result)

query1 = "SELECT * FROM orders WHERE City = 'Mumbai'"
print(pd.read_sql_query(query1, conn))

query2 = "SELECT SUM(Price) AS Total_Revenue FROM orders"
print(pd.read_sql_query(query2, conn))

