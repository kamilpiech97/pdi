import collections
import csv
import json

from src.places import City, Street


class Province(object):
    def __init__(self, code, name):
        self.code = code
        self.name = name


provinces = [Province("02", "dolnośląskie"), Province("04", "kujawsko-pomorskie"), Province("06", "lubuskie"),
             Province("10", "łódzkie"), Province("06", "lubelskie"), Province("12", "małopolskie"),
             Province("14", "mazowieckie"), Province("16", "opolskie"), Province("20", "podlaskie"),
             Province("18", "podkarpackie"), Province("22", "pomorskie"), Province("26", "świętokrzyskie"),
             Province("24", "śląskie"), Province("28", "warmińsko-mazurskie"), Province("30", "wielkopolskie"),
             Province("32", "zachodniopomorskie")]


class Cities(object):
    def __init__(self, file):
        self.file = file

    def find_by_id(self, city_id):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            city = self.__find_exact_city(lines, city_id)

            if not city:
                city = self.__find_fallback_city(lines, city_id)

            if city:
                return city

        return City("? (" + city_id + ")")

    @staticmethod
    def __find_exact_city(lines, city_id):
        for line in lines:
            if city_id + ";" + city_id in line:
                return City(line.split(";")[6])

    @staticmethod
    def __find_fallback_city(lines, city_id):
        for line in lines:
            if city_id in line:
                return City(line.split(";")[6])


class Streets(object):
    def __init__(self, file, cities):
        self.file = file
        self.cities = cities

    def find_by_street_name(self, street_name):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                if street_name.lower() in line.lower():
                    street = Street(line)
                    street.set_city(self.cities.find_by_id(street.city_id))
                    yield street

    def find_by_street_name_and_wojewodztwo(self, street_name, wojewodztwo):
        with open(self.file, encoding="utf-8") as fp:
            lines = fp.readlines()
            for line in lines:
                if wojewodztwo in line.lower():
                    if street_name.lower() in line.lower():
                        street = Street(line)
                        street.set_city(self.cities.find_by_id(street.city_id))
                        yield street

    def find_100_popular_streets(self):
        results = []
        with open(self.file) as file_cities:
            file_read = csv.reader(file_cities, delimiter=';', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            array = list(file_read)
            for row in array[1:-1]:
                results.append(row[8] + " " + row[7])

            occurrences = collections.Counter(results)

            for letter, count in occurrences.most_common(100):
                print('%s: %7d' % (letter, count))

    def find_popular_streets_per_province(self):

        with open(self.file) as file_cities:
            file_read = csv.reader(file_cities, delimiter=';', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            array = list(file_read)
            for province in provinces:
                results = []
                for row in array[1:-1]:
                    if row[0] == province.code:
                        results.append(row[8] + " " + row[7])
                occurrences = collections.Counter(results)

                for letter, count in occurrences.most_common(1):
                    print('%s: %s - %d' % (province.name, letter, count))
