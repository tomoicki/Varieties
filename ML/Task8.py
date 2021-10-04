import numpy
import pandas


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)


def modul_odleglosci(punkt1, punkt2):
    suma = 0
    for i in range(len(punkt1)):
        suma += ((punkt1[i] - punkt2[i]) ** 2)
    return suma**0.5


# print("\nPary Tomekowe.\n")
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
training_set = pandas.read_csv('dane7.txt', header=None, sep='\s+', skiprows=[0])
output = open('res888.txt', 'w')

features = []
headers = ['class']
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
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

to_numpy = training_set.drop(columns=['class'])
numpy_training = to_numpy.values
n = len(features)  # number of features
first_class_values = training_set.loc[training_set['class'] == class1]
a = first_class_values[features].values
second_class_values = training_set.loc[training_set['class'] == class2]
b = second_class_values[features].values
print("\nZadanie numer 8.", file=output)
for i in range(len(a)):
    specimen_a = a[i]
    a_without_specimen_a = numpy.delete(a, i, 0)
    for j in range(len(b)):
        specimen_b = b[j]
        b_without_specimen_b = numpy.delete(b, j, 0)
        a2b = modul_odleglosci(specimen_a, specimen_b)
        point = 0
        radius = a2b / 2
        center = (specimen_a + specimen_b) / 2
        center_to_b = []
        for i in range(len(b_without_specimen_b)):
            center_to_b.append(modul_odleglosci(b_without_specimen_b[i], center))
        center_to_a = []
        for i in range(len(a_without_specimen_a)):
            center_to_a.append(modul_odleglosci(a_without_specimen_a[i], center))
        index_specimen_a, index_specimen_b = 0, 0
        for i in range(len(numpy_training)):
            if numpy.array_equal(numpy_training[i], specimen_a):
                index_specimen_a = i + 1
            if numpy.array_equal(numpy_training[i], specimen_b):
                index_specimen_b = i + 1
        yesA = 0
        yesB = 0
        if radius >= min(center_to_a):
            yesA = 1
            # print("W hiperkuli ab znajduje się co najmniej 1 obiekt z a")
        # print("Odległości ze srodka hiperkuli do obiektów z klasy {}\n{}".format(class2, center_to_b))
        if radius >= min(center_to_b):
            yesB = 1
            # print("W hiperkuli ab znajduje się co najmniej 1 obiekt z b")
        if yesA + yesB == 0:
            print(f"Punkt nr {index_specimen_a} o wspolrzednych {specimen_a} oraz punkt nr {index_specimen_b} o wspolrzednych {specimen_b} sa para Tomekowa.", file=output)
            # print("utworzyły hiperkulę o promieniu {} i środku w punkcie \n{}".format(radius, center))
            # print("Odległości ze srodka hiperkuli do obiektów z klasy \n{}".format(center_to_a))


