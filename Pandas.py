import pandas as pd

# Load the data
df = pd.read_csv("swiggy_orders.csv")

# View first 5 rows
# print(df.head())

# View columns
# print("Columns:", df.columns)

# Rows and columns count
# print("Shape:", df.shape)

# Info about data
# print(df.info())


print(df["Price"].sum())

print(df["Price"].mean())

print(df["Price"].max())

print(df["Price"].min())

count = df.columns
print(len(count))

print(df["City"].unique())

