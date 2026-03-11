import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="RetailPulse Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 RetailPulse – Demand Forecast & Inventory Dashboard")
st.markdown("Data-driven retail demand forecasting and inventory optimization")

# Sidebar
st.sidebar.title("RetailPulse")
st.sidebar.markdown("""
Demand Forecasting System

Model Used:  
SARIMA Time-Series Model

Category:  
Office Supplies
""")

# Load data
forecast = pd.read_csv("outputs/forecasts/office_supplies_12_month_forecast.csv")
inventory = pd.read_csv("outputs/inventory_policy_office_supplies.csv")

# Convert date column
forecast["Month"] = pd.to_datetime(forecast["Month"])

# KPIs
total_forecast = int(forecast["Forecasted_Quantity"].sum())
avg_forecast = int(forecast["Forecasted_Quantity"].mean())
max_month = forecast.loc[forecast["Forecasted_Quantity"].idxmax(), "Month"]

st.subheader("📊 Forecast Summary")

k1, k2, k3 = st.columns(3)

k1.metric("Total Forecasted Demand", f"{total_forecast:,}")
k2.metric("Average Monthly Demand", f"{avg_forecast:,}")
k3.metric("Peak Demand Month", max_month.strftime("%b %Y"))

st.divider()

# Tables
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔮 12-Month Demand Forecast")
    st.dataframe(forecast)

with col2:
    st.subheader("📦 Inventory Recommendation")
    st.dataframe(inventory)

st.divider()

# Forecast chart
st.subheader("📈 Forecast Visualization")

fig, ax = plt.subplots()

ax.plot(
    forecast["Month"],
    forecast["Forecasted_Quantity"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Forecasted Quantity")
ax.set_title("Office Supplies Demand Forecast")

plt.xticks(rotation=45)

st.pyplot(fig)

st.divider()

# Insights
st.subheader("📊 Key Insights")

peak_month = forecast.loc[forecast["Forecasted_Quantity"].idxmax(), "Month"]
low_month = forecast.loc[forecast["Forecasted_Quantity"].idxmin(), "Month"]

st.markdown(f"""
• Highest forecasted demand occurs in **{peak_month.strftime('%B %Y')}**.

• Lowest demand is expected in **{low_month.strftime('%B %Y')}**.

• Demand shows **seasonal variation**, highlighting the need for adaptive inventory planning.

• RetailPulse forecasts help businesses **optimize inventory levels and improve supply chain planning**.
""")