# 🛒 Retail Sales Forecasting & Inventory Optimization System

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)

This is a high-performance **Predictive Analytics Dashboard** that transforms raw retail data into inventory intelligence. It uses Machine Learning to forecast demand and automate stock replenishment.

---

## 📸 Project Visualizations (Direct View)

### 1 Executive Summary & Business KPIs
Real-time tracking of Total Units, Average Demand, and Sales Volatility.
![KPI Dashboard](demo_ss1.png)

### 2 ML-Powered Demand Forecasting
7-day predictive window visualized with interactive Plotly charts.
![Forecasting Logic](demo_ss2.png)

### 3 Inventory Replenishment Plan
Automated decision table with color-coded alerts for SKU management.
![Inventory Table](demo_ss3.png)

### 4 Feature Engineering Logic
Testing lag features for the ML model
![Engineering Logic](Sales Distribution by Day of Week.PNG)

## 5 Visualizing Sales Trends
Daily Sales Trend
![Visualizing Sales Trends](Daily Sales Trend.PNG)

## 6 Load Data & Basic Stats
Load the data
![load data](load_data.PNG)

---

## 🌟 Key Features
- **Predictive Intelligence:** 7-Day sales forecasting using Random Forest Regressor.
- **Inventory Engine:** Automated Safety Stock and Reorder Point (ROP) calculations.
- **Professional UX:** High-contrast dark-themed dashboard for high data readability.
- **Data Research:** Dedicated Jupyter notebook for deep-dive EDA.

---

## 📁 Project Architecture
```text
Retail_Project/
├── app.py              # Main Dashboard (Streamlit UI)
├── data_setup.py       # Dataset Generator script
├── demo_ss1.png        # Screenshot 1 (Main Folder)
├── demo_ss2.png        # Screenshot 2 (Main Folder)
├── demo_ss3.png        # Screenshot 3 (Main Folder)
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
├── data/               # Source: raw_sales_data.csv
├── models/             # Serialized ML models (.pkl)
└── notebooks/          # Exploratory Data Analysis (.ipynb)
