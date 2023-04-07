import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

today = datetime.now()
today = str(today)

DATE = today.split(" ")[0]
TIME = today.split(" ")[1].split(".")[0]
APP_ID = "ENTER_NUTRITIONIX_APP_ID"
APP_KEY = "ENTER_NUTRITIONIX_APP_KEY"
AUTH = HTTPBasicAuth('USERNAME', 'ACCESS_TOKEN')

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
ADD_ROW_ENDPOINT = "https://api.sheety.co/5853f4f76eee6f21faec8de507c024e4/myWorkoutTracker/workouts"

exercise_text = input("Tell me which Exercise you did?")

User_data = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
Request_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=User_data, headers=Request_header)
response.raise_for_status()
result = response.json()

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=ADD_ROW_ENDPOINT, json=sheet_input, auth=AUTH)
    response.raise_for_status()
    print(response.json())
