import poblacion, cromosoma, sys

class Genetico:

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
        w += 1

    for h in a:
        fila = '  '.join(h)
        print "\t",fila

    print "\n"


import sys
def valores(argv):
    params = {'proba_mutacion':.001, 'max_iteraciones':1000, 'num_reinas':8,'tam_poblacion':10}

    return params


#main
if __name__ == "__main__":
    parameters = valores(sys.argv[1:])

    poblacion = poblacion.Poblacion(parameters['num_reinas'],parameters['tam_poblacion'])
    g = Genetico(parameters['proba_mutacion'], parameters['max_iteraciones'])

    resultado = g.buscarSolucion(poblacion)
    imprimeTablero(resultado,parameters['num_reinas'])

   