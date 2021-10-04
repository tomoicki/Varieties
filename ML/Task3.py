import numpy
import pandas


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

# print("Task3")
# while True:
#     train = input("Training set file? (e.g. train.txt): ")
#     try:
#         training_set = pandas.read_csv(train, header=None, sep='\s+', skiprows=[0])
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
training_set = pandas.read_csv('epj_trn.txt', header=None, sep='\s+', skiprows=[0])
# training_set = pandas.DataFrame([[1,2,4],[1,4,2],[1,4,4],[2,1,3],[2,3,1]])
output = open('res3.txt', 'w')

headers = ['class']
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
headers.append('cc')
training_set['cc'] = 1
training_set.columns = headers

# print('Pick a pair of classes out of the following set\n', training_set['class'].unique())
# while True:
#     class1 = input('First class: ')
#     try:
#         class1 = int(class1)
#         if class1 in training_set['class'].unique():
#             break
#         else:
#             print('Class you entered does not exist in our data set.')
#     except:
#         print('Wrong input type. Need an integer.')
# while True:
#     class2 = input('Second class: ')
#     try:
#         class2 = int(class2)
#         if class2 != class1:
#             if class2 in training_set['class'].unique():
#                 break
#             else:
#                 print('Class you entered does not exist in our data set.')
#         else:
#             print('Second class must be different than first.')
#     except:
#         print('Wrong input type. Need an integer.')
class1 = 1
class2 = 2

# while True:
#     max_iter = input('Maximum number of iterations? ')
#     try:
#         max_iter = int(max_iter)
#         break
#     except:
#         print('Wrong input type. Need an integer.')
max_iter = 1000

picked_class_set = training_set.loc[(training_set['class'] == class1) | (training_set['class'] == class2)]
picked_class_set.sort_index(inplace=True)
second_class_values_made_negative = picked_class_set.loc[picked_class_set['class'] == class2].applymap(lambda x: -x)
second_class_values_made_negative['class'] = second_class_values_made_negative['class'].apply(lambda x: -x)
increased = pandas.concat([picked_class_set.loc[picked_class_set['class'] == class1], second_class_values_made_negative])
increased.sort_index(inplace=True)
basic_set_length = increased.index.size
increased.reset_index(inplace=True, drop=True)
headers.remove('class')
j, same, number_of_corrections, msg = 0, 0, 0, 0
v = numpy.zeros(len(headers))
print(v)
x = increased[headers].values
while number_of_corrections < max_iter:
    v_old = v
    if j == basic_set_length:
        j = 0
    if numpy.dot(x[j], v) <= 0:
        v = x[j] + v
        number_of_corrections += 1
    if numpy.array_equal(v_old, v):
        same += 1
    else:
        same = 0
    if same >= basic_set_length:
        break
    j += 1
print(v)
headers.remove('cc')
picked_class_set.reset_index(inplace=True, drop=True)
picked_class_set['g'] = (picked_class_set[headers] * v[:len(headers)]).sum(axis=1) + v[len(headers)]
for i in range(basic_set_length):
    if picked_class_set.loc[i, 'g'] >= 0:
        picked_class_set.loc[i, 'class?'] = class1
    else:
        picked_class_set.loc[i, 'class?'] = class2
picked_class_set['Correct'] = numpy.where(picked_class_set['class'] == picked_class_set['class?'], 1, 0)
print("Error correction algorithm.", file=output)
print("\nNumber of correct decisions: ", picked_class_set['Correct'].sum(), file=output)
print("Training set size: ", basic_set_length, file=output)
print("Number of corrections: ", number_of_corrections, file=output)
h = [x.replace('y', 'v') for x in headers]
h.append('v_last')
weights = pandas.DataFrame(v.tolist(), index=h, columns=['Best weights'])
print('\n', weights, file=output)
print(picked_class_set.tail())
# input("Press any key to finish the program.")
