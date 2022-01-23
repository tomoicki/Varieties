from math import sin, pi
import random


class Genotype:
    def __init__(self, number_of_genes):
        self.number_of_genes = number_of_genes
        self.gene = []
        for i in range(number_of_genes):
            self.gene.append(random.random() * pi)
        self.fitness = self.oblicz_dopasowanie()

    dopasowanie = 1000

    def oblicz_dopasowanie(self):
        for gen in self.gene:
            self.dopasowanie *= sin(gen)
        return self.dopasowanie

    def show(self):
        print(f"Pula genów: {self.gene}")
        print(f"Dopasowanie: {self.fitness}")

    @classmethod
    def generuj_nowego(cls, genotype_object):
        gen_rand = random.randint(0, 4)
        print(f"Zmieniony gen: {gen_rand + 1}")
        nowy = Genotype(5)
        for i in range(nowy.il_zmiennych):
            nowy.gene[i] = genotype_object.gene[i]
        nowy.gene[gen_rand] += random.random() - 0.5
        if nowy.gene[gen_rand] < 0:
            nowy.gene[gen_rand] = 0
        if nowy.gene[gen_rand] > pi:
            nowy.gene[gen_rand] = pi
        nowy.fitness = nowy.oblicz_dopasowanie()
        return nowy

    @classmethod
    def select(cls, new, old):
        pass

osobnik = Genotype(5)
osobnik.show()

def select(nowy, osobnik):
    if nowy.fitness > osobnik.fitness:
        osobnik.gene = nowy.gene.copy()
        osobnik.fitness = osobnik.oblicz_dopasowanie()
        print("Zmieniono")
        return osobnik
    else:
        print("Nie zmieniono")
        return nowy


for i in range(5):
    print(f"\nGeneracja nr: {i}")
    nowy = Genotype.generuj_nowego(osobnik)
    nowy.show()
    osobnik = select(nowy, osobnik)
    osobnik.show()
