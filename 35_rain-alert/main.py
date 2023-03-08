# Day 35: Rain alert message

import requests
import os
from twilio.rest import Client

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "ACe4ee1d2748ee1ef3c12998f0f9797816"
auth_token = "05695802c33d3f32b3816f226aedc89f"

parameters = {
    "appid": api_key,
    "lat": 43.156578,
    "lon": -77.608849,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

next_12_hours = weather_data["hourly"][:12]


def extract_code(hour):
    hour_codes = []
    for i in range(len(hour["weather"])):
        hour_code = int(hour["weather"][i]["id"])
        hour_codes.append(hour_code)
    return hour_codes


codes = []
for hour in range(11):
    code = extract_code(next_12_hours[hour])
    codes.extend(code)


will_it_rain = True in (code < 700 for code in codes)

# send a message from twilio

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18888405814",
        to="verified twilio number"
    )
    print(message.status)


