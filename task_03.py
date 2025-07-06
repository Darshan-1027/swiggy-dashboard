import pandas as pd

df = pd.read_csv("swiggy_orders.csv")

print(df)

revenue_by_city = df.groupby("City")["Price"].sum()
print(revenue_by_city)

avg_price_food = df.groupby("Food")["Price"].mean()
print(avg_price_food)

orders_by_food = df["Food"].value_counts()
print(orders_by_food)

avg_rating = df.groupby("City")["Rating"].mean()
print(avg_rating)

rev_city_food = df.groupby(["City", "Food"])["Price"].sum()
print(rev_city_food)


