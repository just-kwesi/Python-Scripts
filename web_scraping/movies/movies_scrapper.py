import requests
from bs4 import BeautifulSoup
from pprint import pprint

site_data = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(site_data.text,"lxml")

movies = soup.find_all(name="h3",class_="title")
movies_list = [movie.getText() for movie in movies]

with open("web_scraping/movies/movies.txt", "w") as movies_file:
    for index in range(99,-1,-1):
        movie = movies_list[index]
        movies_file.write(f"{movie}\n")