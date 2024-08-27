import requests
import smtplib

email = 'EMAIL HERE'
password =  'EMAIL API PASSWORD HERE'

api_key = "b903617802f7f965510325560ce6d8cf"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 29.563690,
    "lon": -95.286179,
    "appid": api_key,
    "cnt": 4
}

OWM_Data = requests.get(url=OWM_Endpoint, params=weather_params)
OWM_Data.raise_for_status()
weather_data = OWM_Data.json()
# print(weather_data["list"])

will_rain = False

for hour_data in weather_data["list"]:
    if [hour_data][0]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = email, password=password)
        connection.sendmail(from_addr=email, to_addrs="TO EMAIL HERE", msg ="Subject:Bring an Umbrella \n\nIt's going to rain today.")

print("Done")