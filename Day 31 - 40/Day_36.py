import requests
from twilio.rest import Client

stock_name = "IBM"
company_name = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_api_key = "636CZK2WMH502P3H"
news_api_key = "2952fc05f75a49cf8382cebf4a82b844"
twilio_sid = "AC9b6e88c1237a005d35b8aa0f58000488"
twilio_auth_token = "34efc98698085985ef4aa560ee7217ab"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": stock_api_key
}
response = requests.get(stock_endpoint, params=stock_parameters)
response.raise_for_status()  # Added to handle potential HTTP errors

data = response.json().get("Time Series (Daily)")
if not data:  # Added to handle cases where there is no data
    raise ValueError("No stock data found.")

data_list = [value for (key, value) in data.items()]
if len(data_list) < 2:  # Added to handle cases where there is insufficient data
    raise ValueError("Not enough data available to calculate differences.")

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
up_down = "⬆️" if yesterday_closing_price > day_before_yesterday_closing_price else "⬇️"

diff_percentage = round((difference / yesterday_closing_price) * 100, 2)

if abs(diff_percentage) >= 5:  # Corrected from < 5 to >= 5 to match logical trigger
    new_parms = {
        "apiKey": news_api_key,
        "qInTitle": company_name
    }
    new_response = requests.get(news_endpoint, params=new_parms)
    new_response.raise_for_status()  # Added to handle potential HTTP errors

    articles = new_response.json().get("articles", [])
    if not articles:  # Added to handle cases where no articles are found
        raise ValueError("No news articles found.")

    three_articles = articles[:3]
    formatted_articles = [
        f"{stock_name}: {up_down}{diff_percentage}% headline: {article.get('title', 'No title available')}. "
        f"\nBrief: {article.get('description', 'No description available')}" for article in three_articles
    ]
    client = Client(twilio_sid, twilio_auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17753108424",
            to="+251923330363"
        )
