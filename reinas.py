import main, poblacion, cromosoma, sys

class Reinas:

    #constructor
    def __init__(self, proba_mutacion, max_iteraciones):
        self.proba_mutacion = proba_mutacion
        self.max_iteraciones = max_iteraciones

    def buscarSolucion(self, poblacion):
        print "probabilidad de mutacion: {} iteraciones maximas: {}".format(self.proba_mutacion,self.max_iteraciones)

        for i in range(self.max_iteraciones):
            poblacion = poblacion.cruzar(self.proba_mutacion)

            # imprime poblaciones
            print poblacion
            
            if poblacion[0].costo == 0:
                print "{} cruzas".format(i)
                return poblacion[0]

        print "no hay solucion"
        return -1


