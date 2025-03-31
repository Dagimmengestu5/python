import requests



owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "860c0060a78cf87e04e6fbb4d9901fde"
parameters = {
    "lat":8.980603,
    "lon": 38.757759,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}


response = requests.get(url=owm_endpoint, params=parameters)
# response.raise_for_status()
print(response.json())

