import requests
from datetime import datetime

latitude = -32.9575
longitude = -60.6394

url = (
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    "&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=auto"
)

weather_map = {
    0: "Despejado", 1: "Principalmente despejado",
    2: "Parcialmente nublado", 3: "Nublado", 45: "Niebla",
    48: "Niebla con escarcha", 51: "Llovizna ligera",
    53: "Llovizna moderada", 55: "Llovizna intensa",
    61: "Lluvia ligera", 63: "Lluvia moderada",
    65: "Lluvia intensa", 66: "Lluvia helada ligera",
    67: "Lluvia helada intensa", 71: "Nieve ligera",
    73: "Nieve moderada", 75: "Nieve intensa",
    77: "Granos de nieve", 80: "Chubascos ligeros",
    81: "Chubascos moderados", 82: "Chubascos violentos",
    95: "Tormenta ligera o moderada",
    96: "Tormenta con granizo ligero",
    99: "Tormenta con granizo fuerte"
}

print("Cargando datos del clima actual...")
res = requests.get(url)

if res.status_code != 200:
    print(f"Error al cargar los datos: {res.status_code}")
    exit()

data = res.json()
current = data["current"]

print(f"Fecha y hora: {datetime.now()}")
print(f"Temperatura: {current['temperature_2m']} °C")
print(f"Humedad: {current['relative_humidity_2m']}%")
print(f"Estado del cielo: {weather_map[current['weather_code']]}")
print(f"Viento: {current['wind_speed_10m']} km/h")