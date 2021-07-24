import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_moons
from sklearn.cross_validation import train_test_split


#generujemy dane w kształcie odwróconych księżyców
Data,Classes = make_moons(noise=0.2)

#Podział na część uczącą i testową
TrainData, TestData, TrainClasses, TestClasses = train_test_split(Data, Classes, test_size=.5)

#Parametry klasyfikatora SVM
svm=SVC(kernel="linear", C=0.1)

#wartość kroku
h=0.025
x_min, x_max = Data[:, 0].min() - .5, Data[:, 0].max() + .5
y_min, y_max = Data[:, 1].min() - .5, Data[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
#dane uczące
plt.scatter(TrainData[:, 0], TrainData[:, 1], c=TrainClasses, cmap=cm_bright)
#dane testowe
plt.scatter(TestData[:, 0], TestData[:, 1], c=TestClasses, cmap=cm_bright, alpha=0.6)
#wyświetlenie wykresu
plt.show()

#uczenie klasyfikatora
svm.fit(TrainData,TrainClasses)
#uzyskana sprawnosc
score = svm.score(TestData, TestClasses)
print('Sprawność na zbiorze testowym'
print(score

#Generujemy wykres powierzchni rozdzielającej
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=cm_bright, alpha=.8)
#Wyświetlenie elementów zbioru uczącego
plt.scatter(TrainData[:, 0], TrainData[:, 1], c=TrainClasses, cmap=cm_bright)
#Wyświetlenie elementów zbioru testowego
plt.scatter(TestData[:, 0], TestData[:, 1], c=TestClasses, cmap=cm_bright,alpha=0.6)
plt.show()