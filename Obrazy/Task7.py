import numpy
import pandas


pandas.set_option('display.width', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('colheader_justify', 'center')
pandas.set_option('display.show_dimensions', False)
pandas.set_option('display.max_rows', None)

print("\nProgram for class areas determination.\n")
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

# training_set = pandas.read_csv('iris_trn.txt', header=None, sep='\s+', skiprows=[0])
# output = open('res7.txt', 'w')

features = []
headers = ['class']
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
training_set.columns = headers
kl = training_set['class'].values
m = training_set.index.size  # number of rows in training set
n = len(features)  # number of features
classes = list(set(kl))
nc = len(classes)
indexes_list = training_set.index.values.tolist()
class_df = []
for i in classes:
    class_df.append(training_set.loc[training_set['class'] == i])
list_of_max_d = []
for df in class_df:
    x = df[features].values
    list_of_distances_to_closest_neighbour = []
    for i in range(df.index.size - 1):
        specimen = x[i]
        deleted = numpy.delete(x, i, 0)
        distances = numpy.linalg.norm(deleted - specimen, axis=1)
        distance_to_closest_neighbour = min(distances)
        list_of_distances_to_closest_neighbour.append(distance_to_closest_neighbour)
    list_of_max_d.append((max(list_of_distances_to_closest_neighbour)))
d_df = pandas.DataFrame([list_of_max_d], columns=classes, index=['d'])
overlapping = pandas.DataFrame(index=training_set.index, columns=classes)
for df in class_df:
    specimens = df[features].values
    specimens_class = df['class'].values
    class_df_removed = [item for item in class_df if item is not df]
    for i in range(df.index.size):
        specimen = specimens[i]
        specimen_class = specimens_class[i]
        specimen_id = indexes_list.pop(0)
        overlapping.loc[specimen_id, df.iloc[0, 0]] = 1
        for df_to_compare_with in class_df_removed:
            to_compare_with = df_to_compare_with[features].values
            class_distance = d_df.loc['d', df_to_compare_with.iloc[0, 0]]
            distances = numpy.linalg.norm(to_compare_with - specimen, axis=1)
            # print("Obiekt nr:", specimen_id, "Klasa:", specimen_class, "Cechy:", specimen)
            # print("max(odleglosci do NN) w klasie {}: {}".format(df_to_compare_with.iloc[0, 0], class_distance))
            # print("Macierz odleglosci obiektu do każdego z klasy {}: \n{}\n"
            #       .format(df_to_compare_with.iloc[0, 0], distances))
            if class_distance >= min(distances):
                overlapping.loc[specimen_id, df_to_compare_with.iloc[0, 0]] = 1
            else:
                overlapping.loc[specimen_id, df_to_compare_with.iloc[0, 0]] = 0
overlapping.rename(columns=lambda i: 'A'+str(i), inplace=True)
print(overlapping, file=output)
# input("Press any key to finish the program.")
