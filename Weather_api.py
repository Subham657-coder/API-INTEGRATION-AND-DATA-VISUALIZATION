import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Replace with your actual API key
API_KEY = "73312c239cd9434a933161631250607"
CITY = "Kolkata"

# --- API Request ---
url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=7&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()

# --- Extract Forecast Data ---
dates = []
temps = []
humidity = []

forecast_days = data['forecast']['forecastday']

for day in forecast_days:
    date = day['date']
    avg_temp = day['day']['avgtemp_c']
    avg_humidity = day['day']['avghumidity']

    dates.append(datetime.strptime(date, "%Y-%m-%d").strftime('%a %d'))
    temps.append(avg_temp)
    humidity.append(avg_humidity)

# --- Plotting ---
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker='o', label='Avg Temp (°C)', color='orange')
plt.plot(dates, humidity, marker='o', label='Avg Humidity (%)', color='blue')
plt.title(f"7-Day Weather Forecast - {CITY}")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
