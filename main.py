import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from src.engine import calculate_inventory_policy
import joblib

# 1. Synthetic Data Generation (Simulation) [cite: 156]
def generate_data():
    dates = pd.date_range(start="2024-01-01", periods=365, freq='D')
    data = pd.DataFrame({
        'date': dates,
        'item_id': 1,
        'store_id': 101,
        'qty_sold': np.random.randint(10, 50, size=365) + np.sin(np.linspace(0, 10, 365)) * 10
    })
    return data

# 2. Feature Engineering [cite: 437, 587]
def prepare_features(df):
    df = df.copy()
    df['day_of_week'] = df['date'].dt.dayofweek
    df['lag_1'] = df['qty_sold'].shift(1)
    df['roll_mean_7'] = df['qty_sold'].shift(1).rolling(7).mean()
    return df.dropna()

# 3. Training & Forecasting
df = generate_data()
df_feat = prepare_features(df)

X = df_feat[['day_of_week', 'lag_1', 'roll_mean_7']]
y = df_feat['qty_sold']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y) # [cite: 603]

# 4. Inventory Recommendation [cite: 617]
latest_data = X.tail(1)
forecast_next_7_days = model.predict(latest_data)[0] * 7
resid_std = np.std(y - model.predict(X))

recommendation = calculate_inventory_policy(
    forecast_sum=forecast_next_7_days,
    resid_std=resid_std,
    on_hand=50,
    lead_time=7
)

print("--- Retail System Output ---")
print(f"Inventory Strategy: {recommendation}")