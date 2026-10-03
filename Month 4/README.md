# Month 4: End-to-End Machine Learning Real Estate Price Predictor

## 📌 Project Overview
This project fulfills the Month 4 Capstone requirements for The Developers Arena internship. It is a complete, production-ready machine learning system designed to predict real estate prices based on property features. The architecture strictly adheres to professional code hygiene, modular design, and robust data validation principles.

## ⚙️ Setup Instructions
1. **Clone the repository** and navigate to the `Month 4` directory.
2. **Install dependencies**: `pip install pandas numpy scikit-learn streamlit`
3. **Run the Preprocessing & Training Pipeline**:
   python src/model_training.py
4. **Launch the Web Interface**:
   streamlit run app/app.py

## 📁 Code Structure
The project abandons monolithic Jupyter notebooks in favor of a modular, production-ready hierarchy:
* `data/`: Contains the raw `house_prices.csv` dataset.
* `notebooks/`: Contains `01_exploratory_data_analysis.ipynb` for EDA and correlation matrix visualization.
* `src/`: 
  * `data_preprocessing.py`: Handles data loading, leakage-free train/test splitting, and `ColumnTransformer` scaling/encoding.
  * `model_training.py`: Executes multi-model benchmarking and pipeline serialization.
* `models/`: Stores the serialized `best_model.pkl` artifact.
* `app/`: Contains `app.py`, the interactive Streamlit prediction frontend.
* `tests/`: Contains `test_pipeline.py` (built with `unittest`) to validate data shape and pipeline integrity.

## 🔬 Technical Details & Methodology
* **Exploratory Data Analysis:** Pearson correlation revealed `Area` as the strongest numerical predictor (r = 0.80). Scatter plot visualizations confirmed a strong location-based pricing premium (City Center > Suburb > Rural).
* **Data Preprocessing:** Implemented a Scikit-Learn `ColumnTransformer` using `StandardScaler` for numerical features and `OneHotEncoder` for categorical features. The dataset was strictly split (80/20) *before* transformations to eliminate data leakage.
* **Model Benchmarking:** Evaluated three distinct algorithms:
  1. Linear Regression (Baseline): R² = 0.941 | MAE = ₹2,188,736
  2. Random Forest Regressor: R² = 0.974 | MAE = ₹1,436,717
  3. **Gradient Boosting Regressor (Winner):** R² = 0.985 | MAE = ₹1,008,585
* **Deployment:** The winning Gradient Boosting pipeline was serialized via `pickle` and integrated into a Streamlit frontend for dynamic, real-time user predictions.

## ✅ Testing Evidence
A unit test suite (`tests/test_pipeline.py`) was implemented and successfully executed, verifying that the data loader properly drops identifiers (`Property_ID`), splits the 300 rows exactly into 240 train / 60 test subsets without data loss, and initializes the preprocessor correctly.