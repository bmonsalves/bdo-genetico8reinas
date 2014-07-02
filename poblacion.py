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

    #getter/setter
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
        #toma 3 individuos y las ordena por costo
        trio = random.sample(self, 3)
        print "trio", trio
        trio.sort()
        #envia las 2 individuos de menor costo
        hijo = cromosoma.Cromosoma.parejas(trio[0], trio[1])
        hijo.mutar(proba_mutacion)

        self.matar(hijo, trio[2])
        return self

    #reemplaza el nuevo individuo por el de mayor costo
    def matar(self, hijo, no_apto):
        self.poblacion.append(hijo)
        self.poblacion.remove(no_apto)
        self.poblacion.sort()

    def sort(self):
        self.poblacion.sort()

