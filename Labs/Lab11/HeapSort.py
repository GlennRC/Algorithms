import heapq
import random
import time
import math


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

'''
def rbinSearch(a, n, lo, hi):
    if lo > hi:
        return -1
    else:
        mid = int((hi + lo) / 2)
        if n > a[mid]:
            return rbinSearch(a, n, mid+1, hi)
        elif n < a[mid]:
            return rbinSearch(a, n, lo, mid-1)
        else:
            return mid
'''

def binSearch(a, n):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (hi + lo) // 2
        if n > a[mid]:
            lo = mid + 1
        elif n < a[mid]:
            hi = mid - 1
        else:
            return mid
    return -1


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


def main():
    # Part 1
    l = [5, 3, 1, 7, 8, 6, 4, 2]
    heapq.heapify(l)
    print(l)
    print(heapq.heappop(l))
    heapq.heappush(l, 2)
    print(l)

    # part 2
    l = genRandList(500)
    start = time.time()
    randint = random.randint(0, len(l)-1)

    for i in range(5000):
        # linear
        linearSearch(l, l[randint])
    print(time.time() - start)

    start = time.time()
    for i in range(10):
        # quick sort + binary search
        l = quick_sort(l, 0, len(l)-1)
        binSearch(l, l[randint])
    print(time.time() - start)

    '''
    The linear search needs to perform about 500 times more operations
    in order for binary search to out perform linear search
    '''


if __name__ == '__main__':
    main()
