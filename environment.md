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

1. Road.py
2. Garbage_Collector.py
3. Grass.py
4. House.py
5. Trash.py

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
