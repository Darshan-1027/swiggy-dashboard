import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("swiggy_project.csv")

print(df)


# 1. Which city gives the most revenue?	Bar chart (groupby)

revanue = df.groupby("City")["Price"].sum()
print(revanue)

revanue.plot(

    kind="bar",
    title="Revenue Of Cities",
    xlabel="City",
    color="orange",
    ylabel="revanue",
)

plt.tight_layout()
plt.show()


# 2. Which 5 foods are ordered most?  Bar or Pie chart

food=df["Food"].value_counts().head(5)
print(food)



food.plot(kind="bar",color="red",title="most food order",xlabel="Foods",ylabel="Orders most")

plt.tight_layout()
plt.show()

food.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 3. What’s the average delivery time overall?	Just .mean()


Dt = df["DeliveryTime"].min()
print(f"📦 Average Delivery Time:{Dt} minutes")

# 4. Most used payment method?	Pie chart 

payment = df["PaymentMethod"].value_counts()

payment.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.show()

df.to_csv("swiggy_cleaned.csv", index=False)
