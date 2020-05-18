import random
import joblib
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from models.__house__ import House
from sklearn.metrics import (
    classification_report, plot_confusion_matrix, accuracy_score
)


# size = 0, 1, 2, 3
def main():
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

        # data.append({
        #     'budget': budget,
        #     'population': 4,
        #     'income': 10000,
        #     'children': 2,
        #     'size': size
        # })


    #usunięcie wartości "size", aby móc je przewidzieć

    labels = [x[4] for x in data]
    for x in range(len(data)):
        del data[x][4]

    #przeprowadzenie nauki dla zbioru testowego losowo generowanego
    mlp = MLPClassifier()
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3)
    mlp.fit(X_train, y_train)

    #generowanie wyników dla zbioru testowego losowo generowanego
    pred = mlp.predict(X_test)


    #porównianie z faktyczny wynikiem - wyliczenie dokładności naszej predykcji
    print(accuracy_score(y_test, pred)) 
    
    #stworzenie raportu pokazującego m.in. precyzje dla poszczególnych "size'ów"
    
    #print(classification_report(y_test, pred))


    #Macierz konfuzji w postacji wykresu gradientowego (użyta w raporcie)
    
    #plot_confusion_matrix(mlp, X_test, y_test)
    #gi tstplt.show()
    
    
    # przekazanie wygenerowanego modelu do pliku
    #filename = 'finalized_model.sav'
    #joblib.dump(mlp, filename)


## Funkcja
##def predict_houses(houses_data):
    # mlp = MLPClassifier()
    # mlp.fit(X_train, y_train)
    #red = mlp.predict(houses_data)
    #return pred

# wywolanie funkcji, wrzucam liste obiektow klasy House

#house = House(1, 3)
#house.data = [1000, 4, 10000, 2]
#house_2 = House(1, 3)
#house_2.data = [1000, 4, 11000, 2]
#houses = [house, house_2]
#predictions = predict_houses([house.data for house in houses])
#for x in range(len(houses)):
#    houses[x].size = predictions[x]

#print([(x.col, x.row, x.size, x.data) for x in houses])
main()