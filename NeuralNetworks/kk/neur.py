wzorce = [[2, 2, 2, 2, 2],
          [-2, -2, -2, -2, -2],
          [1, 1, -1, -1, -1],
          [-1, -1, 1, 1, 1]]
stopien_pewnosci = [1, -1, 0.8, -0.8]
wagi_poczatkowe = [-0.1, 0.2, -0.5, 0.3, -0.4]
wsp_uczenia = 0.1

dane_znormalizowane = []
for i in range(len(wzorce)):
    wzorzec = wzorce[i]
    normalizacja = sum([wartosc ** 2 for wartosc in wzorzec]) ** 0.5
    dana_znormalizowana = [wartosc / normalizacja for wartosc in wzorzec]
    dane_znormalizowane.append(dana_znormalizowana)

iteracja = 0
i = 0


def licz_wagi(wagi_poczatkowe):
    global i
    wynik = sum(wartosc * waga for wartosc, waga in zip(dane_znormalizowane[i], wagi_poczatkowe))
    delta = stopien_pewnosci[i] - wynik
    nowe_wagi = [waga + wsp_uczenia * delta * wartosc for wartosc, waga in zip(dane_znormalizowane[i], wagi_poczatkowe)]
    print(f"Iteracja: {iteracja}\n"
          f"wzorzec {i + 1}: {dane_znormalizowane[i]}\n"
          f"wagi poczatkowe: {wagi_poczatkowe}\n"
          f"wynik poprawny: {stopien_pewnosci[i]}\n"
          f"nowy wynik dla wzorca {i + 1}: {wynik}, delta: {delta}\n"
          f"wagi po nauczeniu: {nowe_wagi}\n")
    if i < len(wzorce) - 1:
        i += 1
    else:
        i = 0
    return nowe_wagi


iteracja += 1
nowe_wagi = licz_wagi(wagi_poczatkowe)


def testowanie_wprowadzonych_danych(nowe_wagi):
    dane_do_przetestowania = []
    print("Podaj dane do przetestowania:")
    for i in range(len(wzorce[0])):
        wartosc = float(input(f"Podaj wartość nr {i + 1}: "))
        dane_do_przetestowania.append(wartosc)

    oczekiwany_wynik = float(input("Podaj oczekiwany wynik: "))
    wynik = sum(wartosc * waga for wartosc, waga in zip(dane_do_przetestowania, nowe_wagi))
    delta = oczekiwany_wynik - wynik
    print(f"podane wartosci = {dane_do_przetestowania}\n"
          f"uzyte wagi = {nowe_wagi}\n"
          f"oczekiwany wynik = {oczekiwany_wynik}\n"
          f"policzony wynik = {wynik}\n"
          f"delta = {delta}")


while True:
    iteracja += 1
    nowe_wagi = licz_wagi(nowe_wagi)
    stop = input("Nacisnij 'e' zeby przerwac, 't' zeby przetestowac lub inny klawisz zeby kontynuowac nauke:\n")
    if stop == 'e':
        break
    elif stop == 't':
        testowanie_wprowadzonych_danych(nowe_wagi)
        break
