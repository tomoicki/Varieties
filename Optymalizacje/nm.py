import pandas
import numpy


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)


def f(x):
    return (2 - x[0]) ** 2 + 12 * (x[1] - x[0] ** 2) ** 2


def centroid(xl, xs):
    return [(xl[0] + xs[0]) / 2, (xl[1] + xs[1]) / 2]


def reflection(x0, xh):
    return [(1 + 1) * x0[0] - 1 * xh[0], (1 + 1) * x0[1] - 1 * xh[1]]


def expansion(r, x0):
    return [2 * r[0] + (1 - 2) * x0[0], 2 * r[1] + (1 - 2) * x0[1]]


def contraction(xh, x0):
    return [0.5 * xh[0] + (1 - 0.5) * x0[0], 0.5 * xh[1] + (1 - 0.5) * x0[1]]


def shrinking(x, xl):
    return [0.5 * (x[0] + xl[0]), 0.5 * (x[1] + xl[1])]


def crit(xl, xh, xs, x0):
    return (((f(xl) - f(x0)) ** 2 + (f(xs) - f(x0)) ** 2 + (f(xh) - f(x0)) ** 2) / 2) ** 0.5


xl = [1, 1.3]
xl.append(f(xl))
xs = [-2, -1]
xs.append(f(xs))
xh = [1.5, 1]
xh.append(f(xh))
criteria = 999
epsilon = 0.0001
iterations = 0
while criteria > epsilon:
    iterations += 1
    dane = numpy.array([xl, xs, xh])
    dane = dane[dane[:, 2].argsort()]
    xl = list(dane[0])
    xs = list(dane[1])
    xh = list(dane[2])
    x0 = centroid(xl, xs)
    x0.append(f(x0))
    # 2)
    r = reflection(x0, xh)
    r.append(f(r))
    # 3)
    if r[2] < xl[2]:
        e = expansion(r, x0)
        e.append(f(e))
        # 3a)
        if e[2] < xl[2]:
            xh = e.copy()
            criteria = crit(xl, xh, xs, x0)
        # 3b)
        else:
            xh = r.copy()
            criteria = crit(xl, xh, xs, x0)
    # 4)
    elif xs[2] >= r[2] >= xl[2]:
        xh = r.copy()
        criteria = crit(xl, xh, xs, x0)
    # 5)
    elif xh[2] > r[2] > xs[2]:
        c = contraction(xh, x0)
        c.append(f(c))
        # 5a)
        if c[2] < xh[2]:
            xh = c.copy()
            criteria = crit(xl, xh, xs, x0)
        # 5b)
        else:
            xh = shrinking(xh, xl)
            xs = shrinking(xs, xl)
            criteria = crit(xl, xh, xs, x0)
    # 6)
    elif r[2] >= xh[2]:
        c = contraction(xh, x0)
        c.append(f(c))
        # 6a)
        if c[2] < xh[2]:
            xh = c.copy()
            criteria = crit(xl, xh, xs, x0)
        # 6b)
        else:
            xh = shrinking(xh, xl)
            xh.append(f(xh))
            xs = shrinking(xs, xl)
            xs.append(f(xs))
            criteria = crit(xl, xh, xs, x0)

    # df = pandas.DataFrame([xl, xs, xh, x0, r],
    #                       columns=['x', 'y', 'z'], index=['xl', 'xs', 'xh', 'x0', 'r'])
    # print(df)

print("\nMinimum funkcji ", xh)
# print('Number of iterations: ', iterations)
