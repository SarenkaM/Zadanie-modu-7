from faker import Faker
fake = Faker('pl_PL')
import random


class Movie:
    def __init__(self, title, year, species, number_of_plays):
        self.title = title
        self.year = year
        self.species = species
        self.number_of_plays = number_of_plays
    def play(self):
        self.number_of_plays +=1
    def __str__(self):
        return f'"{self.title} ({self.year})'
    def __repr__(self):
        return f'{self.title} {self.year} {self.species}{self.number_of_plays}'

class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __str__(self):
        return f'"{self.title} S{self.season}E{self.episode}"'
    def __repr__(self):
        return f'{self.title} {self.year} {self.species} {self.number_of_plays} {self.season} {self.episode}'





def get_movies(lista):
    for i in lista:
        if type(i) == Movie:
            lista_movie.append(i)
    lista1 = sorted(lista_movie, key=lambda movie: movie.title)
    return(lista1)


def get_series(lista):
    for i in lista:
        if type(i) == Series:
            lista_series.append(i)
    lista2 = sorted(lista_series, key=lambda series: series.title)
    return(lista2)


def search(lista):
    found = False
    x = input("Podaj szukany tytuł:")
    for i in lista:
        if x == i.title:
            found = True
    if found == True:
        print("Podany tytuł jest na liście")
    else:
        print("Podanego tytułu nie ma na liście")


def generate_views(lista):
    random.choice(lista).number_of_plays += random.choice(range(1, 101))


def generate_views_10():
    for i in range(11):
        generate_views(lista)


def top_titles(lista):
    amount = int(input("Podaj ilość tytułów:"))
    lista3 = sorted(lista, key=lambda movie: movie.number_of_plays, reverse=True)
    print(lista3[0:amount])


if __name__ == "__main__":
    game_of_thrones = Series(title="Game of Thrones", year=2010, species="fantasy", number_of_plays=10, episode=2,
                             season=2)
    prison_break = Series(title="Prison Break", year=2004, species="criminal", number_of_plays=15, episode=10,
                          season=13)
    harry_potter = Movie(title="Harry Potter", year=2005, species="fantasy", number_of_plays=100)
    lord_of_rings = Movie(title="The Lord of the Rings", year=2000, species="fantasy", number_of_plays=150)
    lista = [game_of_thrones, prison_break, harry_potter, lord_of_rings]
    lista_movie = []
    lista_series = []

print(lista)


generate_views(lista)
generate_views_10()
print(get_movies(lista))
print(get_series(lista))
print(game_of_thrones.number_of_plays)
print(prison_break.number_of_plays)
print(lord_of_rings.number_of_plays)
print(harry_potter.number_of_plays)
search(lista)
top_titles(lista)