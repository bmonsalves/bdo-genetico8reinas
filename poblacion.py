import cromosoma
import random

class Poblacion:
    def __init__(self, num_reinas, tam_poblacion):
        self.num_reinas = num_reinas
        self.tam_poblacion = tam_poblacion
        self.poblacion = self.generarPoblacion()
        print "Num reinas: {} poblacion: {}".format(self.num_reinas, self.tam_poblacion)

    def __str__(self):
        return "\n".join([str(cromosoma) for cromosoma in self.poblacion])

    def __len__(self):
        return len(self.poblacion)

    def __getitem__(self, index):
        return self.poblacion[index]

    #genera poblacion y la almacena en una lista
    def generarPoblacion(self):
        poblacion = []
        for index in range(self.tam_poblacion):
            poblacion.append(cromosoma.Cromosoma.random(self.num_reinas))
        #poblacion.sort()
        return poblacion


    def cruzar(self, proba_mutacion):
        #toma 3 poblaciones y las ordena por costo
        touny = random.sample(self, 3)
        print "touny", touny
        touny.sort()
        #envia las 2 poblaciones de menor costo
        new_c = cromosoma.Cromosoma.fromParents(touny[0], touny[1])
        new_c.mutar(proba_mutacion)

        self.matar(new_c, touny[2])
        return self

    #reemplaza el nuevo individuo por el de mayor costo
    def matar(self, new_c, old_c):
        self.poblacion.append(new_c)
        self.poblacion.remove(old_c)
        self.poblacion.sort()

    def sort(self):
        self.poblacion.sort()

