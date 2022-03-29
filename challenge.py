from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3",class_="title")]
movies.reverse()
# tambien se puede con movies[::-1]

with open("movies.txt", 'w') as f_obj:
    for movie in movies:
        f_obj.write(f"{movie}\n")




