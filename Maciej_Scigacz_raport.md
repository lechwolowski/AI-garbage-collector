# Sztuczna Inteligencja 2020 - Raport z podprojektu

**Czas trwania opisywanych prac:** 01.05.2020 - 19.05.2020

**Autor:** Maciej Ścigacz

**Wybrana metoda uczenia:** Drzewa decyzyjne

**Link do repozytorium projektu:** https://git.wmi.amu.edu.pl/s434810/SZI2020Project

---
## Tworzenie zbioru uczącego

Do tworzenia zbioru uczącego wykorzystałem zaimplementowany w projekcie grupowym algorytm A*.

Podczas każdego przejścia przez algorytm, były zbierane informacje o tym jaki krok wykonuje śmieciarka w danym otoczeniu.
Każde otoczenie było dopisywane do tablicy "x_list", a ruch do tablicy "y_list".
Następnie otoczenia zostały zapisane do plików Xlearn.txt, a ruchy do Ylearn.txt.

x_list=[[1,2,4,1,2,1,3,3,1],[3,3,3,1,1,1,4,1,4]]

y_list=[1,2]

---
## x_list

Spłaszczona tablica dwuwymiarowa przedstawiająca otoczenie śmieciarki w danym momencie działania algorytmu.
Zaczytywane jest otoczenie 7x7 wokół śmieciarki.

Legenda:

- 1 - Droga (Road)
- 2 - Trawa (Grass)
- 3 - Dom (House)
- 4 - Śmietnik (Trash)

Dla przykładu w otoczeniu 3x3, poniższy wpis w tablicy:

x_list=
        [1,1,4,
        1,3,2,
        1,3,4]

Przedstawia otoczenie:

```
R R T
R H G
R H T
```
```Python
   # 7x7
    coords = [
        [x-3, y-3], [x-2, y-3], [x-1, y-3], [x+0, y-3], [x+1, y-3], [x+2, y-3], [x+3, y-3],
        [x-3, y-2], [x-2, y-2], [x-1, y-2], [x+0, y-2], [x+1, y-2], [x+2, y-2], [x+3, y-2],
        [x-3, y-1], [x-2, y-1], [x-1, y-1], [x+0, y-1], [x+1, y-1], [x+2, y-1], [x+3, y-1],
        [x-3, y+0], [x-2, y+0], [x-1, y+0], [x+0, y+0], [x+1, y+0], [x+2, y+0], [x+3, y+0],
        [x-3, y+1], [x-2, y+1], [x-1, y+1], [x+0, y+1], [x+1, y+1], [x+2, y+1], [x+3, y+1],
        [x-3, y+2], [x-2, y+2], [x-1, y+2], [x+0, y+2], [x+1, y+2], [x+2, y+2], [x+3, y+2],
        [x-3, y+3], [x-2, y+3], [x-1, y+3], [x+0, y+3], [x+1, y+3], [x+2, y+3], [x+3, y+3]
    ]
```
W momencie gdy danego otoczenia nie da się zaczytać, gdyż obszar wychodzi poza wymiary mapy, nie mieszczące się pola wypełniane są trawą. Nie wpływa to bowiem na poruszanie się śmieciarki, gdyż trawa jest dla niej neutralna.

```Python
    for coord in coords:
        if(0 <= coord[1] < MAP_HEIGHT and 0 <= coord[0] < MAP_WIDTH):
            map_part.append(map2int(MAP, coord[1], coord[0]))
        else:
            map_part.append(2)
```
Dodatkowo na początku "otoczenia" dopisywany jest ruch jaki śmieciarka wykonała uprzednio. Na końcu dopisywane są 24-elementowe kombinacje 0 i 1, które oznaczają aktualny stan danego typu śmieci w danym domu z całej mapy (0-brak/1-jest).

---
## y_list

Tablica jednowymiarowa, która przechowuje ruch śmieciarki w danym otoczeniu. I-ty ruch odpowiada i-temu otoczeniu. Zbieramy informacje o 4 ruchach śmieciarki.

Legenda:

- 0 - Góra
- 1 - Dół
- 2 - Lewo
- 3 - Prawo

---
## Implementacja

Do implementacji uczenia poprzez drzewo decyzyjne użyłem bibiliotekę **scikit learn** dostępnej w języku **python**.
Wypełniając drzewo odpowiednio przygotowanymi danymi, funkcja **predict** zwróci odpowiedni dla otoczenia ruch śmieciarki.

```python
#Uczenie modelu
from sklearn import tree
X = [Otoczenia 7x7 w danym kroku]
Y = [Kolejne ruchy odpowiadające danemu otoczeniu]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

#Zwrócony ruch agenta
clf.predict([Otoczenie agenta])
```

Wszystkie funkcje potrzebne do implementacji projektu znajdują się w folderze **Tree**. 

---
## Problemy
1. Na początku przekazywałem do drzewa otoczenie(bez poprzedniego ruchu i informacji o stanie śmieci na mapie), lecz nie przyniosło to porządanych efektów. Śmieciarka sobie nie radziła. Wykonywała nieskończone, naprzemienne ruchy w prawo/lewo lub góra/dół.

2. Następnie przekazałem do drzewa otoczenie z dodaną na początku informacją jaki był poprzednik ruch śmieciarki. Sytuacja uległa poprawie, śmieciarka zaczęła poruszać się w sposób naturalny, jednakże robiła ciągle tą samą pętlę. 

3. Ostatnią próbą jeszcze większego zróżnicowania zestawu uczącego było dodanie na końcu każdego "otoczenia" stanu śmieci w domach znajdujacych się na mapie.
Ta operacje znacznie polepszyła samodzielne poruszanie się śmieciarki po mapie, przestała ona jeździć tą samą trasą, choć i tak problem z zapętlaniem nie minął, tylko, że teraz pętle które robiła śmieciarka były różne.

---
## Wnioski
Po przygotowaniu około 500 próbek śmieciarka radziła sobie na mapie różnorako. Czasami udało się oczyścić prawie całą mapę. Ewidentnie poprawność działania śmieciarki na mapie, była związana z miejscem w którym śmieciarka rozpoczęła pracę (została wyrenderowana). Nie potrafię stwierdzić, dlaczego śmieciarka wpada czasami w pętle tj. jeździ tą samą drogą w nieskończoność, co uniemożliwia spełnienie warunku kończącego jej pracę (odebranie śmieci z domów + odwiezienie śmieci na wysypisko).