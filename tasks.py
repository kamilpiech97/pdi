import collections
import csv
from sys import argv

from src.cli import get_searched_phrase, get_mapbox
from src.repositories import Cities, Streets, Province

searched_street = get_searched_phrase(argv)
mapbox = get_mapbox(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

found_streets = streets.find_by_street_name(searched_street)

streets.find_popular_streets_per_province()
streets.find_100_popular_streets()
