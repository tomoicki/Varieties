from scipy.spatial import ConvexHull, convex_hull_plot_2d
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy


points1 = numpy.random.rand(5, 2)
points2 = numpy.random.rand(5, 2)
hull1 = ConvexHull(points1)
hull2 = ConvexHull(points2)
hull1_Delaunay = Delaunay(points1)
hull2_Delaunay = Delaunay(points2)
print(points1)
print(hull1.points)

plt.plot(points1[:, 0], points1[:, 1], 'o')
plt.plot(points2[:, 0], points2[:, 1], 'x')
for simplex in hull1.simplices:
    plt.plot(points1[simplex, 0], points1[simplex, 1], 'k-')

plt.plot(points1[hull1.vertices,0], points1[hull1.vertices,1], 'r--', lw=2)
plt.plot(points1[hull1.vertices[0],0], points1[hull1.vertices[0],1], 'ro')

for simplex in hull2.simplices:
    plt.plot(points2[simplex, 0], points2[simplex, 1], 'k-')

plt.plot(points2[hull2.vertices,0], points2[hull2.vertices,1], 'r--', lw=2)
plt.plot(points2[hull2.vertices[0],0], points2[hull2.vertices[0],1], 'ro')
plt.show()