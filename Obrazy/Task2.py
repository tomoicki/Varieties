import numpy
import pandas

pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

print("Task2")
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

# training_set = pandas.read_csv('epj_trn.txt', header=None, sep='\s+', skiprows=[0])
# testing_set = pandas.read_csv('epj_tst.txt', header=None, sep='\s+', skiprows=[0])
# output = open('epj_res2.txt', 'w')

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
W = Ps * 2
W['last'] = (-1) * ((Ps ** 2).sum(axis=1))
print('\nWeights before including standardisation:\n', W, file=output)
Ws = W.drop('last', axis=1) / std
Ws['last'] = W['last'] - (Ws * mv).sum(axis=1)
print('\nWeights before including standardisation:\n', Ws, file=output)
g = pandas.DataFrame(testing_set['class'])
for i in range(len(Ps.index)):
    squared = (testing_set.drop('class', axis=1) * Ws.drop('last', axis=1).iloc[i])
    squared.dropna(axis=1, inplace=True)
    g[i + 1] = squared.sum(axis=1) + Ws['last'].iloc[i]
g['max'] = g.drop('class', axis=1).max(axis=1)
ifs = []
for i in range(len(Ps.index)):
    ifs.append('if' + str(i + 1))
    g[ifs[i]] = numpy.where(g[i + 1] == g['max'], i + 1, 0)
g['class?'] = g.loc[g.index, ifs].sum(axis=1)
g['Error'] = numpy.where(g['class'] != g['class?'], 1, 0)
res_df = pandas.DataFrame(index=g.index)
res_df.index.name = "Nr obj"
res_df['True class'] = g['class']
res_df['Assigned class'] = g['class?']
print('\nResults of classification\n', res_df, file=output)
print('\nErrors: ', g['Error'].sum(), file=output)
print('Error rate: ', round((g['Error'].sum() / len(g.index)) * 100, 1), '%', file=output)
conf_matrix = g.groupby('class').sum()
conf_matrix = conf_matrix.loc[conf_matrix.index, ifs]
conf_matrix.reset_index(inplace=True, drop=True)
conf_matrix.index = conf_matrix.index + 1
conf_matrix.columns = conf_matrix.index
conf_matrix = (conf_matrix / conf_matrix.index).applymap(int)
print('\nConfussion matrix:\n', conf_matrix, file=output)
apriori = conf_matrix / testing_set['class'].value_counts()
print('\nProbabilities a priori:\n', apriori, file=output)
aposteriori = (conf_matrix/conf_matrix.sum(axis=0)).transpose()
print('\nProbabilities a posteriori:\n', aposteriori, file=output)
# input("Press any key to finish the program.")
