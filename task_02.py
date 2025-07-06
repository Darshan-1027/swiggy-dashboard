import pandas as pd

df = pd.read_csv("swiggy_orders.csv")

print(df)

Mumbai_Orders = df[df["City"]=="Mumbai"]

print(Mumbai_Orders)

print(df[df["Price"]>=200])

Biryani_orders = df[df["Food"]=="Biryani"]

print(Biryani_orders)

print(df[(df["City"]=="Delhi") & (df["Food"]=="Pizza")])

sorted_by_price = df.sort_values(by="Price", ascending=False)
print(sorted_by_price)

dt = df.sort_values(by="DeliveryTime")
print(dt)

