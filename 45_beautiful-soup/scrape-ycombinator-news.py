from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(response, "html.parser")

# print(soup.title)

articles = soup.select(".titleline a")

articles_texts = []
articles_links = []

for article in articles:
    title = article.get_text()
    link = article.get("href")
    articles_texts.append(title)
    articles_links.append(link)

