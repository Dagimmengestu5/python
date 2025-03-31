import requests



owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "694ca15c7440a3505d402bc51b4e3b89"
parameters = {
    "lat":8.980603,
    "lon": 38.757759,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}


response = requests.get(url=owm_endpoint, params=parameters)
# response.raise_for_status()
print(response.json())

