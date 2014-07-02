import reinas, poblacion

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


#main
if __name__ == "__main__":

    parametros = {'proba_mutacion':1, 'max_iteraciones':1000, 'num_reinas':8,'tam_poblacion':10}

    #crea poblaciones
    poblacion = poblacion.Poblacion(parametros['num_reinas'],parametros['tam_poblacion'])
    #crea objeto reinas
    r = reinas.Reinas(parametros['proba_mutacion'], parametros['max_iteraciones'])

    resultado = r.buscarSolucion(poblacion)
    imprimeTablero(resultado,parametros['num_reinas'])
