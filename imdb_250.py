import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Please enter a rating: "))

names = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for name,rating in zip(names,ratings):
    name = name.text
    rating = rating.text
    name = name.strip()
    name = name.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating)) >= a:
        print("Film: {} Rating: {}".format(name,rating))

