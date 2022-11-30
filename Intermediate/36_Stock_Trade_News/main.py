import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# TODO: Provide API KEYS, AUTH TOKEN AND SID
STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
closing_price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(closing_price_difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = (closing_price_difference / float(yesterday_closing_price)) * 100
print(difference_percentage)

# If TODO4 percentage is greater than 5 then print("Get News").
if difference_percentage > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

## STEP 2: https://newsapi.org/

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# See line 44-52

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python to send a separate message with each article's title and description to your phone number.

# Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

# Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
# TODO: Provide Twilio phone number and destination phone number
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="",
        to=""
    )
