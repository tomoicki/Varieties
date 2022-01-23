from math import sin, exp
import random


def funkcja_aktywacji(wartosc):
    return 2 / (1 + exp(-wartosc)) - 1
    # return (1 - exp(-wartosc)) / (1 + exp(-wartosc))


wspolczynnik_uczenia = 0.1
dziedzina = [0.4 * i for i in range(14)]
wagi = []
wartosci_oczekiwane = []
wartosci_policzone = []
delty = []
for i, x in enumerate(dziedzina):
    wagi.append(random.uniform(-2, 2))
    wartosci_oczekiwane.append(sin(x))
    wartosci_policzone.append(funkcja_aktywacji(x * wagi[i]))
    delty.append(wartosci_oczekiwane[i] - wartosci_policzone[i])
# print(dziedzina)
# print(wagi)
# print(wartosci_oczekiwane)
# print(delty)
generation = 0
while True:
    input("")
    print(f"gen={generation}")
    for i, _ in enumerate(wagi):
        print(f"Przed, Neuron nr {i + 1},"
              f"x={dziedzina[i]},waga={wagi[i]},"
              f"expected={wartosci_oczekiwane[i]}, "
              f"calc={wartosci_policzone[i]},d={delty[i]}")
        wagi[i] = wagi[i] + wspolczynnik_uczenia * delty[i] * dziedzina[i]
        wartosci_policzone[i] = funkcja_aktywacji(dziedzina[i] * wagi[i])
        delty[i] = wartosci_oczekiwane[i] - wartosci_policzone[i]
        print(f"Po, Neuron nr {i + 1},"
              f"x={dziedzina[i]},waga={wagi[i]},"
              f"expected={wartosci_oczekiwane[i]}, "
              f"calc={wartosci_policzone[i]},d={delty[i]}")
        # print(delty)
    # print("\n")
    generation += 1
