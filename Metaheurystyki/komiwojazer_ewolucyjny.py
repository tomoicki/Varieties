import pandas
import random

round_int = 3
genes_amount = 5
population_size = 25
max_gens = 100
prob_over = 0.8
prob_mutation = 0.2

names = ["City " + str(i) for i in range(1, 17)]
cities = pandas.read_csv("miasta.txt", delimiter='\t', names=names)
cities.index = names
print(cities)
