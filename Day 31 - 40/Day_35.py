import requests



owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "bb5ccdd367b9aa706aa945f5ba0f9045"
parameters = {
    "lat":25.325665,
    "lon": -20.321556,
    "appid": "bb5ccdd367b9aa706aa945f5ba0f9045",
    "exclude":"current,minutely,daily"
}


response = requests.get(url=owm_endpoint, params=parameters)
# response.raise_for_status()
whether = response.json()
print(whether)
input("Press enter to exitSGDFF and SDFAASDF")
# I DONT HAVE UNDERSTAND FDGHJDFGHJGH CXGHDGH

