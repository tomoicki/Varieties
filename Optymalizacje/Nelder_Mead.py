import pandas
import random
import numpy
from scipy.optimize import minimize


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)


class Point:
    a = 1
    n = 4
    b = 10 + n

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        if z is None:
            # Rosenbrock
            self.z = (self.a - self.x) ** 2.0 + self.b * (self.y - self.x ** 2) ** 2
            # self.z = self.x ** 2 + self.y ** 2 + 1
            # self.z = self.x ** 2 - self.x + self.y ** 2 + 4 * self.y + 1
            # self.z = self.x ** 2 - self.x * self.y + self.y ** 2 - 2 * self.y + 2
            # self.z = self.x ** 2 + self.y ** 2 + self.x + self.y + 1
        else:
            self.z = z

    def values(self):
        return self.x, self.y, self.z

    def show(self):
        print(self.values())


def centroid():
    return Point((xl.x + xs.x) / 2, (xl.y + xs.y) / 2)


def reflection():
    alpha = 1
    return Point((1 + alpha) * x0.x - alpha * xh.x, (1 + alpha) * x0.y - alpha * xh.y)


def expansion():
    gamma = 2
    return Point(gamma * r.x + (1 - gamma) * x0.x, gamma * r.y + (1 - gamma) * x0.y)


def contraction():
    beta = 0.5
    return Point(beta * xh.x + (1 - beta) * x0.x, beta * xh.y + (1 - beta) * x0.y)


def shrinking(point2shrink):
    delta = 0.5
    return Point(delta * (point2shrink.x + xl.x), delta * (point2shrink.y + xl.y))


def crit():
    return (((xl.z - x0.z) ** 2 + (xs.z - x0.z) ** 2 + (xh.z - x0.z) ** 2) / 2) ** 0.5


# 0)
r_max = 9
r_min = -r_max
# xl = Point(random.randrange(r_min, r_max), random.randrange(r_min, r_max))
# xs = Point(random.randrange(r_min, r_max), random.randrange(r_min, r_max))
# xh = Point(random.randrange(r_min, r_max), random.randrange(r_min, r_max))
xl = Point(1,1.3)
xs = Point(-2,-1)
xh = Point(1.5,1)
# 1)
criteria = 999
epsilon = 0.0001
iterations = 0
while criteria > epsilon:
    iterations += 1
    path = ''
    path += '1'
    data = pandas.DataFrame([xl.values(), xs.values(), xh.values()], columns=['x', 'y', 'z'])
    data.sort_values('z', inplace=True)
    xl = Point(data.iloc[0, 0], data.iloc[0, 1], data.iloc[0, 2])
    xs = Point(data.iloc[1, 0], data.iloc[1, 1], data.iloc[1, 2])
    xh = Point(data.iloc[2, 0], data.iloc[2, 1], data.iloc[2, 2])
    x0 = centroid()
    # 2)
    path += ' -> 2'
    r = reflection()
    # 3)
    if r.z < xl.z:
        path += ' -> 3'
        e = expansion()
        # 3a)
        if e.z < xl.z:
            path += ' -> 3a'
            xh = e
            criteria = crit()
        # 3b)
        else:
            path += ' -> 3b'
            xh = r
            criteria = crit()
    # 4)
    elif xs.z >= r.z >= xl.z:
        path += ' -> 4'
        xh = r
        criteria = crit()
    # 5)
    elif xh.z > r.z > xs.z:
        path += ' -> 5'
        c = contraction()
        # 5a)
        if c.z < xh.z:
            path += ' -> 5a'
            xh = c
            criteria = crit()
        # 5b)
        else:
            path += ' -> 5b'
            xh = shrinking(xh)
            xs = shrinking(xs)
            criteria = crit()
    # 6)
    elif r.z >= xh.z:
        path += ' -> 6'
        c = contraction()
        # 6a)
        if c.z < xh.z:
            path += ' -> 6a'
            xh = c
            criteria = crit()
        # 6b)
        else:
            path += ' -> 6b'
            xh = shrinking(xh)
            xs = shrinking(xs)
            criteria = crit()
    df = pandas.DataFrame([xl.values(), xs.values(), xh.values(), x0.values(), r.values()],
                          columns=['x', 'y', 'z'], index=['xl', 'xs', 'xh', 'x0', 'r'])
    print(df)
    print(path)
    print()
minim = pandas.DataFrame([xh.values()], columns=['x', 'y', 'z'], index=[f'min (epsilon = {epsilon})'])
print(minim)
print('Number of iterations: ', iterations)

print('\nSprawdzenie funkcją scipy.optimize')
def func(x):
    a = 2
    n = 2
    b = 10 + n
    return (a-x[0])**2.0 + b*(x[1]-x[0]**2)**2.0
    # return x[0] ** 2 + x[1] ** 2 + 1
    # return x[0] ** 2 - x[0] + x[1] ** 2 + 4 * x[1] + 1
    # return x[0]**2 -x[0] * x[1] + x[1]**2 - 2*x[1] + 2

x = numpy.array([11,11])
result = minimize(func, x, method='nelder-mead')
solution = result['x']
evaluation = func(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))