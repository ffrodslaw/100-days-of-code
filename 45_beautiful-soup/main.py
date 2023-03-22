from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)

# print(soup.prettify())

# get all anchor tags
tags = soup.find_all(name="a")
print(tags)

for tag in tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")  # use find for first, find_all for all matches
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

print(soup.select(".heading"))