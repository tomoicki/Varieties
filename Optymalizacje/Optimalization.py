from math import fabs
import random
import pandas

def wp():
    a = 5
    b = 0
    n = 99999
    print("\nWyczerpującego poszukiwania")
    print(f"(a,b) = {a, b}")
    print(f"n = {n}")
    x1 = a
    dx = (b - a) / n
    x2 = x1 + dx
    x3 = x2 + dx
    while True:
        if f(x1) >= f(x2) <= f(x3):
            print(f"x_min ∈ {x1, x3}")
            break
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + dx
            if x3 <= b:
                continue
            else:
                print(f"Min does not exist inside {a, b} or is equal {a} or {b}.")
                break

def pp():  # przyspieszonego poszukiwania
    xk = 2
    d = 0.001
    k = 0
    if f(xk - fabs(d)) >= f(xk) >= f(xk + fabs(d)):
        d = fabs(d)
    elif f(xk - fabs(d)) <= f(xk) <= f(xk + fabs(d)):
        d = -1 * fabs(d)
    else:
        print("go back to 1)")
    print("\nPrzyspieszonego poszukiwania")
    print(f"k = {k}")
    print(f"xk = {xk}")
    print(f"d = {d}")
    k_list = []
    while True:
        xkplus1 = xk + 2 ** k * d
        k_list.append(xkplus1)
        if f(xkplus1) < f(xk):
            k += 1
        else:
            temp = [min(k_list[-3], k_list[-1]), max(k_list[-3], k_list[-1])]
            print(f"x_min ∈ {temp[0], temp[1]}")
            new_A, new_B = temp[0], temp[1]
            break

def dpp():  # dzielenie przedziału na połowe
    global A
    global B
    global epsilon
    a = A
    b = B
    print("\nDzielenie przedziału na połowe")
    print(f"(a,b) = {a, b}")
    print(f"𝜖 = {epsilon}")
    xm = (a + b) / 2
    L = b - a
    while True:
        x1 = a + L / 4
        x2 = b - L / 4
        if f(x1) < f(xm):
            b = xm
            xm = x1
        else:
            if f(x2) < f(xm):
                a = xm
                xm = x2
            else:
                a = x1
                b = x2
        L = b - a
        if fabs(L) < epsilon:
            break
    print(f"x_min ∈ {a, b}")

def zp():  # złoty podział
    fi = (1 + 5 ** 0.5) / 2
    global A
    global B
    global epsilon
    a = A
    b = B
    print("\nZłoty podział")
    print(f"(a,b) = {a, b}")
    print(f"𝜖 = {epsilon}")
    x1 = b - (b - a) / fi
    x2 = a + (b - a) / fi
    fx1 = f(x1)
    fx2 = f(x2)
    while True:
        if fx1 > fx2:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = a + (b - a) / fi
            fx2 = f(x2)
        else:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = b - (b - a) / fi
            fx1 = f(x1)
        if fabs(b - a) < epsilon:
            break
    print(f"x_min ∈ {a, b}")

def lf():  # liczb Fibonacziego
    global A
    global B
    global epsilon
    a = A
    b = B
    print("\nLiczb Fibonacciego")
    print(f"(a,b) = {a, b}")
    print(f"𝜖 = {epsilon}")
    fib = [1, 1]
    [fib.append(fib[k - 1] + fib[k - 2]) for k in range(2, 100)]
    fn = (b - a) / (2 * epsilon)
    # for i in range(2, 100):
    #     fibs.append(fibs[-1] + fibs[-2])
    #     if fibs[-1] >= fn:
    #         break
    n = len(fib) - 1
    x1 = b - (fib[n - 1] / fib[n]) * (b - a)
    x2 = a + (fib[n - 1] / fib[n]) * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    while True:
        n = n - 1
        if y1 < y2:
            b = x2
            x2 = x1
            y2 = y1
            x1 = b - (fib[n - 1] / fib[n]) * (b - a)
            y1 = f(x1)
        else:
            a = x1
            x1 = x2
            y1 = y2
            x2 = a + (fib[n - 1] / fib[n]) * (b - a)
            y2 = f(x2)
        if fabs(x2 - x1) >= epsilon and n >= 2:
            continue
        else:
            x = (x1 + x2) / 2
            print(f"x_min ≈ {x}\nf(x_min) ≈ {f(x)}")
            break

