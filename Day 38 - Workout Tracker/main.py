import requests
from datetime import datetime
import os

APP_ID = "NUTRIONIX APP ID"
APP_KEY = "NUTRITIONIX APP KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 183
AGE = 19

SHEETY_ENDPOINT = "SHEET END_POINT HERE"


query = input("Please enter what you did: ")

headers = {
    'x-app-id': APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

exercises = result["exercises"]

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")


for item in exercises:
    calories = item["nf_calories"]
    duration = item["duration_min"]
    exercise = item['name'].title()
    
    headers = {
        "Authorization": "SHEET AUTHORIZATION HERE"
    }
    sheet_input = {
    "workout" : {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
    }

    response = requests.post(SHEETY_ENDPOINT, json=sheet_input, headers=headers)
    response.raise_for_status()