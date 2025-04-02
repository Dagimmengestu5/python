import requests
from twilio.twiml.voice_response import Client

stock_name = "IBM"
company_name = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_api_key = "636CZK2WMH502P3H"
news_api_key = "2952fc05f75a49cf8382cebf4a82b844"
twilio_api_key = "bb5ccdd367b9aa706aa945f5ba0f9045"
twilio_auth_token = "34efc98698085985ef4aa560ee7217ab"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":stock_name,
    "interval":"1 min",
    "apikey":stock_api_key
}
response = requests.get(stock_endpoint, params=stock_parameters)
print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
up_down = 0
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percentage = round(difference / yesterday_closing_price) * 100
print(diff_percentage)

if abs(diff_percentage) < 5:
    new_parms = {
        "apiKey":news_api_key,
        "qInTitle":company_name
    }
    new_response = requests.get(news_endpoint, params=new_parms)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]
    formated_articles = [f"{stock_name}: {up_down}{diff_percentage}% headline: {articles['title']}. \nBrif: {articles['disecription']}" for articles in three_articles]
    client = Client(twilio_api_key, twilio_auth_token)
    for articles in formated_articles:
        message = client.messages.create(
            body=articles,
            from_= "+17753108424",
            to = "+251901933879"
        )




    print(three_articles)



# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()
#
# print(data)