import math
import random

def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    liczba = input("Wpisz liczbę całkowietą dodatnią: ")
    if is_num(liczba) and int(liczba) > 0:
        break
liczba = int(liczba)
for i in range(liczba):
    i += 1
    if i/math.ceil(i/2) != 2:
        print(i)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    A = input("podaj liczbę całkowitą: ")
    if is_num(A):
        break
while True:
    B = input("podaj kolejną liczbę całkowitą, ale większą od A: ")
    if is_num(B) and int(B) > int(A):
        break
A = int(A)
B = int(B)
suma = 0
for i in range(A,B+1):
    suma = suma + i
print(suma)
suma = 0
i = A
while i < B+1:
    suma = suma + i
    i += 1
print(suma)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    n = input("Wpisz liczbę całkowietą dodatnią: ")
    if is_num(n) and int(n) > 0:
        break
n = int(n)
i = 0
while 2**i < n:
    print(2**i)
    i += 1
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
suma = 0
i = 1
while True:
    while True:
        x = input("Wpisz " + str(i) + ". liczbę całkowitą: ")
        if is_num(x):
            suma = suma + int(x)
            break
    i += 1
    if x == '0':
        break
print(suma)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
zestaw = []
i = 1
while True:
    while True:
        x = input("Wpisz " + str(i) + ". liczbę całkowitą: ")
        if is_num(x):
            if x != '0': zestaw.append(int(x))
            break
    i += 1
    if x == '0':
        break
w = max(zestaw)
m = min(zestaw)
s = w + m
mid = (w + m)/2
print(w,m,s,mid)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
x = random.randrange(1,100)
print(x)
while True:
    guess = input("Podaj liczbę całkowitą z zakresu od 1 do 100: ")
    if is_num(guess) and int(guess) in range(1,100):
        if int(guess) > x:
            print("Podałeś za duża wartość..")
            continue
        if int(guess) < x:
            print("Podałeś za małą wartość..")
            continue
        if int(guess) == x:
            print("Wygrałeś!")
            break
        break
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    x = input("Podaj współrzędną x lewego narożnika prostokąta (liczba całkowita dodatnia): ")
    if is_num(x) and int(x) > 0:
        break
while True:
    y = input("Podaj współrzędną y lewego narożnika prostokąta (liczba całkowita dodatnia): ")
    if is_num(y) and int(y) > 0:
        break
while True:
    a = input("Podaj długość poziomego boku prostokąta (liczba całkowita dodatnia): ")
    if is_num(a) and int(a) > 0:
        break
while True:
    b = input("Podaj długość pionowego boku prostokąta (liczba całkowita dodatnia): ")
    if is_num(b) and int(b) > 0:
        break
sign = input("Podaj symbol za pomocą którego narysujemy prostokąt: ")
x = int(x)
y = int(y)
a = int(a)
b = int(b)
print("\n"*(y-2))
for j in range(b):
    print(" "*(x-1)+sign*a)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    h = input("Podaj wysokość choinki (dodatnia liczba całkowita: ")
    if is_num(h) and int(h) > 0:
        break
h = int(h)
for i in range (h):
    for k in range(h-i):
        print(" ",end ="")
    for j in range(i*2+1):
        print("*",end="")
    print("")
#
def is_num(x):
    try:
        int(x)
        return True
    except:
        return False
while True:
     liczba = input("Podaj liczbę całkowitą: ")
     if is_num(liczba):
         break
sum = 0
sp = 0
sn = 0
for letter in liczba:
    sum = sum + int(letter)
    if int(letter)/math.ceil(int(letter)/2) < 2:
        sn += int(letter)
    else:
        sp += int(letter)
print(sum,sn,sp)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    liczba = input("Podaj liczbę całkowitą: ")
    if is_num(liczba):
        break
liczba = int(liczba)
dzielniki = []
for i in range(1,liczba+1):
    if liczba % i == 0:
        dzielniki.append(i)
print(dzielniki)
#
def is_num(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
while True:
    n = input("Podaj liczbę całkowitą: ")
    if is_num(n):
        break
n = int(n)
dzielniki = []
for i in range(1,n+1):
    if n % i == 0:
        dzielniki.append(i)
if len(dzielniki) == 2:
    print(n,"to liczba pierwsza")
else:
    print(n,"nie jest liczba pierwsza")