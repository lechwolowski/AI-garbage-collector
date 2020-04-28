# Sztuczna inteligencja 2020 - Raport 2

**Czas trwania opisywanych prac:** 09.04.2020 - 29.04.2020

**Członkowie zespołu:** Lech Wołowski, Dawid Korybalski, Łukasz Kochański, Maciej Ścigacz

**Wybrany temat:** Inteligentna śmieciarka

**Link do repozytorium projektu:** https://git.wmi.amu.edu.pl/s434810/SZI2020Project

## Wykorzystywany algorytm przeszukiwania

Zdecydowaliśmy się na wybór algorytmy 'A*'.  Jest to heurystyczny algorytm do znajdowania najkrótszej ścieżki w grafie. Jest zupełny i optymalny, zatem zawsze znalezione rozwiązanie jest tym najlepszym. Dodatkowo, wykorzystując algorytm 'A*' mamy pewność, że każdy punkt może zostać odwiedzony. 

## Przygotowanie środowiska pod algorytm

Śmieciarka (co oczywiste) poruszać może się tylko po powierzchni typu "Road". Dodatkowo, w rzeczywistym świecie, zazwyczaj śmieciarka zbiera smieci, które są wystawione "przed" dom, a nie są w nim, zatem przyjęliśmy założenie, że w odległości 1 kratki od domu, śmieciarka może zebrać śmieci.

Postanowiliśmy również zmiejszyć mapę, tak aby było na mapie sześć domów z losowo generowaną ilością śmieci, czterech różnych typów (zakres ilości śmieci danego typu określony jest w  [House.py](models/House.py) i jest to losowa liczba od 0 do 9). Pojemość śmieciarki określona w [Garbage_Collector.py](models/[Garbage_Collector.py) wynosi 10 sztuk śmieci danego typu. 

Nowy model mapy wygląda w następujący sposób (znajduje się w pliku [config.py](config.py)):

MAP = {
    0: {0: "Glass", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Paper"},
    1: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "Road", 6: "Grass", 7: "Road", 8: "Grass"},
    2: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Grass", 7: "Road", 8: "House"},
    3: {0: "Grass", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Grass"},
    4: {0: "House", 1: "Road", 2: "Grass", 3: "Road", 4: "Road", 5: "Road", 6: "Grass", 7: "Road", 8: "House"},
    5: {0: "Grass", 1: "Road", 2: "Grass", 3: "Road", 4: "House", 5: "Road", 6: "Grass", 7: "Road", 8: "Grass"},
    6: {0: "Mixed", 1: "Road", 2: "Road", 3: "Road", 4: "Grass", 5: "Road", 6: "Road", 7: "Road", 8: "Plastic"},
}

Model mapy jest skonstruowany oczywiście w taki sposób, aby z każdego domu dało się dojechać do innego domu, jak również, z każdego miejsca na mapie do dowolnego miejsca utylizacji śmieci.

## Implementacja algorytmu w nasz projekt

Cały algorytm 'A*' zaimplemetnowany jest w pliku o nazwie [a_star.py](a_star.py).  Działa on w następujący sposób:

Na początku, dbamy o to, żeby wszystkie domy w których znajdują się śmieci, zostały umieszczone na liście o nazwie  <code>houses_with_trash</code>. W momencie, gdy śmieciarka zabierze wszystkie śmieci z danego domu, wtedy dom ten jest usuwany z tej listy.

Najlepsza droga wybierana jest za pomocą zdefinowanej funkcji <code>best_move</code>. Sprawdza ona najpierw ile jest śmieci w danym domku (w sumie) i dzieli ten wynik przez odległość do tego domu. Funkcja ta też sprawdza, kiedy śmieciarka ma odwieźć śmieci do wysypiska (dzieje się tak, gdy w domach nie ma już śmieci, albo jeśli jest ona pełna).
 
Dostanie się śmieciarki do drogi sąsiadującej z "najlepszym" domem (żeby odebrać śmieci) i do drogi sąsiadującej z wysypiskiem (w celu opróżnienia śmieci) opisana jest w funkcji <code>astar</code>.

## Uruchomienie projektu i algorytmu A*

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
wciśnij klawisz `a`

Windows

```
python -m venv env
env\scripts\activate.bat
pip install -r requirements.txt
python main.py
```
wciśnij klawisz `a`
