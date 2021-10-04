import pandas


def AB():
    print("\nPoint A: ", end=' ', file=output)
    for k in range(n):
        print(round(a[k], 4), end=' ', file=output)
    print("\nPoint B: ", end=' ', file=output)
    for k in range(n):
        print(round(b[k], 4), end=' ', file=output)

def test():
    ii = m1 + m2
    for i in range(ii):
        print("\n", lw[i + 1], end=' ', file=output)
        for k in range(n):
            print(z[i + 1, k], end=' ', file=output)

def dst():
    ds = 0
    for k in range(n):
        ds = ds + (a[k] - b[k]) ** 2
    return ds

def war1():
    for k in range(n):
        c1[k] = (a[k] - b[k])
    for k in range(n):
        c2[k] = (z[j, k] - a[k])
    war = 0
    for k in range(n):
        war = war + c1[k] * c2[k]
    return war

def war2():
    for k in range(n):
        c1[k] = (b[k] - a[k])
    for k in range(n):
        c2[k] = (z[j, k] - b[k])
    war = 0
    for k in range(n):
        war = war + c1[k] * c2[k]
    return war

def za2():
    for s in range(n):
        c2[k] = z[j, s] - a[s]
    war = 0
    for ss in range(n):
        war = war + c2[ss] ** 2
    return war + 0.00000001

def zb2():
    for k in range(n):
        c2[k] = z[j, k] - b[k]
    war = 0
    for k in range(n):
        war = war + c2[k] ** 2
    return war + 0.00000001

def dxa(i):
    war = 0
    for k in range(n):
        war = war + (x[i, k] - a[k]) ** 2
    return war

def dxb(i):
    war = 0
    for k in range(n):
        war = war + (x[i, k] - b[k]) ** 2
    return war

training_set = pandas.read_csv('epj_trn.txt', header=None, sep='\s+', skiprows=[0])
output = open('iris_res5.txt', 'w')

headers = ['class']
features = []
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
training_set.columns = headers

class1 = 1
class2 = 2

delta1 = 0.1
delta2 = -0.001

m = training_set.index.size  # number of rows in training set
n = len(features)  # number of features

lv = training_set['class'].values
lw = [0] * len(lv)
x = training_set[features].values
z = x.copy()
first_class_values = training_set.loc[training_set['class'] == class1]
second_class_values = training_set.loc[training_set['class'] == class2]
m1 = first_class_values.index.size
m2 = second_class_values.index.size
minn = min(m1, m2)

k1, k2, k = 0, 0, 0
for ii in range(m):
    if lv[ii] == class1 and k1 <= minn:
        k1 += 1
        i = 2 * (k1 - 1) + 1
        lw[i] = lv[ii]
        for j in range(n):
            z[i, j] = x[ii, j]
    if lv[ii] == class1 and k1 > minn:
        k += 1
        i = 2 * minn + k
        lw[i] = lv[ii]
        for j in range(n):
            z[i, j] = x[ii, j]
    if lv[ii] == class2 and k2 <= minn:
        k2 += 1
        i = 2 * k2
        lw[i] = lv[ii]
        for j in range(n):
            z[i, j] = x[ii, j]
    if lv[ii] == class2 and k2 > minn:
        k += 1
        i = 2 * minn + k
        lw[i] = lv[ii]
        for j in range(n):
            z[i, j] = x[ii, j]
a = []
b = []
for j in range(n):
    a.append(z[1, j])
    b.append(z[2, j])

c1 = [0] * len(a)
c2 = [0] * len(a)

print("Ordered training set:", file=output)
test()
j = 1
lcz = 0
while True:
    lcz += 1
    if j >= m - 1:
        j = 0
    else:
        j += 1
    if lw[j] == class1 and war1() < delta2:
        t = 0
        lcz = 0
        for k in range(n):
            t = t + (z[j, k] - a[k]) * (b[k] - a[k])/za2()
            if t < 1:
                for k in range(n):
                    a[k] = a[k] + t * (z[j, k] - a[k])
            else:
                for k in range(n):
                    a[k] = z[j, k]
    if lw[j] == class2 and war2() < delta2:
        t = 0
        lcz = 0
        for k in range(n):
            t = t + (z[j, k] - b[k]) * (a[k] - b[k])/zb2()
            if t < 1:
                for k in range(n):
                    b[k] = b[k] + t * (z[j, k] - b[k])
            else:
                for k in range(n):
                    b[k] = z[j, k]
    ds = dst()
    AB()

    print("\nObject nr {}; Distance between A and B: {}".format(j, round(ds, 4)), end=' ', file=output)
    print("\tlcz: ", lcz, file=output)

    if dst() < delta1:
        print("\nTHE SETS ARE LINEARLY INSEPARABLE\n", file=output)
        break
    if lcz == m1 + m2:
        print("\nTHE SETS ARE LINEARLY SEPARABLE\n", file=output)
        break

print("Verification:", file=output)
for i in range(m):
    if lv[i] == class1 or lv[i] == class2:
        kl = class2
        if dxa(i) <= dxb(i):
            kl = class1
        print("True class: {}\tAssigned class: {}".format(lv[i], kl), file=output)
