#### Scraping top 100 movies list from empire.com
# saves output in movies.txt


from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text)

titles = soup.select(".gallery .title")

titles_list = [movie.get_text() for movie in reversed(titles)]

with open(file="movies.txt", mode="w") as output:
    output.write("\n".join(titles_list))