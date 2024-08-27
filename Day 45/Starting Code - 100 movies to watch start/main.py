import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

title_div = soup.find_all(name = "div", class_="article-title-description__text")
titles = [title.find(name = "h3") for title in title_div]
titles_text = [title.text for title in titles]

for i in range(len(titles_text)):
    titles_text[i] = titles_text[i] + "\n"

titles_text = titles_text[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines(titles_text)

print("Done")