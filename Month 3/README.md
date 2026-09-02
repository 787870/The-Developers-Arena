# 🌦️ Month 3: Complete Weather Data Pipeline System

**Objective:** Build an end-to-end ETL (Extract, Transform, Load) data pipeline that fetches live weather API data, cleans it using Pandas, and stores it in a relational SQLite database for querying and visualization.

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **Data Extraction:** `requests` (REST API Web Scraping)
* **Data Transformation:** `pandas` (JSON flattening, data type conversion)
* **Database Management:** `sqlite3` (SQL table creation, insertion, and querying)
* **Visualization:** `matplotlib`, `seaborn`

## 🏗️ Pipeline Architecture
1. **Extract:** Fetched live, hourly temperature and precipitation data for New York City using the Open-Meteo API (No API Key Required).
2. **Transform:** Parsed the nested JSON payload and converted it into a structured Pandas DataFrame.
3. **Load:** Initialized a local `weather.db` SQLite database and programmatically inserted the DataFrame into a new `nyc_weather` SQL table.
4. **Analysis:** Executed SQL `SELECT` queries to retrieve 48-hour data blocks for time-series visualization.

## 🚀 How to Run Locally

**1. Install Dependencies**
Ensure you have the required libraries installed:
`pip install pandas requests matplotlib seaborn jupyterlab`

**2. Execute the Pipeline**
Open the `weather_etl_pipeline.ipynb` notebook and select **Run > Run All Cells**. 
The script will automatically:
* Pull the latest live weather data.
* Generate the `weather.db` database file in your directory.
* Display the 48-hour temperature forecast chart.
