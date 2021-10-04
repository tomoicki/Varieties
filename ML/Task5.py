import pandas
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay
import numpy


training_set = pandas.read_csv('iris_trn.txt', header=None, sep='\s+', skiprows=[0])
output = open('iris_res5.txt', 'w')

headers = ['class']
features = []
for i in range(len(training_set.iloc[0]) - 1):
    headers.append('y' + str(i + 1))
    features.append('y' + str(i + 1))
training_set.columns = headers

class1 = 1
class2 = 2

delta1 = 0.1
delta2 = -0.001

m = training_set.index.size  # number of rows in training set
n = len(features)  # number of features

lv = training_set['class'].values
x = training_set[features].values
first_class_values = training_set.loc[training_set['class'] == class1]
x_c1 = first_class_values[features].values
second_class_values = training_set.loc[training_set['class'] == class2]
x_c2 = second_class_values[features].values
m1 = first_class_values.index.size
m2 = second_class_values.index.size
minn = min(m1, m2)
c1_hull = ConvexHull(x_c1)
print("po hullu")
# c1_hull_Delaunay = Delaunay(x_c1)
# x_c2_inside_c1_hull = c1_hull_Delaunay.find_simplex(x_c2)
# x_c2_inside_c1_hull_TrueFalse = False
# for item in x_c2_inside_c1_hull:
#     if item >= 0:
#         x_c2_inside_c1_hull_TrueFalse = True

c2_hull = ConvexHull(x_c2)
# c2_hull_Delaunay = Delaunay(x_c2)
# x_c1_inside_c2_hull = c2_hull_Delaunay.find_simplex(x_c1)
# x_c1_inside_c2_hull_TrueFalse = False
# for item in x_c1_inside_c2_hull:
#     if item >= 0:
#         x_c1_inside_c2_hull_TrueFalse = True

# if not x_c1_inside_c2_hull_TrueFalse and not x_c2_inside_c1_hull_TrueFalse:
#     print("Sets are linearly separable.")
# else:
#     print("Sets are linearly inseparable.")

nearest_x_c1_to_c2_hull = []
for i in range(len(x_c1)):
    distances = numpy.linalg.norm(c2_hull.points - x_c1[i], axis=1)
    nearest_from_c2_hull = distances.argsort()[:1]
    nearest_x_c1_to_c2_hull.append([i, nearest_from_c2_hull[0], distances[nearest_from_c2_hull][0]])
nearest_x_c1_to_c2_hull = numpy.array(nearest_x_c1_to_c2_hull)
c1_to_c2 = nearest_x_c1_to_c2_hull[numpy.where(nearest_x_c1_to_c2_hull[:, 2] == min(nearest_x_c1_to_c2_hull[:, 2]))][0]

nearest_x_c2_to_c1_hull = []
for i in range(len(x_c2)):
    distances = numpy.linalg.norm(c1_hull.points - x_c2[i], axis=1)
    nearest_from_c1_hull = distances.argsort()[:1]
    nearest_x_c2_to_c1_hull.append([i, nearest_from_c1_hull[0], distances[nearest_from_c1_hull][0]])
nearest_x_c2_to_c1_hull = numpy.array(nearest_x_c2_to_c1_hull)
c2_to_c1 = nearest_x_c2_to_c1_hull[numpy.where(nearest_x_c2_to_c1_hull[:, 2] == min(nearest_x_c2_to_c1_hull[:, 2]))][0]

if c1_to_c2[2] == c2_to_c1[2] and c1_to_c2[0] == c2_to_c1[1] and c1_to_c2[1] == c2_to_c1[0]:
    print("Bingo!. We found pair of specimens closest to each other.")

A = x_c1[int(c1_to_c2[0])]
B = x_c2[int(c2_to_c1[0])]
print(A)
print(B)
print(numpy.linalg.norm(A - B))


