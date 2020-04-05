# Sztuczna inteligencja 2020 - Raport 1

**Czas trwania opisywanych prac:** 04.03.2020 - 08.04.2020

**Członkowie zespołu:** Lech Wołowski, Dawid Korybalski, Łukasz Kochański, Maciej Ścigacz

**Wybrany temat:** Inteligentna śmieciarka

**Link do repozytorium projektu:** https://git.wmi.amu.edu.pl/s434810/SZI2020Project

## Założenia Gry

1. Mapa składa się z kwadratów
2. Każdy kwadrat jest generowany dynamicznie zależnie od mapy
3. Mapa jest zapisana w postaci macierzy w celu prostej modyfikacji
4. Śmieciarka porusza się jedynie po kwadratach które są drogą
5. Śmieciarka będąc obok budynku odbiera odpady
6. Śmieciarka będąc obok śmietnika oddaje odpady
7. Obrazki do generowania kwadratów tworzymy sami

## Klasy składowych elementów gry

1. Droga
2. Dom
3. Fabryka
4. Wysypisko
5. Trawa
6. Drzewa
7. Staw
8. Śmieciarka

## Mapa

Macierz postaci: <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 <br />

reprezentująca mapę gry.

mapa jest renderowana z tej macierzy w pliku main.py

## Instalacja i uruchomienie

Wymagania:

```
Python: 3.7.7
```

macOS / Linux

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python main.py
```

Windows

```
python -m venv env
env\scripts\activate.bat
pip install -r requirements.txt
python main.py
```
