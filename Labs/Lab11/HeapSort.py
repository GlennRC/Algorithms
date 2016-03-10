import heapq
import random
import time


def genRandList(n):
    l = []
    for i in range(n):
        l.append(random.randint(0, 5000))
    return l


def linearSearch(l, n):
    for i in range(len(l)):
        if n == l[i]:
            return i
    return -1


def binSearch(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return -1


def binSearch(number, array, lo, hi):

    if hi < lo: return -1
    mid = (lo + hi) // 2
    if number == array[mid]:
        return mid
    elif number < array[mid]:
        return binSearch(number, array, lo, mid - 1)
    else:
        return binSearch(number, array, mid + 1, hi)


def main():
    l = genRandList(1000)
    randint = random.randint(0, len(l)-1)

    print(binSearch(l[randint], l, 0, len(l)-1))

    start = time.time()
    linearSearch(l, l[randint])
    time1 = time.time() - start


    start = time.time()
    heapq.heapify(l)
    binSearch(l[randint], l, 0, len(l)-1)
    time2 = time.time() - start





if __name__ == '__main__':
    main()