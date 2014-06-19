import poblacion,sys

class GeneticAlgorithm:

    #constructor
    def __init__(self, proba_mutacion=.001, max_iterations = 1000000):
        self.proba_mutacion = proba_mutacion
        self.max_iterations = max_iterations

    def buscar_solucion(self, poblacion):
        print "probabilidad de mutacion: {} iteraciones maximas: {}".format(self.proba_mutacion,self.max_iterations)

        for i in range(self.max_iterations):
            poblacion = poblacion.breed(self.proba_mutacion)

            # imprime poblaciones
            print poblacion
            
            if poblacion[0].cost == 0:
                print "{} cruzas".format(i)
                return poblacion[0]

        print "no hay solucion"
        return -1

def imprimeTablero(poblacion, tamano):
    print "Posiciones: "
    print poblacion
    a = []
    for i in xrange(tamano):
        a.append([])
        for j in xrange(tamano):
            a[i].append('-')

    w = 0
    print "\n----------------TABLERO----------------\n"
    for x in poblacion:
        a[x][w] = "R"
        w=w+1

    for h in a:
        fila = '  '.join(h)
        print "\t",fila

    print "\n"


import sys
def valores(argv):
    params = {'proba_mutacion':.001, 'max_iterations':1000000, 'nqueens':8,'poblacion_size':10}

    return params

if __name__ == "__main__":
    parameters = valores(sys.argv[1:])

    poblacion = poblacion.Poblacion(parameters['nqueens'],parameters['poblacion_size'])
    g = GeneticAlgorithm(parameters['proba_mutacion'], parameters['max_iterations'])

    #imprime tablero
    resultado = g.buscar_solucion(poblacion)
    imprimeTablero(resultado,parameters['nqueens'])

   