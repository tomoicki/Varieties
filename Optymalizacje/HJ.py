import pandas
import random
import sys


sys.setrecursionlimit(3000)
pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)


class Point:
    def __init__(self, x):
        self.x = x

    def f(self):
        a = 1
        n = 4
        b = 10 + n
        # return (a - self.x[0]) ** 2.0 + b * (self.x[1] - self.x[0] ** 2) ** 2
        return self.x[0] - self.x[1] + 2 * self.x[0] ** 2 + 2 * self.x[0] * self.x[1] + self.x[1] ** 2
        # return self.x[0] ** 2 + self.x[1] ** 2 + 1 + self.x[0] + self.x[1]
        # return 6 * self.x[0] ** 2 - 2 * self.x[0] + 2 * self.x[1] ** 2 + 4 * self.x[1] + 3
        # return self.x[0] ** 2 * self.x[1] ** 2 + 2 * self.x[0] ** 2 + 3 * self.x[1] ** 2 - 5 * self.x[0] * self.x[1] + 4 * self.x[0] - self.x[1] + 5
    """
    https://www.geogebra.org/3d?lang=en
    m(x,y)=x-y + 2x^2 + 2xy + y^2
    z(x,y)=x^(2)+y^(2)+x+y+1
    f(x,y)=6 x^(2)+2 y^(2)-2 x+4 y+3
    g(x,y)=x^(2) y^(2)+2 x^(2)+3 y^(2)-5 x y+4 x-y+5
    """

    def __add__(self, other):
        return Point([sum(item) for item in zip(self.values(), other.values())])

    def __sub__(self, other):
        return Point([(a - b) for a, b in zip(self.values(), other.values())])

    def __rmul__(self, other):
        return Point([other * item for item in self.values()])

    def __mul__(self, other):
        if str(other) == "Point":
            return Point([(a * b) for a, b in zip(self.values(), other.values())])
        if type(other) == float:
            return self.__rmul__(other)

    def __str__(self):
        return "Point"

    def values(self):
        return self.x

    def show(self):
        print(self.values())

def probny(x0, xB0, delta):
    global iters
    iters += 1
    pomyslne = False
    F0 = x0.f()
    z = xB0
    for i in range(len(x0.x)):
        z.x[i] = z.x[i] + delta
        F = z.f()
        if F < F0:
            F0 = F
            pomyslne = True
        else:
            z.x[i] = z.x[i] - 2 * delta
            F = z.f()
            if F < F0:
                F0 = F
                pomyslne = True
    if pomyslne is False and iters == 1:
        iters = 0
        x0 = Point([random.randrange(-10, 10),random.randrange(-10, 10)])
        probny(x0, xB0, delta)
    elif pomyslne is False and iters != 1:
        if delta >= epsilon:
            delta = delta * beta
            probny(x0, xB0, delta)
        else:
            print(f"x_min ≈ {x0.values()}\nf(x_min) ≈ {x0.f()}")
    elif iters > 2000:
        print(f"x_min ≈ {x0.values()}\nf(x_min) ≈ {x0.f()}")
    elif pomyslne:
        xB = z
        x0, xB0 = roboczy(xB, xB0)
        probny(x0, xB0, delta)

def roboczy(xB, xB0):
    x0 = 2 * xB - xB0
    xB0 = xB
    return x0, xB0

epsilon = 0.001
delta = epsilon + 0.01
beta = 0.5
x0 = Point([11,11])
z, xB0 = x0, x0
iters = 0
probny(x0, z, delta)
