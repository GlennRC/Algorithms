import random
import time


def preSortIntersection(a: list, b: list):
    a.sort()
    b.sort()

    intersect = set()

    if len(a) < len(b):
        a, b = b, a

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            intersect.add(a[i])
            i += 1
            j += 1
    return intersect


def preSortDiff(a: list, b: list):
    a.sort()
    b.sort()

    diff = set()

    if len(a) < len(b):
        a, b = b, a

    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            j += 1
        else:
            if a[i] < b[j]:
                diff.add(a[i])
            i += 1
            j += 1
    diff = diff | set(a[i:])
    return diff


def bruteForceIntersection(a, b):
    intersection = set()

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                intersection.add(a[i])
    return intersection


def bruteForceDiff(a, b):
    diff = set()
    for i in range(len(a)):
        found = False
        for j in range(len(b)):
            if a[i] == b[j]:
                found = True
                break
        if not found:
            diff.add(a[i])
    return diff


def fastMinDist(a: list):
    a.sort()
    dist = float("inf")
    for j in range(len(a)-1):
        i = j + 1
        d = abs(a[i] - a[j])
        if d < dist:
            dist = d
    return dist


def genList(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, 1000))
    return l


def findMedian(a: list):
    a.sort()
    return a[int(len(a)/2)]


def findMode(a: list):
    a.sort()
    print(a)
    num = a[0]
    count = 0
    mode = (num, count)
    for i in range(len(a)):
        if mode[1] < count:
                mode = (num, count)
        if num == a[i]:
            count += 1
        else:
            count = 1
            num = a[i]
    return mode


def main():
    n = 10000
    a = genList(n)
    #b = genList(n)

    '''
    print("1.1")
    start = time.time()
    print("Presorting intersection: {}".format(preSortIntersection(a.copy(), b.copy())))
    print("Time: {}".format(time.time() - start))

    print("\n1.2")
    start = time.time()
    print("Brute force intersection: {}".format(bruteForceIntersection(a, b)))
    print("Time: {}".format(time.time() - start))

    start = time.time()
    print("\nshould be: \t\t\t{}".format(set(a.copy()) - set(b.copy())))
    print("Time: {}".format(time.time() - start))

    start = time.time()
    print("\nPresorting diff: \t{}".format(preSortDiff(a.copy(), b.copy())))
    print("Time: {}".format(time.time() - start))

    start = time.time()
    print("\nBruteForce diff: \t{}".format(bruteForceDiff(a.copy(), b.copy())))
    print("Time: {}".format(time.time() - start))
    '''
    a = [1,2,3,3,5,5,8,8,8,8,0,2,4]
    print(findMode(a))

if __name__ == "__main__":
    main()