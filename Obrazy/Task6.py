import numpy
import pandas
import collections


numpy.set_printoptions(threshold=numpy.inf)
pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

print("\nNEAREST NEIGHBOR CLASSIFIER\n")
while True:
    train = input("Training set file? (e.g. train.txt): ")
    try:
        training_set = pandas.read_csv(train, header=None, sep='\s+', skiprows=[0])
        break
    except:
        print("Cannot find corresponding file.")
while True:
    test = input("Testing set file? (e.g. test.txt): ")
    try:
        testing_set = pandas.read_csv(test, header=None, sep='\s+', skiprows=[0])
        break
    except:
        print("Cannot find corresponding file.")
while True:
    res = input("Output file? (e.g. result.txt): ")
    try:
        output = open(res, "w")
        break
    except:
        print("Cannot create "+res+" file.")

# training_set = pandas.read_csv('iris_trn.txt', header=None, sep='\s+', skiprows=[0])
# testing_set = pandas.read_csv('iris_tst.txt', header=None, sep='\s+', skiprows=[0])
# output = open('res6.txt', 'w')

print('Number of neighbours. Number from 1 to', training_set.index.size)
while True:
    k = input("k = ")
    try:
        k = int(k)
        if k <= training_set.index.size:
            break
        else:
            print('Too high number. training set has only {} specimens.'.format(training_set.index.size))
    except:
        print('Wrong input type. Need an integer.')
# k = 20

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
m = training_set.index.size  # number of rows in training set
mt = testing_set.index.size
n = len(features)  # number of features
classes = list(set(kl))
nc = len(classes)
def kNN(k):
    temp = numpy.empty(len(klt))
    for i in range(mt):
        specimen = xt[i]
        specimen_class = klt[i]
        # euclidean distance from test specimen to every specimen in training set
        distances = numpy.linalg.norm(x - specimen, axis=1)
        # list of IDs of closest k Neighbours
        nearest_neighbor_ids = distances.argsort()[:k]
        # list of classes of closest k Neighbours
        nearest_neighbor_classes = numpy.take(kl, nearest_neighbor_ids)
        # counts of each class
        counter = collections.Counter(nearest_neighbor_classes)
        counter_max = counter[max(counter, key=counter.get)]
        max_classes = [i for i in counter.keys() if counter[i] == counter_max]
        if len(max_classes) == 1:
            specimen_assigned_class = max_classes[0]
        else:
            if specimen_class in max_classes:
                specimen_assigned_class = specimen_class
            else:
                specimen_assigned_class = max(max_classes)
        # print("\nObject: ", specimen)
        # print("k =", k, "\n", counter)
        # print("True class: {}\t{} :Assigned class".format(specimen_class, specimen_assigned_class))
        temp[i] = specimen_assigned_class
    return temp


klt_assigned = kNN(k)
print("\nResults of classification.", file=output)
class_comparison = pandas.DataFrame({'True class': klt, 'Assigned class': klt_assigned})
class_comparison = class_comparison.applymap(int)
print("\nk = ", k, file=output)
print(class_comparison, file=output)
errors = (numpy.where(class_comparison['True class'] != class_comparison['Assigned class'], 1, 0)).sum()
print('\nErrors: ', errors, file=output)
print('Error rate: ', round((errors / class_comparison.index.size) * 100, 1), '%', file=output)

conf_array_of_arrays = []
for j in range(nc):
    conf_array = []
    onlys = class_comparison.loc[class_comparison['True class'] == classes[j]]
    for i in range(nc):
        conf_array.append(numpy.where(onlys['Assigned class'] == classes[i], 1, 0).sum())
    conf_array_of_arrays.append(conf_array)
confusion_matrix = pandas.DataFrame(conf_array_of_arrays, index=classes, columns=classes)

pandas.set_option('colheader_justify', 'left')
print('\nConfusion matrix:\n', confusion_matrix, file=output)
apriori = confusion_matrix / class_comparison['True class'].value_counts()
aposteriori = (confusion_matrix / confusion_matrix.sum()).T
apriori = apriori.applymap('{:,.4f}'.format)
aposteriori = aposteriori.applymap('{:,.4f}'.format)
pandas.set_option('colheader_justify', 'center')
print('\nProbabilities a priori:\n', apriori, file=output)
print('\nProbabilities a posteriori:\n', aposteriori, file=output)

print("Calculations for k = {} already done.\n".format(k))
print("Want to add comparison of error rates for various k?\n(it can take a while depending on the training set)")

while True:
    yesno = input("Type y or n: ").lower()
    if yesno in ['y', 'n', 'yes', 'no']:
        break
    else:
        print("Simple 'y' or 'n' will be enough.")
# yesno = 'n'

if yesno == 'y':
    list_of_k = []
    list_of_error_rates = []
    for k in range(1, training_set.index.size):
        klt_assigned = kNN(k)
        errors = (numpy.where(klt != klt_assigned, 1, 0)).sum()
        error_rate = round((errors / class_comparison.index.size) * 100, 2)
        list_of_k.append(k)
        list_of_error_rates.append(error_rate)
    k2error = pandas.DataFrame({'k': list_of_k, 'Error rate [%]': list_of_error_rates})

    print("\nComparison of error rates for various k", file=output)
    print(k2error.to_string(index=False), file=output)
    min_er = k2error.iloc[:, 1].min()
    max_er = k2error.iloc[:, 1].max()
    print("\nLowest error rate:", file=output)
    print(k2error.loc[k2error["Error rate [%]"] == min_er].to_string(index=False), file=output)
    print("\nHighest error rate:", file=output)
    print(k2error.loc[k2error["Error rate [%]"] == max_er].to_string(index=False), file=output)
    print("\nDone for k ∈ [{},{}]".format(1, training_set.index.size))

# input("Press any key to finish the program.")
