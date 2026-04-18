import pandas as pd
import numpy as np
import os

def generate_retail_dataset():
    """
    Generates a synthetic retail sales dataset with trend, 
    seasonality, and noise for forecasting.
    """
    print("Starting Data Generation Process...")

    # Create 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Created directory: /data")

    # Parameters for simulation
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=500, freq='D')
    
    # Simulating Business Logic:
    # 1. Base demand (150 units)
    # 2. Seasonality (Sales go up and down in cycles)
    # 3. Trend (Slight growth over time)
    # 4. Noise (Random daily fluctuations)
    base_demand = 150
    time_index = np.linspace(0, 20, 500)
    seasonality = 40 * np.sin(time_index)
    trend = 0.05 * np.arange(500)
    noise = np.random.normal(0, 12, 500)
    
    sales = (base_demand + seasonality + trend + noise).astype(int)

    # Creating the DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Product_ID': 'SKU_101',
        'Sales': sales,
        'Stock_On_Hand': np.random.randint(50, 200, size=500),
        'Price': 19.99
    })

    # Save to CSV
    file_path = 'data/raw_sales_data.csv'
    df.to_csv(file_path, index=False)
    
    print(f"Successfully generated dataset at: {file_path}")
    print(f"Total Rows: {len(df)}")

if __name__ == "__main__":
    generate_retail_dataset()