import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# 1. Page Configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# 2. Load the trained model safely using robust relative paths
@st.cache_resource
def load_model():
    try:
        base_dir = Path(__file__).resolve().parent.parent
        model_path = base_dir / "models" / "best_model.pkl"
        
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'best_model.pkl' is inside the 'models' folder.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

model = load_model()

# 3. Application UI and Input Forms
st.title("🏠 Real Estate Price Predictor")
st.markdown("Enter the property details below to get an instant price estimate powered by our Gradient Boosting model.")

st.header("Property Features")

# Layout using columns for a cleaner interface
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=1500, step=100)
    bedrooms = st.selectbox("Bedrooms", options=[1, 2, 3, 4, 5, 6], index=2)
    bathrooms = st.selectbox("Bathrooms", options=[1, 2, 3, 4], index=1)
    
with col2:
    age = st.number_input("Property Age (years)", min_value=0, max_value=100, value=10, step=1)
    location = st.selectbox("Location", options=["Rural", "Suburb", "City Center"])
    property_type = st.selectbox("Property Type", options=["House", "Villa", "Apartment"])

# 4. Prediction Execution
if st.button("Predict Price", type="primary"):
    if model:
        # Construct the DataFrame exactly as the preprocessor expects it
        input_data = pd.DataFrame({
            "Area": [area],
            "Bedrooms": [bedrooms],
            "Bathrooms": [bathrooms],
            "Age": [age],
            "Location": [location],
            "Property_Type": [property_type]
        })
        
        try:
            # Execute inference
            prediction = model.predict(input_data)[0]
            
            # Display results beautifully
            st.success("Prediction Generated Successfully!")
            st.metric(label="Estimated Property Value", value=f"₹{prediction:,.2f}")
            
            st.info("💡 **Model Insight:** Our benchmark analysis determined that total Area and City Center locations hold the strongest predictive weight for this valuation.")
        except Exception as e:
            st.error(f"Prediction failed during inference: {e}")
    else:
        st.warning("The predictive model is offline. Please check system logs.")