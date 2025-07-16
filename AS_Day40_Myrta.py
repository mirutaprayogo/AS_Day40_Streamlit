import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt

st.title("📦 RFM Analysis - Know Your Customer")

df = pd.read_csv("Sample - Superstore.csv", encoding='ISO-8859-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])

st.subheader("📄 Preview Data")
st.dataframe(df[['Customer Name', 'Order Date', 'Sales']].head())

# Hitung RFM
NOW = dt.datetime(2018, 1, 1)  # Tanggal acuan
rfm = df.groupby('Customer Name').agg({
    'Order Date': lambda x: (NOW - x.max()).days,
    'Customer Name': 'count',
    'Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']
rfm.reset_index(inplace=True)

st.subheader("📊 Tabel RFM")
st.dataframe(rfm)

# Visualisasi interaktif
st.subheader("🟢 Scatter Plot Recency vs Frequency")
fig = px.scatter(rfm, x='Recency', y='Frequency', size='Monetary', color='Monetary',
                 hover_data=['Customer Name'],
                 title='Recency vs Frequency (RFM Analysis)')
st.plotly_chart(fig)