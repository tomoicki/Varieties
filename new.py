import numpy as np
import matplotlib.pyplot as plt

#definicje funkcji klasyfikujących
def g1(x):
    return x[0]+x[1]

def g2(x):
    return -x[0]-x[1]

#klasyfikator
def klasyfikuj(x):
    if g1(x)>g2(x):
        return 1
    else:
        return 2

#liczba próbek w klasie
N = 5

#próba losowa z rozkładu jednostajnego na przedziale [1,5]
class1 = np.random.rand(N,2)
class2 = np.random.rand(N,2)-1

data=np.vstack((class1,class2))

#wykres przedstawiający dane do testowania oraz powierzchnię rozdzielającą
#zakres wartości na osiach
plt.ylim(ymax = 1.5, ymin = -1.5)
plt.xlim(xmax = 1.5, xmin = -1.5)
#dane uczące
plt.scatter(data[:,0],data[:,1])
#powierzchnia rozdzielająca
plt.plot([-1.5, 1.5],[1.5, -1.5])
plt.show()

#wartości funkcji klasyfikujących
y1=[g1(data[i,:]) for i in range(2*N)]
y2=[g2(data[i,:]) for i in range(2*N)]
#zaokrąglenie
y1=np.round(y1,2)
y2=np.round(y2,2)
print('Wartości funkcji klasyfikujacych')
print(y1)
print(y2)

#wyznaczamy decyzje klasyfikatora (numer funkcji klasyfikującej zwracającej większą wartość)
labels=np.array([klasyfikuj(data[i,:]) for i in range(2*N)])
print('Decyzje klasyfikatora:')
print(labels)

#numery próbek zakalsyfikowane do kazdej z klas
c1 = (labels==1).nonzero()
c2 = (labels==2).nonzero()

#wykres przedstawiający dane oraz powierzchnię rozdzielającą
#klasę w zależności od decyzji klasyfikatora zaznaczamy kolorem
plt.ylim(ymax = 1.5, ymin = -1.5)
plt.xlim(xmax = 1.5, xmin = -1.5)
#dane testowe - klasa1 kolor niebieski, klasa2 kolor czerwony
plt.scatter(data[c1,0],data[c1,1],c='b')
plt.scatter(data[c2,0],data[c2,1],c='r')
#powierzchnia rozdzielająca
plt.plot([-1.5, 1.5],[1.5, -1.5])
plt.show()