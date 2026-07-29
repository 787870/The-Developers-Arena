# 📊 Month 2: Multi-Domain Data Analysis & Visualization Portfolio

A comprehensive data analysis, statistical modeling, and visualization portfolio built as part of **The Developers Arena Internship — Month 2 Capstone**. 

This folder contains **5 end-to-end data analysis projects** spanning multiple real-world domains (Retail, Real Estate, Weather, Healthcare, and Finance). Every project demonstrates data manipulation with `pandas`, statistical hypothesis evaluation, and interactive visual storytelling with `matplotlib` and `seaborn`.

---

## 📁 Repository Contents

| File / Folder | Description |
| :--- | :--- |
| **`project1_supermarket.ipynb`** | **Retail Domain:** Supermarket sales patterns, best-selling product lines, and revenue trend analysis. |
| **`project2_house_prices.ipynb`** | **Real Estate Domain:** Property feature correlations, square footage impact, and location-based price valuations. |
| **`project3_weather.ipynb`** | **Weather Domain:** Annual meteorological study covering temperature waves, rainfall distributions, and humidity cycles. |
| **`project4_healthcare.ipynb`** | **Healthcare Domain:** COVID-19 infection tracking, patient recovery rate monitoring, and hospital capacity loads. |
| **`project5_finance.ipynb`** | **Finance Domain:** Stock market equity analysis, 20-Day/50-Day Moving Average crossovers, and volume momentum. |
| **`supermarket_sales.csv`** | Cleaned dataset used for Project 1 retail analysis (2,000 transaction records). |
| **`house_prices.csv`** | Cleaned dataset used for Project 2 real estate valuation analysis (300 property listings). |

*(Note: Datasets for Projects 3, 4, and 5 are dynamically simulated and loaded directly within their respective notebooks via reproducible Python scripts.)*

---

## 🏆 Project Summaries & Key Findings

### 1️⃣ Retail Domain: Supermarket Sales Analysis (`project1_supermarket.ipynb`)
* **Objective:** Analyze daily sales patterns, identify high-margin product categories, and evaluate customer spending behavior.
* **Key Insights:**
  * **Electronics** dominated turnover, generating **34.1% (₹4.25M)** of total revenue with a **45% profit margin**.
  * Weekend promotional discounts boosted sales volume by **~40%** compared to weekday averages.
  * Customer foot traffic peaked during evening hours (**5:00 PM – 7:00 PM**), accounting for over **60%** of daily revenue.

### 2️⃣ Real Estate Domain: Housing Valuation Analysis (`project2_house_prices.ipynb`)
* **Objective:** Determine the primary structural and geographic drivers of residential property valuations.
* **Key Insights:**
  * Property square footage (`Area`) is the single strongest predictor of market price, showing an **r = 0.80 positive correlation**.
  * **City Center** properties command a **35–45% price premium** per square foot over comparable rural homes.
  * Property age shows a slight negative depreciation impact (**r = -0.13**).

### 3️⃣ Weather Domain: Annual Climate Study (`project3_weather.ipynb`)
* **Objective:** Track annual seasonal temperature trends, rainfall distribution patterns, and extreme weather events.
* **Key Insights:**
  * Documented a clear mid-year sinusoidal temperature peak reaching up to **39.2°C**.
  * Heavy precipitation events (>20 mm/day) consistently drove average relative humidity above **85%**.
  * Outlier monsoon downpours exceeding **100 mm/day** were identified via statistical distribution checks.

### 4️⃣ Healthcare Domain: COVID-19 Patient Tracking (`project4_healthcare.ipynb`)
* **Objective:** Evaluate daily infection rates, patient recovery resilience, and hospital inpatient capacity loads.
* **Key Insights:**
  * Confirmed an **88%–95% overall patient recovery rate**, with daily recoveries tracking infections closely (**r = 0.81**).
  * Daily case counts correlated strongly with inpatient hospitalizations (**r = 0.82**), validating capacity forecasting models.
  * Hospital admissions experienced a seasonal surge during **August (~85 average daily beds)**.

### 5️⃣ Finance Domain: Quantitative Equity Analysis (`project5_finance.ipynb`)
* **Objective:** Analyze equity price trends, moving average crossover signals, daily return volatility, and trading volume momentum.
* **Key Insights:**
  * Identified a sustained Q3/Q4 bullish breakout confirmed by a **Golden Cross (20-Day SMA crossing above 50-Day SMA)**.
  * Daily percentage returns followed a symmetrical normal distribution centered at a **+0.08% daily mean**.
  * High-volume trading surges (**>3.0M monthly shares**) confirmed structural price breakouts.

---

## 🛠️ Technical Stack & Methodology

* **Language:** Python 3.10+
* **Data Manipulation (`pandas`, `numpy`):**
  * Vectorized filtering and aggregation (`groupby`, `reindex`)
  * Time-series feature engineering (`dt.strftime`, frequency indexing)
  * Simple Moving Averages (`rolling(window=...).mean()`)
* **Statistical Analysis (`scipy`, `numpy`):**
  * Pearson correlation matrices and statistical hypothesis checks
  * Normal distribution fitting and outlier detection via Interquartile Ranges (IQR)
* **Data Visualization (`matplotlib`, `seaborn`):**
  * Consistent executive-grade palettes (`Set2`, `Blues`, `Reds`, `Purples`)
  * Annotated baselines, explicit grid styling, and automated image saving

---

## 🚀 How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/787870/The-Developers-Arena.git
   cd "The-Developers-Arena/Month 2"

2. **Install Required Python Dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyterlab

3. **Launch Jupyter Lab / Notebook:**
   ```bash
   jupyter lab