def ik(): # Powella
    global A
    global B
    global epsilon
    a = A
    b = B
    print("\nPowella")
    print(f"(a,b) = {a, b}")
    attempts = 0
    while attempts <= 1000:
        x1 = random.uniform(a, b)
        x2 = random.uniform(a, b)
        x3 = random.uniform(a, b)
        attempts += 1
        if x1 < x2 < x3:
            if f(x1) > f(x2) < f(x3):
                break
    if attempts == 1000:
        print("Nie da się znaleźć punktów x1 < x2 < x3 : f(x1) > f(x2) < f(x3) na zadanym przedziale.")
    else:
        maxi = 0
        while fabs(f(x1) - f(x2)) > epsilon and fabs(f(x1) - f(x3)) > epsilon and fabs(f(x2) - f(x3)) > epsilon:
            a0 = f(x1)
            a1 = (f(x2) - f(x1)) / (x2 - x1)
            a2 = (1 / (x3 - x2)) * (((f(x3) - f(x1)) / (x3 - x1)) - ((f(x2) - f(x1)) / (x2 - x1)))
            x0 = ((x1 + x2) / 2) - (a1 / (2*a2))
            points = pandas.DataFrame([(x1, f(x1)), (x2, f(x2)), (x3, f(x3)), (x0, f(x0))],
                                      columns=['x', 'f(x)'], index=['x1', 'x2', 'x3', 'x0'])
            if x0 < x2:
                if f(x0) < f(x2):
                    points = points.drop('x3')
                if f(x0) > f(x2):
                    points = points.drop('x1')
            if x0 > x2:
                if f(x0) < f(x2):
                    points = points.drop('x1')
                if f(x0) > f(x2):
                    points = points.drop('x3')
            points.sort_values('x',inplace=True)
            x1 = points.iloc[0, 0]
            x2 = points.iloc[1, 0]
            x3 = points.iloc[2, 0]
            maxi += 1
            if maxi > 3000:
                break
        if fabs(f(x1) - f(x2)) < epsilon:
            print(f"x_min ≈ {x1}\nf(x_min) ≈ {f(x1)}")
        elif fabs(f(x1) - f(x3)) < epsilon:
            print(f"x_min ≈ {x1}\nf(x_min) ≈ {f(x1)}")
        elif fabs(f(x2) - f(x3)) < epsilon:
            print(f"x_min ≈ {x2}\nf(x_min) ≈ {f(x2)}")

def nr():  # Newtona-Raphsona
    global A
    global B
    a = A
    b = B
    print("\nNewtona-Raphsona")
    print(f"(a,b) = {a, b}")
    xk_list = []
    xk = a
    dk = 0.01
    for i in range(1000):
        xkplus1 = xk - ((f(xk + dk) - f(xk - dk)) / (2 * dk)) / ((f(xk + dk) - 2 * f(xk) + f(xk - dk)) / dk ** 2)
        xk_list.append(xkplus1)
        xk = xkplus1
    print(f"x_eks ≈ {xk_list[-1]}\nf(x_eks) ≈ {f(xk_list[-1])}")

def ms():  # metoda siecznych
    global A
    global B
    a = A
    b = B
    print("\nSiecznych")
    print(f"(a,b) = {a, b}")
    dk = 0.1
    xk_list = [a, a + dk]
    for i in range(1,1000):
        if xk_list[i] - xk_list[i-1] == 0:
            break
        else:
            xkplus1 = xk_list[i] - ((xk_list[i] - xk_list[i-1])
                                     / (((f(xk_list[i] + dk) - f(xk_list[i] - dk))
                                         / (2 * dk)) - ((f(xk_list[i-1] + dk) - f(xk_list[i-1] - dk))
                                                        / (2 * dk)))) * ((f(xk_list[i] + dk) - f(xk_list[i] - dk)) / (2 * dk))
        xk_list.append(xkplus1)
    print(f"x_eks ≈ {xk_list[-1]}\nf(x_eks) ≈ {f(xk_list[-1])}")

def f(x):
    x4 = 2
    x3 = -0.5
    x2 = -4
    x1 = 2
    x0 = 1
    # return x4 * x ** 4 + x3 * x ** 3 + x2 * x ** 2 + x1 * x + x0
    return (x - 1) ** 2 + x + 1
    # return sin(x) + 1
    # return x ** 4 + 1
    # https://www.desmos.com/calculator/gkle1eve5v


A = 0
B = 5
epsilon = 0.001
pp()
wp()
dpp()
zp()
lf()
ik()
nr()
ms()
