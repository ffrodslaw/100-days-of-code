# Day 38: Workout tracker using natural language processing and Google Sheets

import requests
import datetime
import os

# change to your info
MY_APP_ID = ""
MY_KEY = ""
SHEETY_ENDPOINT = ""
SHEETY_TOKEN = ""

header = {
    "x-app-id": MY_APP_ID,
    "x-app-key": MY_KEY,
    "x-remote-user-id": "0",
}

text_input = input("What was your workout? ").lower()

date = datetime.datetime.now().date()
time = datetime.datetime.now().time().strftime("%H:%M:%S")


nutritionix_params = {
    "query": text_input

}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(nutritionix_endpoint, json=nutritionix_params, headers=header)
response.raise_for_status()


exercise_response = response.json()["exercises"]

sheety_header = {
    "authorization": "Bearer hfhdidisjvjjeghhehgejf3339",
}

for workout in exercise_response:
    exercise_input = {
        "workouts": {
            "date": str(date),
            "time": str(time),
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]
        }
    }


    sheet_response = requests.post(SHEETY_ENDPOINT, exercise_input, headers=sheety_header)

    print(sheet_response.text)

