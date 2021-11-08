import collections
import csv

from src.cli import get_searched_phrase, get_mapbox, get_menu_choose
from src.repositories import Cities, Streets
from sys import argv

menu_choose = get_menu_choose(argv)

cities = Cities("data/SIMC_Urzedowy_2021-10-09.csv")
streets = Streets("data/ULIC_Adresowy_2021-10-09.csv", cities)

if menu_choose == "1":
    searched_street = get_searched_phrase(argv)
    mapbox = get_mapbox(argv)
    counter = 0
    found_streets = streets.find_by_street_name(searched_street)

    for street in found_streets:
        phrase = str(street.city) + ": " + street.get_full_name()
        print(phrase)
        counter = counter + 1

        if mapbox:
            coordinate = mapbox.add_coordinates_for_phrase(phrase)

    print(str(counter) + " streets were found.")

    if mapbox:
        mapbox.prepare_map(searched_street)
elif menu_choose == "2":
    streets.find_100_popular_streets()
elif menu_choose == "3":
    streets.find_popular_streets_per_province()
elif menu_choose == "4":
    streets.duplicated_street_in_city()
