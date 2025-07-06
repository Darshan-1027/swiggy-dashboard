import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("swiggy_orders.csv")
df.columns = df.columns.str.strip()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Streamlit App Title
st.title("🍽️ Swiggy Orders Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Orders")
cities = st.sidebar.multiselect("Select Cities:", options=df["City"].unique(), default=df["City"].unique())
foods = st.sidebar.multiselect("Select Food Items:", options=df["Food"].unique(), default=df["Food"].unique())

# Apply Filters
filtered_df = df[(df["City"].isin(cities)) & (df["Food"].isin(foods))]

# KPIs (Big Numbers)
st.subheader("📊 Key Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{filtered_df['Price'].sum():,.0f}")
col2.metric("Avg Delivery Time", f"{filtered_df['DeliveryTime'].mean():.1f} min")
col3.metric("Total Orders", len(filtered_df))

# Revenue by City - Bar Chart
st.subheader("🏙️ Revenue by City")
rev_by_city = filtered_df.groupby("City")["Price"].sum()
st.bar_chart(rev_by_city)

# Top Foods - Pie Chart
st.subheader("🍕 Most Ordered Foods")
top_foods = filtered_df["Food"].value_counts().head(5)
fig1, ax1 = plt.subplots()
ax1.pie(top_foods, labels=top_foods.index, autopct="%1.1f%%", startangle=90)
st.pyplot(fig1)

# Payment Method Distribution
st.subheader("💳 Payment Method Share")
payment = filtered_df["PaymentMethod"].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(payment, labels=payment.index, autopct="%1.1f%%", startangle=90)
st.pyplot(fig2)

# Show filtered data
with st.expander("🔎 See Raw Data"):
    st.dataframe(filtered_df)
