# This was worked on by Glenn Contreras, Neha Tammana, and Tianxiang liu

import random
import time

def getRandCoord(num):
    random.seed()
    coordinates = []
    for i in range(num):
        x = randNum = random.randrange(-500, 500)
        y = randNum = random.randrange(-500, 500)
        coordinates.append((x,y))
    return coordinates

def getClosestCoord(coord):
    d = float("inf")
    closestCoord = ()
    count = 0
    begin = time.time()
    for i in range(len(coord)-1):
        for j in range(i+1, len(coord)):
            if i < j:
                currD = pow(coord[i][0] - coord[j][0], 2)
                currD += pow(coord[i][1] - coord[j][1], 2)
                count += 2
                if currD < d:
                    d = currD
                    closestCoord = (coord[i], coord[j])
    end = time.time()
    return closestCoord, d, count, end-begin

def main():
    data = {}
    for i in range(100, 1100, 100):
        randCoord = getRandCoord(i)
        closestCoord = getClosestCoord(randCoord)
        data[i] = {"coordinates":closestCoord[0],
                   "distance":closestCoord[1],
                   "iterations": closestCoord[2],
                   "time": closestCoord[3]}

    for i in range(100, 1100, 100):
        print(str(i) +": " + str(data[i]))

    '''
    The theoretical analysis shows this function has an order
    of growth of about n^2. The amount of actual operations
    performed by our function is about the same but a little less.
    '''

if __name__ == '__main__':
    main()