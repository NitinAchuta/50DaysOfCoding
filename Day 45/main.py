from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")
title_span = soup.find_all("span", class_="titleline")
title_link = title_span.find_all("a")
title = title_link.text
print(title)

upvotes_span = soup.find_all(name="span", class_="subline")
upvotes = upvotes_span.find_all(class_="score")
print(upvotes.text)


with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# #For text
# tags = [tag.getText() for tag in all_anchor_tags]
# print(tags)

# href = [tag.get("href") for tag in all_anchor_tags]
# print(f"\n{href}\n") 

# heading = soup.find(name="h1", id="name")
# print(heading.string)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)



headings = soup.select(selector=".heading")
print(headings)