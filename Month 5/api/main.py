"""
API: main.py
Description: FastAPI service to serve the trained LSTM time-series model.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = FastAPI(title="Supermarket Sales Forecaster API")

# Load artifacts using absolute paths
model_path = "models/lstm_sales_model.h5"
scaler_path = "models/sales_scaler.pkl"

try:
    model = load_model(model_path)
    scaler = joblib.load(scaler_path)
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")

class SalesInput(BaseModel):
    past_7_days_sales: list[float]

@app.post("/predict")
def predict_sales(data: SalesInput):
    if len(data.past_7_days_sales) != 7:
        raise HTTPException(status_code=400, detail="Must provide exactly 7 days of sales data.")
    
    try:
        input_array = np.array(data.past_7_days_sales).reshape(-1, 1)
        scaled_input = scaler.transform(input_array)
        lstm_input = scaled_input.reshape(1, 7, 1)
        scaled_prediction = model.predict(lstm_input)
        final_prediction = scaler.inverse_transform(scaled_prediction)
        return {"next_day_forecast": round(float(final_prediction[0][0]), 2)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}