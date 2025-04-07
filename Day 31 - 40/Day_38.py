

import requests
from datetime import datetime
import os

GENDER = "M"
WEIGHT_KG = 60
HEIGHT_CM = 150
AGE = 22

APP_ID = 'c22e45fa'
API_KEY = "cd92e465c4aacd825b7787bb5aa5cc40"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "1OVR03qEdWmybLi5bUl9P_wbPXWmIDbquYj7tDIb59e4"
# cgjhgcxcvbvcghjghj
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Auth
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["USERNAME"],
            os.environ["PASSWORD"],
        )
    )

    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
