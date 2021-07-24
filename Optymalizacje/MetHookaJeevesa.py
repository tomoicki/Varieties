import math

# x = [0, 0]  # punkt poczatkowy
# delta = 0.25  # poczatkowa dlugosc kroku

x = [3, 2]  # punkt poczatkowy
delta = 2  # poczatkowa dlugosc kroku

# x = [1, 4, 2]  # punkt poczatkowy


beta = 0.5  # parametr zmniejszania kroku
epsilon = 0.01  # kryterium zbieznosci


def funkcja(x):
    #return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
    #return x[0] ** 2 + x[1] ** 2 - 3 * math.sin(x[0] - x[1])

    #return x[0] ** 2 + x[1] ** 2 + 1 + x[0] + x[1]
    #return 6 * x[0] ** 2 - 2 * x[0] + 2 * x[1] ** 2 + 4 * x[1] + 3
    #return (x[0] ** 2 - 4 * x[0] + 5) + (x[1] ** 2 - 6 * x[1] + 11) + (x[2] ** 2 - 2 * x[2])


    return (1 - x[0]) ** 2.0 + 14 * (x[1] - x[0] ** 2) ** 2


def etapProbny(x, delta, beta, epsilon):
    xB0 = list.copy(x)
    count = 0
    back = 0
    pBazowy = []
    pBazowy.append(x)
    for i in range(50):
        z = list.copy(x)
        f0 = funkcja(x)
        os = 1
        print(f'\n---- Etap: {count + 1}, delta: {delta}\nx0:', x, 'f0=', f0)
        for i in range(len(x)):
            z[i] = z[i] + delta
            fz = funkcja(z)
            print(f'x{os}:', z, ' fz=', fz)
            if fz < f0:
                f0 = fz
                os += 1
                print('New f0=', f0)
            else:
                z[i] = z[i] - 2 * delta
                fz = funkcja(z)
                print(f"x{os}:", z, ' fz=', fz)
                if fz < f0:
                    f0 = fz
                    os += 1
                    print('New f0=', f0)
                else:
                    z[i] = z[i] + delta
                    os += 1
                    print('- f0=', f0, ' z=', z)

        count += 1
        if f0 < funkcja(xB0):
            pBazowy.append(z)
            x, xB0 = etapRoboczy(pBazowy)
        else:
            if delta < epsilon:
                print('\nf(xmin)', funkcja(x), 'w punkcie', x)
                print('Zmiana delty:', back)
                print("Ilość punktów bazowych:", len(pBazowy))
                print('Punkty bazowe:', pBazowy[:])
                break
            else:
                back += 1
                delta = beta * delta
                x = pBazowy[-1]
                xB0 = list.copy(x)
                print("-- Nowa delta:", delta)
                print("-- Powrót do poprzedniego punktu bazowego:", x)


def etapRoboczy(pBazowy):
    pb = pBazowy[-2]
    npb = pBazowy[-1]
    print('-- Punkt bazowy (xB0):', pb)
    print('-- Nowy punkt bazowy (xB):', npb)
    pbpt = [2 * item for item in npb]
    for i, j in enumerate(pb): pbpt[i] -= j
    xB0 = npb
    x = pbpt
    print('-- Punkt po transformacji:', pbpt)
    return x, xB0


etapProbny(x, delta, beta, epsilon)
