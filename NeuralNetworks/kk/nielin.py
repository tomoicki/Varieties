import random

ilosc_neuronow = 3
wzorce = [[3, 4, 3, 4, 5],
          [1, -2, 1, -2, -2],
          [-3, -2, -3, 2, 3]]

stopien_pewnosci = [[1, -1, -1],
                    [-1, 1, -1],
                    [-1, -1, 1]]

nowe_wagi1 = [random.uniform(-2, 2) for _ in range(len(wzorce[0]))]
nowe_wagi2 = [random.uniform(-2, 2) for _ in range(len(wzorce[0]))]
nowe_wagi3 = [random.uniform(-2, 2) for _ in range(len(wzorce[0]))]

wsp_uczenia = 0.1

dane_znormalizowane = []
for i in range(len(wzorce)):
    wzorzec = wzorce[i]
    normalizacja = sum([wartosc ** 2 for wartosc in wzorzec]) ** 0.5
    dana_znormalizowana = [wartosc / normalizacja for wartosc in wzorzec]
    dane_znormalizowane.append(dana_znormalizowana)

i = 0


def f_aktywacji(wartosc, prog):
    if wartosc >= prog:
        return 1
    else:
        return -1


def licz_wagi(wagi_poczatkowe, nr_kalkulacji):
    global i
    wynik = sum(wartosc * waga for wartosc, waga in zip(dane_znormalizowane[nr_kalkulacji], wagi_poczatkowe))
    wynik = f_aktywacji(wynik, 0)
    delta = stopien_pewnosci[nr_kalkulacji][i] - wynik
    nowe_wagi = [waga + wsp_uczenia * delta * wartosc for wartosc, waga in
                 zip(dane_znormalizowane[nr_kalkulacji], wagi_poczatkowe)]
    print(f"Neuron nr: {i + 1}\n"
          f"wagi poczatkowe: {wagi_poczatkowe}\n"
          f"wzorzec: {dane_znormalizowane[nr_kalkulacji]}\n"
          f"wynik poprawny: {stopien_pewnosci[nr_kalkulacji][i]}\n"
          f"nowy wynik dla wzorca: {wynik}, delta: {delta}\n"
          f"wagi po nauczeniu: {nowe_wagi}\n")
    if i < len(stopien_pewnosci[0]) - 1:
        i += 1
    else:
        i = 0
    return nowe_wagi


nr_kalkulacji = 0
while True:
    nowe_wagi1 = licz_wagi(nowe_wagi1, nr_kalkulacji)
    nowe_wagi2 = licz_wagi(nowe_wagi2, nr_kalkulacji)
    nowe_wagi3 = licz_wagi(nowe_wagi3, nr_kalkulacji)
    stop = input("Nacisnij 'e' zeby przerwac lub inny klawisz zeby kontynuowac nauke:\n")
    if nr_kalkulacji < len(wzorce) - 1:
        nr_kalkulacji += 1
    else:
        nr_kalkulacji = 0
    if stop == 'e':
        break
