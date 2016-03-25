import random

def genRandList(r, n, m):
    l = []
    for i in range(r):
        l.append(random.randint(n, m))
    return l


def linearSearch(l, n):
    for i in range(len(l)):
        if n == l[i]:
            return i
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


def preSortFindIntersection(arr1, arr2):
    sortArr1 = quick_sort(arr1)
    sortArr2 = quick_sort(arr2)

    intersection = set()

    for i in range(len(sortArr1)):
        if sortArr1[i] == sortArr2[i]:
            intersection.add(sortArr1[i])

    return intersection

def bruteForceIntersection(arr1, arr2):
    intersection = set()

    for i in random(len(arr1)):
        for j in random(len(arr2)):
            if arr1[i] == arr2[j]:
                set(arr1[i])

    return intersection



def main():





if __name__ == "__main__":
    main()
