import requests
from datetime import datetime



today = datetime.now()
# print(today.strftime("%Y%m%d"))


GENDER = "Male"
WEIGHT_KG = "60"
HEIGHT_CM = "130"
AGE = "21"

APP_ID = "c22e45fa"
API_KEY = "cd92e465c4aacd825b7787bb5aa5cc40"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://docs.google.com/spreadsheets/d/1xMOT25uLpdscKqqVlFzuwF-v8Bq8-DOKgjzlZjWa8HU/edit?usp=sharing"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
# gfdsgdsf

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