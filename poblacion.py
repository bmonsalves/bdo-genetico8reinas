import cromosoma
import random


class Poblacion:
    def __init__(self, num_queens=8, poblacion_size=10):
        self.num_queens = num_queens
        self.poblacion_size = poblacion_size
        self.poblacion = self.generatePoblacion()
        print "Num reinas: {} poblacion: {}".format(self.num_queens, self.poblacion_size)

    def generatePoblacion(self):
        poblacion = []
        for index in range(self.poblacion_size):
            poblacion.append(cromosoma.Cromosoma.random(self.num_queens))
        poblacion.sort()
        return poblacion

    def breed(self, proba_mutacion=.001):
        touny = random.sample(self, 3)
        touny.sort()

        new_c = cromosoma.Cromosoma.fromParents(touny[0], touny[1])
        new_c.mutar(proba_mutacion)

        self.reemplazarCromosoma(new_c, touny[2])
        return self

    def reemplazarCromosoma(self, new_c, old_c):
        self.poblacion.append(new_c)
        self.poblacion.remove(old_c)
        self.poblacion.sort()

    def sort(self):
        self.poblacion.sort()

    def __str__(self):
        return "\n".join([str(cromosoma) for cromosoma in self.poblacion])

    def __len__(self):
        return len(self.poblacion)

    def __getitem__(self, index):
        return self.poblacion[index]


if __name__ == "__main__":
    print Poblacion()
