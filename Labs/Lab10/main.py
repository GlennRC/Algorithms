'''
Lab 10
Algorithms
Professor Hayes
Glenn Contreras and Tianxiang Liu
'''
import random
import time

def genList():
    l = []
    for i in range(10000):
        l.append(random.randint(0, 10000))
    return l


def lomuto(a, l, r):
    p = a[l]
    s = l
    for i in range(l, r):
        if a[i] < p:
            s += 1
            a[s], a[i] = a[i], a[s]
    a[l], a[s] = a[s], a[l]
    return s


def quick_sort(a, l, r):
    if l < r:
        s = lomuto(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)
    return a


def SelectionSort(A):
    l = len(A)
    for f in range(0, l-1):
        m = f
        for i in range(f+1, l):
            if A[i] < A[m]:
                m = i
        A[f], A[m] = A[m], A[f]
    return A

def calcTime(foo, args):
    start = time.time()
    foo(*args)
    print("{}: {}\n".format(foo, time.time() - start))


def main():
    # part 1 and 2
    unsortedList = [8,2,1,14,9,7,11,13,20,5]
    sortedList = quick_sort(list(unsortedList), 0, len(unsortedList))
    print("{}\n{}\n".format(unsortedList, sortedList))

    # part 3
    randList = genList()
    calcTime(quick_sort, [list(randList), 0, len(randList)])
    calcTime(SelectionSort, [list(randList)])

if __name__ == "__main__":
    main()
