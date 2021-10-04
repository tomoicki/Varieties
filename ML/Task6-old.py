import numpy
import pandas
from math import sqrt



numpy.set_printoptions(threshold=numpy.inf)
pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

print("NEAREST NEIGHBOR CLASSIFIER")
# while True:
#     train = input("Training set file? (e.g. train.txt): ")
#     try:
#         training_set = pandas.read_csv(train, header=None, sep='\s+', skiprows=[0])
#         break
#     except:
#         print("Cannot find corresponding file.")
# while True:
#     test = input("Testing set file? (e.g. test.txt): ")
#     try:
#         testing_set = pandas.read_csv(test, header=None, sep='\s+', skiprows=[0])
#         break
#     except:
#         print("Cannot find corresponding file.")
# while True:
#     res = input("Output file? (e.g. result.txt): ")
#     try:
#         output = open(res, "w")
#         break
#     except:
#         print("Cannot create "+res+" file.")

training_set = pandas.read_csv('iris_trn.txt', header=None, sep='\s+', skiprows=[0])
testing_set = pandas.read_csv('iris_tst.txt', header=None, sep='\s+', skiprows=[0])
output = open('res6.txt', 'w')

features = []
headers = ['class']
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
training_set.columns = headers
testing_set.columns = headers
kl = training_set['class'].values
x = training_set[features].values
klt = testing_set['class'].values
xt = testing_set[features].values
klp = numpy.zeros(len(kl), dtype=int)
m = training_set.index.size  # number of rows in training set
mt = testing_set.index.size
n = len(features)  # number of features
nc = len(set(kl))

# alternative, faster standarization
# mv = training_set.iloc[:, 1:].mean()
# std = training_set.iloc[:, 1:].std()
# s_training_set = (training_set - mv) / std
# s_testing_set = (training_set - mv) / std

vm = [0] * n
sd = [0] * n
for j in range(n):
    for i in range(m):
        vm[j] = vm[j] + x[i, j]
    vm[j] = vm[j] / m
    for i in range(m):
        sd[j] = sd[j] + (x[i, j] - vm[j]) ** 2
    sd[j] = sqrt(sd[j] / m)
for j in range(n):
    for i in range(m):
        x[i, j] = (x[i, j] - vm[j]) / sd[j]
    for k in range(mt):
        xt[k, j] = (xt[k, j] - vm[j]) / sd[j]

ikl = numpy.zeros((nc, nc), dtype=int)
ie = 0

print("Results of classification:")
for i in range(mt):
    dmin = 10 ** 10
    for k in range(m):
        d = 0
        for j in range(n):
            d = d + (x[k, j] - xt[i, j]) ** 2
            if d <= dmin:
                dmin = d
                klp[i] = kl[k]
    if klt[i] != klp[i]:
        ie += 1
    i1 = klt[i]
    i2 = klp[i]
    ikl[i1 - 1, i2 - 1] = ikl[i1 - 1, i2 - 1] + 1
    print(i, klt[i], klp[i])

a = 100 * ie/mt
print("Error rate: {}%".format(a))
print("Confusion matrix:")

