# Day 36: Stock news text automation

# This app sends text message with the three latest news articles on a stock if the stock
# has changed by over 5% between the day before yesterday and yesterday (limitation from the used API).

import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

###### Change all constants to your personal ones:
STOCK_KEY = ""
NEWS_KEY = ""
TWILIO_SID = ""
TWILIO_TOKEN = ""
VERIFIED_NUMBER =""

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

stock = response.json()["Time Series (Daily)"]

# get yesterday and day before's dates as strings
date_yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
date_before_yesterday = str(datetime.date.today() - datetime.timedelta(days=2))

stock_yesterday = float(stock[date_yesterday]["4. close"])
stock_before_yesterday = float(stock[date_before_yesterday]["4. close"])

# absolute value of stock change
stock_diff = (stock_yesterday - stock_before_yesterday) / stock_before_yesterday * 100

# send sms messages if stock changes more than 5%:
# message includes stock price change and the three latest articles on the company
if abs(stock_diff) > 1:

    news_parameters = {
        "q": STOCK,
        "from": date_before_yesterday,
        "sortBy": "popularity",
        "apiKey": NEWS_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news = response.json()["articles"][:3]

    top_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news]

    for article in top_articles:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages \
        .create(
            body=f"{STOCK}: {round(stock_diff)} \n{article}",
            from_="+18888405814",
            to=VERIFIED_NUMBER
        )
        print(message.status)
