import random


class Cromosoma:
    def __init__(self, sequence):
        self.cromosoma = sequence
        self.cost = self.getCost()

    @classmethod
    def fromParents(cls, parent_one, parent_two):
        if (len(parent_one) != len(parent_two)):
            return "Error"

        if (parent_one == parent_two):
            parent_two = Cromosoma.random(len(parent_two))

        possible = [i for i in range(len(parent_one))]
        current = [-1 for i in range(len(parent_one))]

        for i in range(len(parent_one)):
            if (parent_one[i] == parent_two[i]):
                current[i] = parent_one[i]
                possible.remove(current[i])
        for i in range(len(parent_one)):
            if (current[i] == -1):
                current[i] = random.choice(possible)
                possible.remove(current[i])

        return cls(current)

    @classmethod
    def random(cls, num_queens=8):
        cromosoma = [i for i in range(num_queens)]
        random.shuffle(cromosoma)
        return cls(cromosoma)

    def getCost(self):
        cost = 0;
        for i in range(len(self.cromosoma)):
            cost += self.cromosoma.count(self.cromosoma[i]) - 1
            cost += self.getDiagonalCost(i)
        return cost

    def getDiagonalCost(self, index):
        cost = 0
        for i in range(len(self.cromosoma)):
            if (i != index):
                delta_x = abs(index - i)
                delta_y = abs(self.cromosoma[index] - self.cromosoma[i])
                if (delta_x == delta_y):
                    cost = cost + 1
        return cost

    def mutar(self, proba_mutacion=.001):
        if (random.random() < proba_mutacion):
            indexOne = random.randint(0, len(self) - 1)
            indexTwo = random.randint(0, len(self) - 1)
            temp = self.cromosoma[indexOne]
            self.cromosoma[indexOne] = self.cromosoma[indexTwo]
            self.cromosoma[indexTwo] = temp

    def __str__(self):
        return "{} Costo: {}".format(self.cromosoma, self.cost)

    def __repr__(self):
        return str(self.cromosoma)

    def __cmp__(self, other):
        return self.cost.__cmp__(other.cost)

    def __len__(self):
        return len(self.cromosoma)

    def __getitem__(self, index):
        return self.cromosoma[index]

    def __setitem__(self, index, value):
        self.cromosoma[index] = value


if __name__ == "__main__":
    print Cromosoma([4, 2, 0, 6, 1, 7, 5, 3])
    parent_one = Cromosoma.random()
    parent_two = Cromosoma.random()
    print "Parent One: " + str(parent_one)
    print "Parent Two: " + str(parent_two)
    print Cromosoma.fromParents(parent_one, parent_two)