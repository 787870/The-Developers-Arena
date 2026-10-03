import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_and_split_data(filepath, target_col="Price", test_size=0.2, random_state=42):
    """Loads data, drops unnecessary ID columns, and splits into train/test sets."""
    try:
        df = pd.read_csv(filepath)
        
        if "Property_ID" in df.columns:
            df = df.drop("Property_ID", axis=1)
            
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        
        # Split before preprocessing
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        return X_train, X_test, y_train, y_test
        
    except Exception as e:
        print(f"Error loading and splitting data: {e}")
        return None, None, None, None

def build_preprocessor():
    """Builds a scikit-learn ColumnTransformer for numerical and categorical scaling."""
    numeric_features = ["Area", "Bedrooms", "Bathrooms", "Age"]
    categorical_features = ["Location", "Property_Type"]
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features)
        ],
        remainder="passthrough"
    )
    
    return preprocessor

if __name__ == "__main__":
    import os
    from pathlib import Path
    
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "house_prices.csv"
    
    X_train, X_test, y_train, y_test = load_and_split_data(data_path)
    
    if X_train is not None:
        preprocessor = build_preprocessor()
        X_train_processed = preprocessor.fit_transform(X_train)
        
        print("SUCCESS: Data Preprocessing Module is working!")
        print(f"Original Training Shape: {X_train.shape}")
        print(f"Processed Training Shape: {X_train_processed.shape}")