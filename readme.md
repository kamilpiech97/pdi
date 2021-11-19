## Program
Powyższy program jest prostą przykładową aplikacją do wstępnej analizy danych z bazy TERYT. Jest wykorzystywany jako podstawa projektowa na zajęciach "Programowanie dla inżynierów" dla kierunku Inżynieria produkcji i logistyki na Wydziale Nauk Technicznych i Ekonomicznych Państwowej Wyższej Szkoły Zawodowej im. Witelona w Legnicy.

### Wymagania
* Python 3
* opcjonalnie token [Mapbox](https://www.mapbox.com/) do generowania map

### Uruchomienie
Aplikację możemy uruchomić wybierając jedną spośród sześciu opcji w menu:
* `python3 main.py 1 phrase` - wypisuje wszystkie lokacje pasujące do podanej `phrase`;
* `python3 main.py 1 phrase token` - wypisuje wszystkie lokacje pasujące do podanej `phrase` oraz rysuje je na mapie;
* `python3 main.py 2` - wypisuje 100 najpopularniejszych ulic w Polsce;
* `python3 main.py 3` - wypisuje najpopularniejszą ulicę per województwo;
* `python3 main.py 4` - wypisuje podobne ulice w tym samym mieście (np. 1 Maja i 3 Maja);
* `python3 main.py 5` - wypisuje najpopularniejsze miasto per województwo;
* `python3 main.py 6` - wypisuje 100 najpopularniejszych miast w Polsce.

W przypadku uruchomienia z tokenem Mapboksa, wynik znajdzie się w folderze `www/index.html`.

### Krok po kroku
W pliku `main.py` znajduje się zestaw instrukcji, które zostaną pokrótce opisane poniżej:

```python
menu_choose = get_menu_choose(argv) - wyboru opcji z menu
searched_street = get_searched_phrase(argv) - w przypadku wyboru opcji z menu numer jeden
mapbox = get_mapbox(argv)
```
Na podstawie podanych argumentów budowane są wewnętrzne zmienne przechowujące odpowiednie informację o wyszukiwanej frazie oraz obiekcie mapy. Jeżeli nie zostały podane żadne argumenty, program nie uruchomi się poprawnie.

Gdy wybieramy opcję numer jeden i gdy podamy tylko jednen argument zostanie przeprowadzenie przeszukanie zbiorów i wypisanie ich w konsoli na podstawie podanego argumentu.

Przy podaniu trzeciego argumentu, zostanie potraktowany jako token Mapboksa.

## Źródła
Pliki TERYT zostały pobrane 9 października 2021 roku z poniższego adresu:
* https://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default