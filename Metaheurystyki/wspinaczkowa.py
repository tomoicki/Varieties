from math import sin, pi
import random

round_int = 3


class Genotype:
    ancestors = "1"
    number_of_genes = 3

    def __init__(self):
        self.genes = []
        for i in range(self.number_of_genes):
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

    @classmethod
    def generate_new(cls, genotype_object):
        gen_rand = random.randint(0, genotype_object.number_of_genes - 1)
        print(f"Changed gene nr: {gen_rand + 1}")
        new = Genotype()
        new.genes = genotype_object.genes.copy()
        new.genes[gen_rand] = round(new.genes[gen_rand] + random.random() - 0.5, round_int)
        if new.genes[gen_rand] < 0:
            new.genes[gen_rand] = 0
        elif new.genes[gen_rand] > pi:
            new.genes[gen_rand] = pi
        new.fitness = new.calculate_fitness()
        return new

    @classmethod
    def select(cls, new, old):
        if new.fitness > old.fitness:
            new.genes = old.genes.copy()
            new.fitness = new.calculate_fitness()
            print("Old was better than new.")
            cls.ancestors += " -> O"
            return old
        else:
            print("New was better than old.")
            cls.ancestors += " -> N"
            return new


old_specimen = Genotype()
starting_fitness = old_specimen.fitness
j = 0
while old_specimen.fitness > 0:
    print("\n")
    old_specimen.show()
    print(f"Generation nr: {j + 1}")
    new_specimen = Genotype.generate_new(old_specimen)
    new_specimen.show()
    old_specimen = Genotype.select(new_specimen, old_specimen)
    j += 1

print(f"\nStarting fitness = {starting_fitness}\n"
      f"New fitness = {old_specimen.fitness}\n"
      f"Number of generations = {j}\n"
      f"Ancestors {Genotype.ancestors}")
