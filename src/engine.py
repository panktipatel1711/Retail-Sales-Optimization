import numpy as np
from scipy.stats import norm

def calculate_inventory_logic(forecast_sales, std_dev, lead_time=7, service_level=0.95):
    # Z-score for 95% service level
    z = norm.ppf(service_level)
    
    # Safety Stock calculation
    safety_stock = z * std_dev * np.sqrt(lead_time)
    
    # Reorder Point (ROP)
    rop = forecast_sales + safety_stock
    
    return {
        "safety_stock": round(safety_stock, 0),
        "reorder_point": round(rop, 0)
    }