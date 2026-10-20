import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# إعدادات الصفحة
st.set_page_config(page_title="Weekly Sustainability Dashboard", layout="centered")

# Create the dataset
data = {
    "Day": [
        "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"
    ],
    "Electricity": [850, 920, 780, 950, 880, 600, 550],
    "Water": [420, 450, 390, 470, 430, 300, 280],
    "Waste": [35, 40, 30, 45, 38, 25, 20]
}

df = pd.DataFrame(data)

# Dashboard title
st.markdown("<h1 style='text-align:center; color:#176B87;'>Weekly Sustainability Dashboard</h1>", unsafe_allow_html=True)

# Summary cards (Metrics)
col1, col2, col3 = st.columns(3)
col1.metric("Electricity (kWh)", f"{df['Electricity'].sum():,}")
col2.metric("Water", f"{df['Water'].sum():,}")
col3.metric("Waste", f"{df['Waste'].sum():,}")

st.write("---")

# Create charts
st.subheader("Weekly Electricity Consumption")
fig1, ax1 = plt.subplots(figsize=(8, 3))
ax1.bar(df["Day"], df["Electricity"], color="#176B87")
ax1.set_ylabel("Electricity (kWh)")
ax1.tick_params(axis="x", rotation=45)
ax1.grid(axis="y", alpha=0.3)
st.pyplot(fig1)

st.subheader("Weekly Water Consumption")
fig2, ax2 = plt.subplots(figsize=(8, 3))
ax2.bar(df["Day"], df["Water"], color="#2E8B57")
ax2.set_ylabel("Water Consumption")
ax2.tick_params(axis="x", rotation=45)
ax2.grid(axis="y", alpha=0.3)
st.pyplot(fig2)

st.subheader("Weekly Waste Generation")
fig3, ax3 = plt.subplots(figsize=(8, 3))
ax3.bar(df["Day"], df["Waste"], color="#CD853F")
ax3.set_ylabel("Waste Quantity")
ax3.tick_params(axis="x", rotation=45)
ax3.grid(axis="y", alpha=0.3)
st.pyplot(fig3)

st.write("---")

# Show data table
st.subheader("Data Table")
st.dataframe(df, use_container_width=True)
