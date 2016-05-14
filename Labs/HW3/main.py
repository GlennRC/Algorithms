import random
import time


def preSortIntersection(a: list, b: list):
    a.sort()
    b.sort()

    intersect = set(a) & set(b)
    return intersect


def bruteForceIntersection(a, b):
    intersection = set()

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                intersection.add(a[i])

    return intersection


def fastMinDist(a: list):
    a.sort()
    dist = float("inf")
    for j in range(len(a)-1):
        i = j + 1
        d = abs(a[i] - a[j])
        if d < dist:
            dist = d
    return dist


def slowMinDist(a: list):
    dist = float("inf")
    for i in range(len(a)):
        for j in range(len(a)):
            d = abs(a[i] - a[j])
            if i != j and d < dist:
                dist = d
    return dist


def genList(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, 10))
    return l


def main():
    n = 10
    a = genList(n)
    b = genList(n)
    print(a)
    print(b)

    # 1. presorting
    print("1.1")
    start = time.time()
    print("Presorting intersection: {}".format(preSortIntersection(a.copy(), b.copy())))
    print("Time: {}".format(time.time() - start))

    print("\n1.2")
    start = time.time()
    print("Brute force intersection: {}".format(bruteForceIntersection(a, b)))
    print("Time: {}".format(time.time() - start))

    print("\n2.a")
    start = time.time()
    print("Presorting min dist: {}".format(fastMinDist(a)))
    print("Time: {}".format(time.time() - start))

    print("\n2.b")
    start = time.time()
    print("\nBrute force min dist: {}".format(slowMinDist(a)))
    print("Time: {}".format(time.time() - start))


if __name__ == "__main__":
    main()
