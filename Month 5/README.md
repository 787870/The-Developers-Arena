# Supermarket Sales Forecasting & Automated API

An end-to-end Machine Learning and MLOps project focusing on time-series forecasting. This repository contains data exploration notebooks, a trained Long Short-Term Memory (LSTM) neural network model, a production-ready FastAPI backend, and containerized deployment infrastructure using Docker.

---

## 📁 Repository Structure

```text
Month 5/
│
├── api/
│   └── main.py                         # FastAPI application
│
├── data/
│   ├── customer_churn.csv              # Supplementary dataset
│   └── supermarket_sales.csv           # Historical transaction dataset
│
├── docs/
│   └── Project Report.pdf              # Project documentation
│
├── models/
│   ├── lstm_sales_model.h5             # Trained LSTM model
│   └── sales_scaler.pkl                # MinMaxScaler artifact
│
├── notebooks/
│   ├── 01_time_series_exploration.ipynb
│   └── 02_lstm_forecasting.ipynb
│
├── Dockerfile
└── requirements.txt
```

---

## 🚀 Key Features & Workflow

1. **Exploratory Data Analysis (EDA):** Aggregated transactional records into a daily time series and evaluated stationarity using the Augmented Dickey-Fuller (ADF) test.

2. **Deep Learning Model:** Developed and trained an LSTM neural network over 50 epochs to capture sequential daily sales patterns.

3. **Production FastAPI Service:** Implemented a REST API with automatic request validation using Pydantic schemas and a `POST /predict` endpoint for next-day sales forecasting.

4. **Containerized Deployment:** Used Docker to containerize the application, ensuring consistent execution across local and cloud environments.

---

## 🛠️ Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/787870/The-Developers-Arena.git

cd "The-Developers-Arena/Month 5"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API Locally

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Access the API documentation:

http://127.0.0.1:8000/docs

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t supermarket-sales-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 supermarket-sales-api
```

Access the application:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

---

## 🔌 API Usage Example

### Endpoint

```http
POST /predict
```

### Request Body

```json
{
  "past_7_days_sales": [
    1200.5,
    1350.2,
    1100.0,
    1420.8,
    1500.3,
    1650.0,
    1300.9
  ]
}
```

### Example Response

```json
{
  "next_day_forecast": 1389.56
}
```

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Jupyter Notebook

---

## 📊 Documentation

For detailed information about the problem statement, methodology, model architecture, implementation, evaluation, and business impact, refer to:

[`Project Report.pdf`](docs/Project%20Report.pdf)

---

## 👨‍💻 Author

**A. Mohammed Aslam**

MCA Graduate | Data Analytics & Machine Learning Enthusiast

**GitHub:** https://github.com/787870

**Portfolio:** https://web-starter-kit--mohammedaslam87.replit.app

---

⭐ If you find this project interesting, consider giving the repository a star!
