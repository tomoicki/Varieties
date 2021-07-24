import numpy
import pandas

pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

print("Task1")
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
# output = open('iris_res1.txt', 'w')

headers = ['class']
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('v' + str(i + 1))
training_set.columns = headers
testing_set.columns = headers
mv = training_set.mean()
mv.drop('class', inplace=True)
std = training_set.std()
std.drop('class', inplace=True)
P = training_set.groupby(['class']).mean()
print('Class gravity centers before standardisation:\n', P, file=output)
Ps = ((P - mv) / std)
print('\nClass gravity centers after standardisation:\n', Ps, file=output)
standarized_testing_set = (testing_set - mv) / std
standarized_testing_set['class'] = testing_set['class']
d = pandas.DataFrame(testing_set['class'])
for i in range(len(Ps.index)):
    squared = (standarized_testing_set - Ps.iloc[i]) ** 2
    squared.dropna(axis=1, inplace=True)
    d[i + 1] = squared.sum(axis=1)
d['min'] = d.drop('class', axis=1).min(axis=1)
ifs = []
for i in range(len(Ps.index)):
    ifs.append('if' + str(i + 1))
    d[ifs[i]] = numpy.where(d[i + 1] == d['min'], i + 1, 0)
d['class?'] = d.loc[d.index, ifs].sum(axis=1)
d['Error'] = numpy.where(d['class'] != d['class?'], 1, 0)
res_df = pandas.DataFrame(index=d.index)
res_df.index.name = "Nr obj"
res_df['True class'] = d['class']
res_df['Assigned class'] = d['class?']
print('\nResults of classification\n', res_df, file=output)
print('\nErrors: ', d['Error'].sum(), file=output)
print('\nError rate: ', round((d['Error'].sum() / len(d.index)) * 100, 1), '%', file=output)
# input("Press any key to finish the program.")
