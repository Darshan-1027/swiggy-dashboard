import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("swiggy_orders.csv")

# Total revenue per city
revenue = df.groupby("City")["Price"].sum()


revenue.plot(kind="bar", color="orange", title="Total Revenue by City")
plt.xlabel("City")
plt.ylabel("Total Revenue (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()


payment_share = df["PaymentMethod"].value_counts()

payment_share.plot(kind="pie", autopct="%1.1f%%", startangle=90, title="Payment Method Share")
plt.ylabel("")  # Hides y-axis label
plt.tight_layout()
plt.show()


plt.plot(df["OrderID"], df["DeliveryTime"], marker="o", color="green")
plt.title("Delivery Time per Order")
plt.xlabel("Order ID")
plt.ylabel("Minutes")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.hist(df["DeliveryTime"], bins=5, color="purple", edgecolor="black")
plt.title("Delivery Time Distribution")
plt.xlabel("Time (min)")
plt.ylabel("Number of Orders")
plt.grid(True)
plt.tight_layout()
plt.show()

