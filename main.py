import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI, HTTPException
from datetime import date
import os

# Data load karein
df = pd.read_csv("weather_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Basic info
print(df.describe())

# 1. Monthly average temperature
monthly_avg_temp = df.groupby("Month")["Temperature_C"].mean()
print("\nMonthly Average Temperature:\n", monthly_avg_temp)

# 2. Hottest and coldest month
hottest_month = monthly_avg_temp.idxmax()
coldest_month = monthly_avg_temp.idxmin()
print(f"\nHottest Month: {hottest_month} ({monthly_avg_temp.max():.1f}°C)")
print(f"Coldest Month: {coldest_month} ({monthly_avg_temp.min():.1f}°C)")

# 3. Total rainfall per year
yearly_rainfall = df.groupby("Year")["Rainfall_mm"].sum()
print("\nYearly Total Rainfall:\n", yearly_rainfall)

# 4. Monsoon months rainfall (July-Sept)
monsoon = df[df["Month"].isin([7, 8, 9])]
print(f"\nAverage Monsoon Rainfall (Jul-Sep): {monsoon['Rainfall_mm'].mean():.2f} mm")

# 5. NumPy se standard deviation (temperature variability)
temp_std = np.std(df["Temperature_C"])
print(f"\nTemperature Std Dev: {temp_std:.2f}°C")

# ---- GRAPHS ----

# Graph 1: Monthly Average Temperature
plt.figure(figsize=(8,5))
monthly_avg_temp.plot(kind="line", marker="o", color="orange")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_avg_temp.png")
plt.show()

# Graph 2: Yearly Rainfall
plt.figure(figsize=(6,5))
yearly_rainfall.plot(kind="bar", color="steelblue")
plt.title("Total Rainfall per Year")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("yearly_rainfall.png")
plt.show()

# Graph 3: Monthly Rainfall Pattern (all years combined)
monthly_rainfall = df.groupby("Month")["Rainfall_mm"].mean()
plt.figure(figsize=(8,5))
monthly_rainfall.plot(kind="bar", color="teal")
plt.title("Average Monthly Rainfall (Monsoon Pattern)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("monthly_rainfall.png")
plt.show()

# Graph 4: Temperature Trend Over Time
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Temperature_C"], alpha=0.5)
plt.title("Daily Temperature Trend (2022-2024)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("daily_temp_trend.png")
plt.show()

from fastapi import FastAPI, HTTPException
from datetime import date
import pandas as pd
import os

app = FastAPI(title="Weather Data API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "weather_data.csv")

df = pd.read_csv(CSV_FILE)
df["Date"] = pd.to_datetime(df["Date"])


@app.get("/")
def home():
    return {"message": "Weather Data API is running"}


# 1. Ek specific date ka data
@app.get("/weather/{date_str}")
def get_weather_by_date(date_str: str):
    day_data = df[df["Date"] == pd.to_datetime(date_str)]
    if day_data.empty:
        raise HTTPException(status_code=404, detail="No data found for this date")
    return day_data.to_dict(orient="records")[0]


# 2. Date range ka stats (average temp, total rainfall, etc.)
@app.get("/weather/range/{start_date}/{end_date}")
def get_weather_range(start_date: str, end_date: str):
    mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
    range_data = df[mask]

    if range_data.empty:
        raise HTTPException(status_code=404, detail="No data found in this range")

    return {
        "start_date": start_date,
        "end_date": end_date,
        "avg_temperature": round(range_data["Temperature_C"].mean(), 2),
        "total_rainfall": round(range_data["Rainfall_mm"].sum(), 2),
        "avg_humidity": round(range_data["Humidity_%"].mean(), 2),
        "avg_wind_speed": round(range_data["Wind_Speed_kmh"].mean(), 2)
    }


# 3. Monthly average temperature (for a given year)
@app.get("/weather/monthly-avg/{year}")
def monthly_avg(year: int):
    year_data = df[df["Date"].dt.year == year]
    if year_data.empty:
        raise HTTPException(status_code=404, detail="No data found for this year")

    monthly = year_data.groupby(year_data["Date"].dt.month)["Temperature_C"].mean().round(2)
    return monthly.to_dict()


# 4. Overall summary
@app.get("/weather/summary")
def overall_summary():
    return {
        "hottest_temp": df["Temperature_C"].max(),
        "coldest_temp": df["Temperature_C"].min(),
        "total_rainfall": round(df["Rainfall_mm"].sum(), 2),
        "avg_humidity": round(df["Humidity_%"].mean(), 2)
    }