import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(page_title="📊 Paytm Business Dashboard", layout="wide")

st.title("🚀 Paytm Business Dashboard")

# --- KPI Section ---
st.subheader("📌 Key Highlights")
col1, col2, col3, col4 = st.columns(4)
col1.metric("UPI Share (Jan '25)", "6.87%", "↓0.01%")
col2.metric("Revenue (Q3 FY25)", "₹1828 Cr", "+10.1%")
col3.metric("Net Income (Q3 FY25)", "-₹208 Cr", "↓123.4%")
col4.metric("GMV (Q3 FY25)", "₹4.90 L Cr", "+9.6%")

st.markdown("---")

# --- Competition Analysis ---
st.header("🆚 UPI Market Share Comparison")
col1, col2 = st.columns(2)

with col1:
    competition_data = {
        'Competitor': ['PhonePe', 'Google Pay', 'Paytm'],
        'Jan 2025': [0.48, 0.37, 0.0687],
        'Dec 2024': [0.477, 0.367, 0.0688]
    }
    df_comp = pd.DataFrame(competition_data).set_index('Competitor')
    st.dataframe(df_comp.style.format("{:.1%}").highlight_max(axis=0), use_container_width=True)

with col2:
    fig = px.bar(df_comp.T, barmode='group', title="UPI Market Share by Month")
    fig.update_layout(xaxis_title="Month", yaxis_title="Market Share")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Financial Performance ---
st.header("📈 Financial Performance")
financial_data = {
    'Quarter': ['Q4 FY24', 'Q1 FY25', 'Q2 FY25', 'Q3 FY25'],
    'Revenue': [2267, 1502, 1660, 1828],
    'Net Income': [-550, -840, 930, -208]
}
df_fin = pd.DataFrame(financial_data)

metric = st.selectbox("Select Financial Metric:", ['Revenue', 'Net Income'])
fig = px.line(df_fin, x='Quarter', y=metric, markers=True, title=f"{metric} Trend Over Quarters")
fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Transaction Metrics ---
st.header("💳 Transaction Metrics - Gross Merchandise Value")
transaction_data = {
    'Quarter': ['Q3 FY24', 'Q4 FY24', 'Q1 FY25', 'Q2 FY25', 'Q3 FY25'],
    'GMV (Lakh Cr)': [5.10, 4.69, 4.26, 4.47, 4.90]
}
df_trans = pd.DataFrame(transaction_data)

fig = px.area(df_trans, x='Quarter', y='GMV (Lakh Cr)', title="GMV Trend", markers=True)
fig.update_layout(yaxis_title="₹ in Lakh Cr")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- User Metrics ---
st.header("👥 Monthly Transacting Users (MTU)")
user_data = {
    'Period': ['FY24', 'Q1 FY25', 'Q2 FY25', 'Q3 FY25'],
    'MTU (Cr)': [9.6, 7.8, 7.1, 7.2]
}
df_user = pd.DataFrame(user_data)

fig = px.line(df_user, x='Period', y='MTU (Cr)', title="MTU Over Time", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Business Segments ---
st.header("📊 Revenue by Business Segments")
segment_data = {
    'Segment': ['Payments', 'Lending', 'Marketing', 'Financial'],
    'FY24': [6235, 52390, 1738, 2004],
    'Q3 FY25': [1059, 5577, 267, 502]
}
df_seg = pd.DataFrame(segment_data)

fig = px.bar(df_seg, x='Segment', y=['FY24', 'Q3 FY25'], 
             title="Revenue by Segment Comparison", barmode='group',
             labels={"value": "Revenue (₹ Cr)", "variable": "Period"})
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- Stock Performance ---
st.header("📉 Paytm Stock Price Trend")
stock_data = {
    'Date': ['2024-04-30', '2024-07-31', '2024-10-31', '2024-12-31', '2025-03-31'],
    'Close': [365.5, 476.2, 862.5, 1007.85, 777.4]
}
df_stock = pd.DataFrame(stock_data)

fig = px.line(df_stock, x='Date', y='Close', title="Stock Closing Price", markers=True)
fig.update_traces(line_color='orange', line_width=3)
st.plotly_chart(fig, use_container_width=True)

# --- Download Option ---
st.download_button("📥 Download Financial Data (CSV)", df_fin.to_csv(index=False), file_name="Paytm_Financials.csv")

# --- Styling ---
st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 22px;
    font-weight: bold;
    color: #1a73e8;
}
h1, h2, h3 {
    color: #14213d;
}
</style>
""", unsafe_allow_html=True)
