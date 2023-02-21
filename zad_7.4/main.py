from faker import Faker
fake = Faker('pl_PL')
import random
lista = []

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



game_of_thrones = Series(title="Game of Thrones", year=2010, species="fantasy", number_of_plays=10, episode=2, season=2)
prison_break = Series(title="Prison Break", year=2004, species="criminal", number_of_plays=15, episode=10, season=13)
harry_potter = Movie(title="Harry Potter", year=2005, species="fantasy", number_of_plays=100)
lord_of_rings = Movie(title="The Lord of the Rings", year=2000, species="fantasy", number_of_plays=150)

lista = [game_of_thrones, prison_break, harry_potter, lord_of_rings]

lista_movie = []
lista_series = []
def get_movies():
    for i in lista:
        if type(i) == Movie:
            lista_movie.append(i)
    lista1 = sorted(lista_movie, key=lambda movie: movie.title)
    print(lista1)
def get_series():
    for i in lista:
        if type(i) == Series:
            lista_series.append(i)
    lista2 = sorted(lista_series, key=lambda series: series.title)
    print(lista2)
get_movies()
get_series()

def search():
    x = input("Podaj szukany tytuł:")
    z = 0
    for i in lista:
        if x == i.title:
            print("Podany tytuł jest w bibliotece")
            z += 1
            break
        else:
            pass
    if z < 1:
        print("Podanego tytułu nie ma w bibliotece")
search()

def generate_views():
    random.choice(lista).number_of_plays += random.choice(range(1, 101))
generate_views()



def generate_views_10():
    for i in range(11):
        generate_views()

generate_views_10()

def top_titles():
    amount = int(input("Podaj ilość tytułów:"))
    lista3 = sorted(lista, key=lambda movie: movie.number_of_plays)
    lista3.reverse()
    print(lista3[0:amount])

top_titles()
print(game_of_thrones.number_of_plays)
print(prison_break.number_of_plays)
print(lord_of_rings.number_of_plays)
print(harry_potter.number_of_plays)
