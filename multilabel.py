from sklearn.datasets import make_multilabel_classification
X, y = make_multilabel_classification(n_samples=100, n_features=2, n_classes=3, n_labels=2, random_state=1)
for i in range(100):
	print(X[i], y[i])