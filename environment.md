# Sztuczna inteligencja 2020 - Raport 1

**Czas trwania opisywanych prac:** 04.03.2020 - 08.04.2020

**Członkowie zespołu:** Lech Wołowski, Dawid Korybalski, Łukasz Kochański, Maciej Ścigacz

**Wybrany temat:** Inteligentna śmieciarka

**Link do repozytorium projektu:** https://git.wmi.amu.edu.pl/s434810/SZI2020Project

## Założenia Gry

1. Mapa składa się z kwadratów
2. Każdy kwadrat jest generowany dynamicznie zależnie od mapy
3. Mapa jest zapisana w postaci słownika ze współrzędnymi w celu prostej modyfikacji
4. Śmieciarka porusza się jedynie po kwadratach które są drogą
5. Śmieciarka będąc obok budynku odbiera odpady
6. Śmieciarka będąc obok śmietnika oddaje odpady
7. Obrazki do generowania kwadratów tworzymy sami

## Elementy z których gra jest zbudowana

1. [Road.py](models/Road.py)
2. [Garbage_Collector.py](models/Garbage_Collector.py)
3. [Grass.py](models/Grass.py)
4. [House.py](models/House.py)
5. [Trash.py](models/Trash.py)

(kliknięcie otwiera dany plik)

rozmieszczenie powyższych elementów na mapie definiujemy w pliku config.py w następujący sposób:

MAP = {
0: {0: "Glass", 1: "Road", 2: "Road", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "Paper"},
1: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "Grass"},
2: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "House"},
3: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Road", 8: "Road", 9: "Road", 10: "Road", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "House"},
4: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Grass", 8: "Grass", 9: "Grass", 10: "Grass", 11: "Road", 12: "Grass", 13: "Grass", 14: "Road", 15: "House"},
5: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Grass", 8: "Grass", 9: "Grass", 10: "Grass", 11: "Road", 12: "Grass", 13: "Grass", 14: "Road", 15: "House"},
6: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "Road", 8: "Road", 9: "Road", 10: "Road", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "House"},
7: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "House"},
8: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "House", 13: "House", 14: "Road", 15: "Grass"},
9: {0: "Mixed", 1: "Road", 2: "Road", 3: "Road", 4: "House", 5: "House", 6: "Road", 7: "House", 8: "Road", 9: "House", 10: "House", 11: "Road", 12: "Road", 13: "Road", 14: "Road", 15: "Plastic"},
}

Są to nazwy klas w słowniku, gdzie liczby to współrzędne. Każdy element jest w main.py zamieniany na odpowiednią komórkę.

## Reprezentacja Wiedzy

W klasie Knowledge wyciągamy wszystkie istotne informacje o stanie gry i przechowujemy je w obiektach

Ilość odpadów w każdym domu przechowujemy w słownikach tak aby informacja o ilości odpadów była łatwo dostępna. Przykład:

2: {'col': 5, 'row': 0}

Dla klucza którym jest ilość odpadów danego typu przechowujemy tablicę współrzędnych domów z taką ilością odpadów.

```
mixed_trash_quantity_houses
paper_trash_quantity_houses
glass_trash_quantity_houses
plastic_trash_quantity_houses
```

w tych 4 słownikach przechowujemy informację o danym typie śmieci

## Grafika

Całą grafikę stworzyliśmy w oparciu o format SVG w programie Inkscape. Format SVG jest formatem dwuwymiarowej grafiki wektorowej. Jego największą korzyścią jest fakt, iż można dostosowywać rozdzielczość wyeksportowanej z niej grafiki (w formacie .png) podczas rozwoju projektu.

Grafika po utworzeniu w programie Inkscape, zostaje wyeksportowana do pliku .png, który następnie wczytujemy do aplikacji. 

## Elementy grafiki z których gra jest zbudowana

1. [garbage-collector.png](Resources/Images/garbage-collector.png)
2. [house.png](Resources/Images/house.png)
3. [road.png](Resources/Images/road.png)
4. [trash-glass.png](Resources/Images/trash-glass.png)
5. [trash-mixed.png](Resources/Images/trash-mixed.png)
6. [trash-paper.png](Resources/Images/trash-paper.png)
7. [trash-plastic.png](Resources/Images/trash-plastic.png)

(kliknięcie otwiera dany plik)

Część grafik była wzorowana, bądź pobrana z serwisu flaticon.com 

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
