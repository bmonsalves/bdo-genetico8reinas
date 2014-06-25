import random

#individuos
class Cromosoma:
    def __init__(self, sequence):
        self.cromosoma = sequence
        self.costo = self.obtenerCosto()
    def __str__(self):
        return "{} Costo: {}".format(self.cromosoma, self.costo)

    #cadenas
    def __repr__(self):
        return str(self.cromosoma)
    #compara
    def __cmp__(self, other):
        return self.costo.__cmp__(other.costo)

    def __len__(self):
        return len(self.cromosoma)

    def __getitem__(self, indice):
        return self.cromosoma[indice]

    def __setitem__(self, indice, value):
        self.cromosoma[indice] = value

    @classmethod
    def fromParents(cls, padre, madre):
        val = -1
        if (len(padre) != len(madre)):
            return "Error"

        if (padre == madre):
            madre = Cromosoma.random(len(madre))

        posible = [i for i in range(len(padre))]
        actual = [val for i in range(len(padre))]

        #print "posible, ", posible
        #print "actual, ", actual
        
        #si el valor de la madre es igual al del padre se mantiene en el hijo
        for i in range(len(padre)):
            if (padre[i] == madre[i]):
                actual[i] = padre[i]
                posible.remove(actual[i])
                #print "posible",posible
                #print "actual",actual
        #si hay valores que no cambiaron se reemplaza por un valor random de los disponibles
        for i in range(len(padre)):
            if (actual[i] == val):
                actual[i] = random.choice(posible)
                posible.remove(actual[i])
                #print "posible 2",posible
                #print "actual 2",actual

        print "padre: ", padre
        print "madre: ", madre
        print "hijo: ",cls(actual)
        return cls(actual)

    #crea una poblacion aleatoria
    #cls primer parametro de un metodo de clase
    @classmethod
    def random(cls, num_reinas):
        cromosoma = [i for i in range(num_reinas)]
        random.shuffle(cromosoma)
        return cls(cromosoma)

    #calcula la aptitud de los cromosomas
    def obtenerCosto(self):
        costo = 0
        
        for i in range(len(self.cromosoma)):
            print "----"
            costo += self.cromosoma.count(self.cromosoma[i]) - 1
            costo += self.obtenerCostoDiagonal(i)
        return costo

    def obtenerCostoDiagonal(self, indice):
        costo = 0
        for i in range(len(self.cromosoma)):
            #evita que de 0 
            if (i != indice):
                print "indice   :",indice
                print "valor i  :", i
                # posicion del cromosoma - indice
                delta_x = abs(indice - i)
                print "delta_x",delta_x

                #valor posicion actual - el resto de los cromosomas
                delta_y = abs(self.cromosoma[indice] - self.cromosoma[i])
                print "cromosoma indice",self.cromosoma[indice]
                print "cromosoma i", self.cromosoma[i]
                print "delta_y",delta_y
                if (delta_x == delta_y):
                    costo = costo + 1
        return costo

    #si el random es menor a proba_mutacion entonces cambia el valor
    def mutar(self, proba_mutacion):
        if (random.random() < proba_mutacion):
            indiceOne = random.randint(0, len(self) - 1)
            indiceTwo = random.randint(0, len(self) - 1)
            temp = self.cromosoma[indiceOne]
            self.cromosoma[indiceOne] = self.cromosoma[indiceTwo]
            self.cromosoma[indiceTwo] = temp

