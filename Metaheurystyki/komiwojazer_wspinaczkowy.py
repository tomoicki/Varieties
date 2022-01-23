import pandas
import random

names = ["City " + str(i) for i in range(1,17)]
cities = pandas.read_csv("miasta.txt", delimiter='\t', names=names)
cities.index = names
print(cities)


class Genotype:
    ancestors = "1"
    number_of_genes = 16
    list16 = [i for i in range(1, number_of_genes)]

    def __init__(self):
        self.genes = self.initialize_genes()
        self.path = self.create_path()

    def initialize_genes(self):
        genes = [i for i in range(self.number_of_genes)]
        for i in range(self.number_of_genes, 0, -1):
            genes[self.number_of_genes - i] = random.randint(0, 1000) % i
        return genes

    def create_path(self):
        list16 = [i for i in range(1, self.number_of_genes + 1)]
        path = []
        for i in range(len(list16)):
            path.append(list16[self.genes[i]])
            for j in range(self.genes[i], self.number_of_genes - 2):
                list16[j] = list16[j + 1]
        return path


gen1 = Genotype()
print(gen1.genes)
print(gen1.path)
