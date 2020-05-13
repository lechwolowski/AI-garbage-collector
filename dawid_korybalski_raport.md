##### Raport przygotował: Dawid Korybalski

##### Raportowany okres: 29 kwietnia - 12 maja 2020 

##### Niniejszy raport poświęcony jest przekazaniu informacji na temat stanu podprojektu indywidualnego w ramach projektu grupowego realizowanego na przedmiot Sztuczna Inteligencja w roku akademickim 2019/2020. 

Tematem realizowanego projektu indywidualnego jest stworzenie sztucznej inteligencji rozpoznającej z podanych pparametrów, czy śmieci wsytawione są wielkogabarytowe, czy nie (ocenia to w 4-wartościowej skali - 0 - nie są to śmieci wielkogabarytowe, 1 - raczej nie są to śmieci wielkogabarytowe, 2 - raczej są to śmieci wielkogabarytowe i 3 - są to śmieci wielkogabarytowe). Do osiągnięcia celu wykorzystałemwartwowe sieci neuronowe (MLP) oraz następujące biblioteki:

- scikit - learn
- joblib
- matplotlib

## Uczenie modelu ##

#### Dane wejściowe: ####

Do utworzenia modelu wykorzzystałem losowo stworzoną tablicę zawierającą krotki z następującymi danymi:

- budżet (od $300 do $1000);
- populacje danego domu (ilu jest w nim mieszkańców - od 2 do 7);
- przychody danej rodziny (od 2000 do 11000);
-  ilość dzieci w domu (od 2 do 4);
- wskazanie rozmiaru śmieci (czy są wielkogabarytowe)

#### Proces uczenia: ####

Na początku dane są tworzone w pętli:

```python
data = []
    for size in range(4):
     for x in range(40000):
            if size == 0:
                budget = random.randint(300, 450)
                population = random.randint(2, 4)
                income = random.randint(2000, 3000)
                children = random.randint(0, 2)
            elif size == 1:
                budget = random.randint(400, 600)
                population = random.randint(3, 5)
                income = random.randint(3000, 5000)
                children = random.randint(0, 3)
            elif size == 2:
                budget = random.randint(550, 800)
                population = random.randint(4, 6)
                income = random.randint(4500, 7000)
                children = random.randint(0, 4)
            else:
                budget = random.randint(700, 1000)
                population = random.randint(4, 7)
                income = random.randint(6800, 11000)
                children = random.randint(1, 4)

            data.append([
                budget,
                population,
                income,
                children,
                size
            ])
 ```

 Następnie dane dziele na zestaw cech (*data*) i zestaw posiadający wielkość śmieci zapisaną (*labels*):
 
 ```python
     labels = [x[4] for x in data]
    for x in range(len(data)):
        del data[x][4]
 ```

Następnie definuje sieć neuronową. Zbiory utworzone przed chwilą, przy wykorzystaniu funkcji **train_test_split** z biblioteki scikat-learn, są dzielone na zestawy do uczenia się i testowania (*x_train*, *x_test*, *y_train*, *y_test*). test_size = 0.3 oznacza, że zbiór danych testowych składa się z 30% krotek zestawu początkowego:

```python
    mlp = MLPClassifier()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3)
```

W następnej lini ładuję do naszej sieci neuronowej załadowane wcześniej zbiory danych:

```python
    mlp.fit(X_train, y_train)
```

Następnie model zostaje poddany testowi i obliczony jest wskażnik trafności (precyzji) wygenerowanych wyników na zbiorze testowym. Wskaźnik ten, dla liczby 40000 utworzonych wyników zwraca wynik ponad 95% trafności:
```python
pred = mlp.predict(X_test)

print(accuracy_score(y_test, pred)) 
```


