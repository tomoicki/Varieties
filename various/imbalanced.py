from numpy import where
from collections import Counter
from sklearn.datasets import make_classification
from matplotlib import pyplot


X, y = make_classification(n_samples=1000, n_features=3, n_informative=2, n_redundant=1, n_classes=2,
                           n_clusters_per_class=2, weights=[0.999,0.001], random_state=1)
counter = Counter(y)
for label, _ in counter.items():
	row_ix = where(y == label)[0]
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
pyplot.legend()
pyplot.show()