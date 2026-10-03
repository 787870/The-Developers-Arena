import pickle
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Import the clean, modular functions we just built!
from data_preprocessing import load_and_split_data, build_preprocessor

def train_and_evaluate():
    print("Initializing Model Training Pipeline...\n")
    
    # 1. Setup dynamic paths
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "house_prices.csv"
    model_dir = base_dir / "models"
    
    # 2. Load and split data using our module
    X_train, X_test, y_train, y_test = load_and_split_data(data_path)
    if X_train is None:
        return
        
    # 3. Get the preprocessor
    preprocessor = build_preprocessor()
    
    # 4. Define the 3 algorithms to compare (Requirement for Month 4)
    models = {
        "Linear Regression (Baseline)": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42)
    }
    
    best_r2 = -float("inf")
    best_model = None
    best_name = ""
    
    # 5. Train and evaluate each model in a loop
    for name, algorithm in models.items():
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("regressor", algorithm)
        ])
        
        # Train the model
        pipeline.fit(X_train, y_train)
        
        # Predict on the test set and evaluate
        y_pred = pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"--- {name} ---")
        print(f"Mean Absolute Error: ₹{mae:,.2f}")
        print(f"R² Score: {r2:.3f}\n")
        
        # Track the best model based on R2 Score
        if r2 > best_r2:
            best_r2 = r2
            best_model = pipeline
            best_name = name
            
    # 6. Save (Serialize) the winning model to the 'models' folder
    print(f"🏆 Winning Model: {best_name} with an R² of {best_r2:.3f}")
    
    model_path = model_dir / "best_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(best_model, f)
        
    print(f"✅ Model successfully saved to {model_path}")

if __name__ == "__main__":
    train_and_evaluate()