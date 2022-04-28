import random
import math
import time

"""
Testovanie pre 20,30,40 miest
na 50,250,500 tabu list
s 3 opakovania
"""


def fitness(current):
    current.append(current[0])
    counter = 0
    for i in range(len(current) - 1):
        vector = [current[i + 1][0] - current[i][0], current[i + 1][1] - current[i][1]]
        counter += math.sqrt((vector[0]**2) + (vector[1]**2))
    current.pop(-1)

    return counter


def get_children(current):
    children = []
    for i in range(len(current) - 1):
        child = list(current)
        child[0] = current[i + 1]
        child[i + 1] = current[0]
        children.append(child)
    else:
        child = list(current)
        child[1] = current[-1]
        child[-1] = current[1]
        children.append(child)
    return children


if __name__ == '__main__':
    file = open("results.txt", "a")

    for x in range(3):

        starter = []
        while len(starter) != 40:
            new = [random.randint(1, 200), random.randint(1, 200)]
            if new not in starter:
                starter.append(new)


        #starter = [(17,54), (95, 59), (49, 62), (50,92), (12,69), (92,5), (49, 46), (52,93), (80, 83), (50, 73)]

        print(fitness(starter))
        s = time.time()

        sBest = starter
        bestCandidate = starter
        tabuList = [starter]
        file.write(str(fitness(bestCandidate)))
        for stop in range(10000):
            sNeighborhood = get_children(bestCandidate)
            bestCandidate = sNeighborhood[0]
            for sCandidate in sNeighborhood:
                if (sCandidate not in tabuList) and (fitness(sCandidate) < fitness(bestCandidate)):
                    bestCandidate = sCandidate
                    file.write("," + str(fitness(bestCandidate)))
            if fitness(bestCandidate) < fitness(sBest):
                sBest = bestCandidate
            tabuList.append(bestCandidate)
            if len(tabuList) > 20:
                tabuList.pop(0)

        e = time.time()
        print(fitness(sBest))
        print(e - s)
        print("\n")
        file.write("\n")

    file.close()
