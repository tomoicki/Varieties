import matplotlib.pyplot as plt

# 1. regresja liniowa
# dane
x = []
n = 20
for i in range(n):
    x.append(i)
y = [111,115,113,118,114,114,115,119,120,123,118,117,119,121,122,120,122,125,128,124]

xy = []
for i in range(len(x)):
    xy.append(x[i]*y[i])
sum_xy = sum(xy)
sum_x = sum(x)
sum_y = sum(y)
x2 = []
for i in range(len(x)):
    x2.append(x[i] * x[i])
sum_x2 = sum(x2)
b = (sum_xy - 1/n * sum_x * sum_y) / (sum_x2 - 1/n * sum_x * sum_x)
a = sum_y/n - b * sum_x / n
bxa = []
for i in range(len(x)):
    bxa.append(x[i]*b+a)

plt.plot(x,y,linestyle="",marker=".")
plt.plot(x,bxa)
plt.show()

# 2. regresja kwadratowa
# dane
xt = []
n = 20
for i in range(n):
    xt.append(i+1)
yt = [112,115,113,118,114,114,115,119,120,121,118,117,119,115,113,117,116,113,115,110]
x = sum(xt)
y = sum(yt)

x2t = []
x3t = []
x4t = []
for i in range(n):
    x2t.append(xt[i] ** 2)
    x3t.append(xt[i] ** 3)
    x4t.append(xt[i] ** 4)
x2 = sum(x2t)
x3 = sum(x3t)
x4 = sum(x4t)

xyt = []
x2yt = []
for i in range(n):
    xyt.append(xt[i]*yt[i])
    x2yt.append(xt[i]**2*yt[i])
xy = sum(xyt)
x2y = sum(x2yt)

#w = n*x2*x4+x*x3*x2+x2*x*x3-n*x3*x3-x*x*x4-x2*x2*x2
#wb = n*xy*x4+y*x3*x2+x2*x*x2y-n*x3*x2y-y*x*x4-x2*xy*x2
#wc = n*x2*x2y+x*xy*x2+y*x*x3-n*xy*x3-x*x*x2y-y*x2*x2
#b = wb / w
#c = wc / w
c = (((x2y-(x2*y)/n)*(x2-(x**2)/n))-((xy-(x*y)/n)*(x3-(x2*x)/n)))/(((x2-(x**2)/n)*(x4-(x2**2)/n))-(x3-(x2*x)/n)**2)
#b = (((xy-(x*y)/n)*(x4-(x2**2)/n))-((x2y-(x2*y)/n)*(x3-(x2*x)/n)))/(((x2-(x**2)/n)*(x4-(x2**2)/n))-(x3-(x2*x)/n)**2)
b = (xy-x*y/n-c*(x3-x*x2/n))/(x2-x**2/n)
a = (1/n)*(y-b*x-c*x2)
fx = []
for i in range(n):
    fx.append(a + b * xt[i] + c * xt[i]**2)

plt.plot(xt,yt,linestyle="",marker=".")
plt.plot(xt,fx)
plt.show()