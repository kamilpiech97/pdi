from src.map import Map


def get_searched_phrase(argv):
    if len(argv) < 3:
        exit("Try to pass argument: python3 main.py 1 Legnicka")

    return argv[2]


def get_menu_choose(argv):
    if len(argv) < 2:
        exit("Try to pass argument: python3 main.py 2")

    return argv[1]


def get_mapbox(argv):
    if len(argv) == 4:
        return Map(argv[3])

    return None
