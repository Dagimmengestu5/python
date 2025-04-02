import requests


stock_name = "IBM"
company_name = "Tesla Inc"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_api_key = "5U39QU3VE5WJN05T"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":stock_name,
    "interval":"1 min",
    "apikey":stock_api_key
}
response = requests.get(stock_endpoint, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

difference = yesterday_closing_price - day_before_yesterday_closing_price

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()
#
# print(data)