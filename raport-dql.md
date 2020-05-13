# Sztuczna inteligencja 2020 - Raport 2

**Czas trwania opisywanych prac:** 09.04.2020 - 29.04.2020

**Autor:** Lech Wołowski

**Wybrany temat:** Deep Q Learning(Q Learning z wykorzystaniem sieci neuronowych)

**Link do repozytorium projektu:** https://git.wmi.amu.edu.pl/s434810/SZI2020Project

## Trochę historii

Projekt zacząłem jako q-learning. Zaciekawił mnie ten temat jakiś czas temu i stwierdziłem że chcę się nauczyć jak to działa.
Udało mi się stworzyć działającą lecz bardzo uproszczoną wersję w ten sposób. 
Kiedy tylko zacząłem dodawać nowe informacje o otoczeniu tabela zaczynała przybierać ogromne rozmiary np. 2GB.
Nawet raz dostałem błąd że nie mogę stworzyć tabeli wielkości 16 petabajtów czy jakoś tak. 
W ten sposób doświadczyłem poważnego ograniczenia tej metody - działa ona jedynie do prostych bardzo modeli.

Kiedy zdałem sobie sprawę, że to droga do nikąd zacząłem szukać informacji o zastosowaniu sieci neuronowej zamiast tabeli właśnie.
W ten sposób powstał pomysł na takie właśnie rozwiązanie tego problemu.

Po drodze dowiedziałem się że właściwie to potrzebuję nie jednej sieci a dwóch działających jednocześnie - jedna zgadująca, druga trenowana.
Do tego dochodzi problem wybrania architektury sieci - w końcu bardzo mało wiedziałem o projektowaniu ich wcześniej.
Dużo różnych prób i błędów spotkałem po drodze i tego ślady znajdują się w folderach: logs, logs-arch, trained_models/arch i trained_models/bugged.

Niestety uczenie tych sieci idzie bardzo mozolnie i nawet dzisiaj nie wiem czy to działa a już 3 tygodnie temu myślałem że prawie wszystko gotowe

## Jak to wszysto w ogóle działa?

Zacznijmy od klasy DQNAgent:
[deep_q_learning file](Deep_Q_Learning/deep_q_learning.py)
zacznijmy od konstruktora

Model definiujemy w metodzie create_model i tworzymy
lub używamy modelu jeśli jakiś jest podany jako argument.
Obecnie model składa się z 6 ukrytych warstw używających funkcji aktywacyjnej tanh.
Niestety nie miałem dość czasu by testować inne sieci a podobna zaczeła osiągać jakiekolwiek postępy w trakcie testów.
następnie ustawiamy współczynniki tak by były jednakowe w obu sieciach
tworzymy kolejkę zapisanych ruchów
tworzymy logi

Mamy tutaj jeszcze trzy metody:
update_replay_memory - dodawanie ruchu do kolejki zapisanych ruchów
train - uczenie sieci neuronowej
get_qs - przewidywanie ruchu na podstawie stanu środowiska

jedynie train z tych trzech nie jest trywialny więc o nim napiszę.
```
def train(self, terminal_state):

    # Tutaj sprawdzamy czy wystarczająco dużo ruchów mamy zapamiętane do uczenia
    if len(self.replay_memory) < MIN_REPLAY_MEMORY_SIZE:
        return

    # losujemy zdefiniowaną ilość z zapamiętanych ruchów
    minibatch = random.sample(self.replay_memory, MINIBATCH_SIZE)

    # wyciągamy stan środowiska z każdego ruchu
    current_states = np.array([transition[0]
                                for transition in minibatch])
    # dla każdego ze stanów środowiska przewidujemy najlepszy ruch za pomocą sieci
    current_qs_list = self.model.predict(current_states)

    # dla każdego ze stanów następujących bierzemy stan środowiska
    new_current_states = np.array(
        [transition[3] for transition in minibatch])
    # używamy sieci docelowej do przewidywania maksymalnej kolejnego ruchu
    future_qs_list = self.target_model.predict(new_current_states)

    __x__ = []
    __y__ = []

    # Przechodzimy w pętli po każdym ruchu z wylosowanych
    for index, (current_state, action, reward, new_current_state, old_state, done) \
            in enumerate(minibatch):

        # sprawdzamy czy ten ruch nie jest ruchem kończącym grę
        if not done:
            # sprawdzamy jaka jest najlepsza możliwa nadchodząca nagroda po
            # ruchu który wykonaliśmy i doliczamy ją do obecnej
            max_future_q = np.max(future_qs_list[index])
            new_q = reward + DISCOUNT * max_future_q
        else:
            new_q = reward

        # Aktualizujemy wartość q dla wybranej akcji w danym ruchu na podstawie wyżej ustalonej wartości
        current_qs = current_qs_list[index]
        current_qs[action] = new_q

        # dodajemy stan początkowy i wartości q do tablic 
        __x__.append(current_state)
        __y__.append(current_qs)

    # na podstawie tablic które stworzyliśmy w powyższej pętli uczymy sieć
    self.model.fit(np.array(__x__), np.array(__y__), batch_size=MINIBATCH_SIZE, verbose=0,
                    shuffle=False, callbacks=[self.tensorboard] if terminal_state else None)

    # dla każdego końca gry zwiększamy wartość o 1 tak by aktualizować sieć docelową co kilka skończonych gier
    if terminal_state:
        self.target_update_counter += 1

    # # Co ustaloną liczbę powtórzeń aktualizujemy sieć docelową na podstawie uczonej sieci
    if self.target_update_counter > UPDATE_TARGET_EVERY:
        self.target_model.set_weights(self.model.get_weights())
        self.target_update_counter = 0

```




 [dql_runner.py](dql_runner.py)