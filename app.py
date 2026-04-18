import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
import joblib
import os
from src.engine import calculate_inventory_logic

# --- PAGE CONFIGURATION (Professional Look) ---
st.set_page_config(
    page_title="Retail Inventory Pro | Decision Support System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL DARK THEME CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* KPI Card Styling */
    div[data-testid="metric-container"] {
        background-color: #1e2129;
        border: 1px solid #3d4450;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    [data-testid="stMetricValue"] { color: #00d4ff !important; font-size: 2rem !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #bdc3c7 !important; font-size: 1rem !important; }
    
    /* Sidebar Styling */
    .css-1d391kg { background-color: #161b22; }
    
    /* Table Header Fix */
    thead tr th { background-color: #1e2129 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("📊 Retail Sales Forecasting & Inventory Optimization")
st.markdown("##### *Advanced Predictive Analytics for Supply Chain Efficiency*")
st.markdown("---")

# --- 1. DATA INGESTION ---
@st.cache_data
def load_and_process_data():
    # If data setup was run, load that CSV. Otherwise, generate on-the-fly.
    if os.path.exists('data/raw_sales_data.csv'):
        df = pd.read_csv('data/raw_sales_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        dates = pd.date_range(start="2023-01-01", periods=250, freq='D')
        sales = (150 + 40 * np.sin(np.linspace(0, 10, 250)) + np.random.normal(0, 12, 250)).astype(int)
        df = pd.DataFrame({'Date': dates, 'Sales': sales})
    return df

df = load_and_process_data()

# --- 2. EXECUTIVE SUMMARY (KPIs) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Volume", f"{df['Sales'].sum():,}", help="Cumulative sales units")
with col2:
    st.metric("Avg Daily Sales", f"{int(df['Sales'].mean())}")
with col3:
    st.metric("Peak Demand", f"{df['Sales'].max()}")
with col4:
    st.metric("Demand Volatility", f"{round(df['Sales'].std(), 1)} σ")

st.markdown("###")

# --- 3. ML FORECASTING ENGINE ---
# Feature Engineering
df['Day_of_Week'] = df['Date'].dt.dayofweek
df['Lag_1'] = df['Sales'].shift(1)
df_model = df.dropna()

X = df_model[['Day_of_Week', 'Lag_1']]
y = df_model['Sales']

# Training the Model
model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)

# Save the model to /models folder (Professional Practice)
if not os.path.exists('models'): os.makedirs('models')
joblib.dump(model, 'models/sales_model.pkl')

# Multi-step Forecast (Next 7 Days)
last_date = df['Date'].iloc[-1]
last_qty = df['Sales'].iloc[-1]
forecast_values = []
curr_qty = last_qty

for i in range(1, 8):
    next_day_idx = (last_date.dayofweek + i) % 7
    pred = model.predict([[next_day_idx, curr_qty]])[0]
    forecast_values.append(pred)
    curr_qty = pred

# --- 4. DATA VISUALIZATION (PRO CHARTS) ---
st.subheader("📈 Demand Intelligence: Historical vs Forecast")
fig = go.Figure()

# Historical Trace
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Sales'], 
    name='Historical Sales', 
    line=dict(color='#00d4ff', width=2),
    fill='tozeroy', fillcolor='rgba(0, 212, 255, 0.1)'
))

# Forecast Trace
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)
fig.add_trace(go.Scatter(
    x=future_dates, y=forecast_values, 
    name='7-Day ML Forecast', 
    line=dict(color='#ff4b4b', width=3, dash='dash')
))

fig.update_layout(
    template="plotly_dark", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    hovermode="x unified", 
    height=450,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
st.plotly_chart(fig, use_container_width=True)

# --- 5. INVENTORY OPTIMIZATION & DECISION TABLE ---
st.markdown("---")
st.subheader("📋 Inventory Replenishment Decision Support")

# Calculate using engine.py logic
inv_res = calculate_inventory_logic(sum(forecast_values), df['Sales'].std())

# Simulated Product Database for Professional look
inventory_plan = {
    "SKU ID": ["SKU-A101", "SKU-B202", "SKU-C303", "SKU-D404"],
    "Product": ["Organic Milk", "Whole Grain Bread", "Unsalted Butter", "Large Eggs (12pk)"],
    "Current Stock": [45, 120, 25, 210],
    "Forecasted Demand": [int(sum(forecast_values)), 410, 85, 150],
    "Safety Stock": [int(inv_res['safety_stock']), 40, 15, 30],
    "Status": ["Critical", "Healthy", "Reorder Now", "Overstock"]
}

plan_df = pd.DataFrame(inventory_plan)

def style_status(val):
    colors = {
        'Critical': 'color: #ff4b4b; font-weight: bold',
        'Reorder Now': 'color: #f39c12; font-weight: bold',
        'Healthy': 'color: #28a745; font-weight: bold',
        'Overstock': 'color: #3498db; font-weight: bold'
    }
    return colors.get(val, '')

# Display Table with Mapping (Fixed Version)
st.dataframe(plan_df.style.map(style_status, subset=['Status']), use_container_width=True)

# --- SIDEBAR (DEVELOPER BRANDING) ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=100)
st.sidebar.title("System Control")
st.sidebar.markdown("---")

st.sidebar.header("⚙️ Model Parameters")
st.sidebar.info("**Algorithm:** Random Forest Regressor\n\n**Service Level:** 95%\n\n**Forecast Horizon:** 7 Days")

st.sidebar.markdown("---")
st.sidebar.header("👨‍💻 Developer Information")
st.sidebar.write("**Name:** PANKTI PATEL")
st.sidebar.markdown("---")
st.sidebar.caption("Retail Smart Inventory v1.2.0 | © 2026")