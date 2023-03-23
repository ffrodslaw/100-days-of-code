# Day 47: Amazon Price Tracker

import requests
from bs4 import BeautifulSoup
import smtplib
import os

# # change these environmental variables, the link to the product, and below which price you want to be notified
my_email = os.getenv("GMAIL_USER")
email_pw = os.getenv("GMAIL_PASSWORD")
email_to = os.getenv("GMAIL_USER")
product_link = "https://www.amazon.com/dp/B0BP6GMQ8S"
price_threshold = 15

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Defined",
}

response = requests.get(product_link, headers=header).text
soup = BeautifulSoup(response, "lxml")

title = soup.title.get_text()
price = float(soup.find("span", class_="a-offscreen").get_text().replace("$", ""))

if price < price_threshold:
    email_text = f"Subject: Amazon price alert!\n\nThe item {title} is now only ${price}.\nGet it here: {product_link}"
    email_encoded = email_text.encode("utf-8")
    print(email_encoded)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_to,
            msg=email_encoded)
