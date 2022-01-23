from math import sin, pi
import random

round_int = 3
genes_amount = 5
population_size = 25
max_gens = 100
prob_over = 0.8
prob_mutation = 0.2


class Genotype:
    def __init__(self):
        self.genes = []
        for i in range(genes_amount):
            self.genes.append(round(random.random() * pi, round_int))
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        fit = 1000
        for gen in self.genes:
            fit *= sin(gen)
        return round(fit, round_int)

    def show(self):
        print(f"Genes pool: {self.genes}")
        print(f"Fitness: {self.fitness}")
        print(f"rFitness: {self.rfitness}")
        print(f"cFitness: {self.cfitness}")


class Population:
    def __init__(self):
        self.specimens = []
        self.new_population = []
        for i in range(population_size):
            self.specimens.append(Genotype())
        self.suma = sum([specimen.fitness for specimen in self.specimens])
        for specimen in self.specimens:
            specimen.rfitness = specimen.fitness / self.suma
        cum = 0
        for i in range(population_size):
            self.specimens[i].cfitness = (cum, cum + self.specimens[i].rfitness)
            cum += self.specimens[i].rfitness

    def show(self):
        print([specimen.show() for specimen in self.specimens])

    def keep_the_best(self):
        fitnesses = [specimen.fitness for specimen in self.specimens]
        print(fitnesses)
        print(max(fitnesses))
        print(fitnesses.index(max(fitnesses)))

    def select(self):
        self.suma = sum([specimen.fitness for specimen in self.specimens])

    def rfitness(self):
        for specimen in self.specimens:
            specimen.rfitness = specimen.fitness/self.suma

def losowa(gora, dol):
    return dol + random.random() * (gora - dol)

population1 = Population()
[specimen.show() for specimen in population1.specimens]

for i in range(population_size):
    p = random.random()
    if p < population1.specimens[i].cfitness:
        population1.new_population[i] = population1.specimens[i]
    else:
        for j in range(population_size):
            if p >= population1.specimens[j].cfitness and p < population1.specimens[j + 1].cfitness:
                population1.new_population[i] = population1.specimens[j + 1]

