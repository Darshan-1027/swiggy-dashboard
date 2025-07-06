import pandas as pd

df = pd.read_csv("dirty_orders.csv")

print(df)

df.columns = df.columns.str.strip()
print(df.columns)

print("Missing values per column:\n", df.isnull().sum())

df_clean = df.dropna()
print(df_clean)

df_clean = df_clean.drop_duplicates()
print(df_clean)

df_clean.rename(columns={"DeliveryTime": "TimeToDeliver"}, inplace=True)

# df.fillna({"Price": df["Price"].mean(), "Rating": df["Rating"].mean()}, inplace=True)


print(df_clean)