from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot


X, y = make_blobs(n_samples=150, centers=2, random_state=0)
# Z, a = make_blobs(n_samples=100, centers=2, random_state=1)
counter = Counter(y)
# countera = Counter(a)
for label, _ in counter.items():
	row_ix = where(y == label)[0]
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
# for label, _ in countera.items():
# 	row_ix = where(a == label)[0]
# 	pyplot.scatter(Z[row_ix, 0], Z[row_ix, 1], label=str(label),color='black')
pyplot.legend()
pyplot.show()