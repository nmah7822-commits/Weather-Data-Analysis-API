# ️ Weather Data Analysis + API

> **A comprehensive data analysis project that extracts actionable climate insights from historical weather data and serves them via a high-performance FastAPI backend.**

---

## 📋 Overview
This project analyzes historical weather data to uncover temperature trends, rainfall patterns, and seasonal variations. Beyond just generating statistical insights and visualizations, it integrates a **FastAPI** backend to make these data-driven insights accessible via RESTful API endpoints.

---

## 🎯 Problem Statement
Raw weather data is often massive and difficult to interpret manually. Decision-makers in agriculture, logistics, and urban planning need quick, automated access to specific climate metrics (like monsoon rainfall or temperature extremes) without manually processing CSV files. This project solves this by automating the analysis and exposing it through an API.

---

## 📊 Dataset
- **Source:** Historical weather records (`weather_data.csv`).
- **Features:** 
  - `Date`: Daily timestamps.
  - `Temperature_C`: Daily temperature in Celsius.
  - `Rainfall_mm`: Daily rainfall in millimeters.

---

## 🛠️ Tools and Technologies

| Category | Technologies Used |
| :--- | :--- |
| **Data Manipulation** | Python, Pandas, NumPy |
| **Data Visualization** | Matplotlib |
| **Backend & API** | FastAPI, Uvicorn |
| **Environment** | VS Code, Jupyter/Python Script |

---

## 🔬 Methods
1. **Data Preprocessing:** Loaded the CSV using Pandas, converted date strings to datetime objects, and extracted 'Month' and 'Year' features for time-series analysis.
2. **Statistical Analysis:** Calculated monthly average temperatures, identified hottest/coldest months, computed total yearly rainfall, and measured temperature variability using standard deviation (NumPy).
3. **Seasonal Analysis:** Filtered data specifically for Monsoon months (July, August, September) to calculate average rainfall.
4. **Visualization:** Generated clear, publication-ready PNG charts for daily trends, monthly averages, and yearly rainfall.
5. **API Integration:** Wrapped the core logic in FastAPI to serve analysis results dynamically.

---

## 💡 Key Insights
- **Temperature Extremes:** Successfully identified the hottest and coldest months based on historical averages.
- **Monsoon Impact:** Calculated the precise average rainfall during the critical Jul-Sep monsoon window.
- **Climate Variability:** Used standard deviation to measure how much daily temperatures fluctuate throughout the year.

---

## 📊 Dashboard / Output (Visualizations)
The project automatically generates the following analytical charts:
- 📈 `daily_temp_trend.png`: Daily temperature fluctuations.
- 📊 `monthly_avg_temp.png`: Month-wise average temperature bar chart.
- 🌧️ `monthly_rainfall.png`: Monthly rainfall distribution.
- 📉 `yearly_rainfall.png`: Year-over-year total rainfall comparison.

---

## ⚙️ How to Run this Project

### 1. Clone the Repository
```bash
git clone <https://github.com/nmah7822-commits/Weather-Data-Analysis-API>
cd Weather-Data-Analysis-API

👩‍💻 Author & Contact
[Mah Noor]
Email: [nmah7822@gmail.com]
LinkedIn: [https://www.linkedin.com/in/mahnoor14]
🐙 GitHub: [github.com/nmah7822-commits]