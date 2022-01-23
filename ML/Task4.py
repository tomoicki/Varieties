import pandas


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

def gb(i):
    g = 0
    for j in range(len(features)):
        g = g + ab[j] * (x[i, j] - b[j])
    return g

def gcd(i, icd):
    g = 0
    for j in range(len(features)):
        g = g + ab[j] * (x[i, j] - x[icd, j])
    return g

def hip(i):
    return gcd(i, ic) + gcd(i, idd)

eps = 0.0001
while True:
    train = input("Training set file? (e.g. train.txt): ")
    try:
        training_set = pandas.read_csv(train, header=None, sep='\s+', skiprows=[0])
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
# training_set = pandas.read_csv('epj_trn.txt', header=None, sep='\s+', skiprows=[0])
# output = open('epj_res4.txt', 'w')

headers = ['class']
features = []
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
training_set.columns = headers

print('Pick a pair of classes out of the following set\n', training_set['class'].unique())
while True:
    class1 = input('First class: ')
    try:
        class1 = int(class1)
        if class1 in training_set['class'].unique():
            break
        else:
            print('Class you entered does not exist in our data set.')
    except:
        print('Wrong input type. Need an integer.')
while True:
    class2 = input('Second class: ')
    try:
        class2 = int(class2)
        if class2 != class1:
            if class2 in training_set['class'].unique():
                break
            else:
                print('Class you entered does not exist in our data set.')
        else:
            print('Second class must be different than first.')
    except:
        print('Wrong input type. Need an integer.')
# class1 = 2
# class2 = 3

print("\nTraining set editing for linear separability.", file=output)
m = training_set.index.size  # number of rows in training set
n = len(features)  # number of features

kl = training_set['class'].values
clo = kl.tolist()
x = training_set[features].values
first_class_values = training_set.loc[training_set['class'] == class1]
a = first_class_values.mean().tolist()
second_class_values = training_set.loc[training_set['class'] == class2]
b = second_class_values.mean().tolist()
# mean feature i of class1 - mean feature i of class2
ab = (first_class_values.mean() - second_class_values.mean()).tolist()
del ab[0], a[0], b[0]
lcz = 0
ic, idd = 0, 0
while gb(ic) <= gb(idd):
    ic, idd = 0, 0
    minn = 10**10
    maxx = -10**10
    lcz += 1
    for i in range(m):
        gb_value = gb(i)
        if gb_value < minn and kl[i] == class1:
            minn = gb_value
            ic = i
    for i in range(m):
        gb_value = gb(i)
        if gb_value > maxx and kl[i] == class2:
            maxx = gb_value
            idd = i
    l1 = 0
    for i in range(m):
        if kl[i] == class1 and gcd(i, ic) > -eps and gcd(i, idd) < eps:
            l1 += 1
    l2 = 0
    for i in range(m):
        if kl[i] == class2 and gcd(i, ic) > -eps and gcd(i, idd) < eps:
            l2 += 1
    if l1 > l2:
        kl[idd] = 0
    if l1 < l2:
        kl[ic] = 0
    if l1 == l2 and l1 > 0:
        kl[ic] = 0
        kl[idd] = 0
    print("\nRun number {}: Extreme objects: {} and {}\nfrom the classes {} and {} respectively"
          .format(lcz, ic+1, idd+1, clo[ic], clo[idd]), file=output)
    print("l1 = {}\t\tl2 = {}".format(l1, l2), file=output)
    if kl[idd] == 0:
        print('Rejected object nr {} from the class {}'.format(idd+1, clo[idd]), file=output)
    if kl[ic] == 0:
        print('Rejected object nr {} from the class {}'.format(ic+1, clo[ic]), file=output)
    if l1 == l2 and l1 == 0:
        print('No objects rejected. Success.', file=output)

ie = 0
clp = [0]*m
for i in range(m):
    if clo[i] == class1 or clo[i] == class2:
        if hip(i) < 0:
            clp[i] = class2
        else:
            clp[i] = class1
        if clo[i] != clp[i]:
            ie += 1
if ie > 0:
    print("\nRemoved objects:", file=output)
    iu = 0
    removeds = pandas.DataFrame(columns=['Object', 'Class'])
    for i in range(m):
        if kl[i] == 0 and (clo[i] == class1 or clo[i] == class2):
            removeds.loc[i, 'Object'] = i+1
            removeds.loc[i, 'Class'] = clo[i]
            iu += 1
    print(removeds.to_string(index=False), file=output)
    print('\nMisclassified objects from the selected class pair:', file=output)
    missclass = pandas.DataFrame(columns=['Object', 'True Class', 'Assigned Class'])
    for i in range(m):
        if clo[i] != clp[i] and (clo[i] == class1 or clo[i] == class2):
            missclass.loc[i, 'Object'] = i+1
            missclass.loc[i, 'True Class'] = clo[i]
            missclass.loc[i, 'Assigned Class'] = clp[i]
    print(missclass.to_string(index=False), file=output)
    print('\nNumber of runs = ', lcz, '; number of errors = ', ie, ' number of rejections = ', iu)
# input("Press any key to finish the program.")
