import requests


stock_name = "BNB"
company_name = "bitget"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
stock_api_key = "5U39QU3VE5WJN05T"

stock_parameters = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol":stock_name,
    "interval":"1 min",
    "apikey":stock_api_key
}
response = requests.get(stock_endpoint, params=stock_parameters)
print(response.json())