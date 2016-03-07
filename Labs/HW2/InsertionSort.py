"""
@description: HW_2 - Section 4.1, Question 7
@professor: Hayes
@author: Glenn Contreras
@date: 3 March 2016
"""


def insertion_sort(a):
    for i in range(len(a)):
        v = a[i]
        j = i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v


'''
GenSubSets(items[0..n])
    if n = 0
        return subsets <- { {}, {items[0]}}
    else
        smaller <- GenSubSets(items[0..n-1])
        for each subset in smaller
            subset.append(subset.append(subset))
            subset.append(subset U items[n-1])
'''


def bottom_up(a, n):
    print("top n={}".format(n))
    if n == 0:
        print('end')
        print()
        return [[a[n]]]
    else:
        smaller = bottom_up(a, n-1)

        print("else n={}".format(n))
        print("before extend= {}".format(smaller))
        smaller.extend(smaller[:len(n)])
        smaller = [sub.copy() for sub in smaller]

        print("after extend= {}".format(smaller))

        print('permute')

        for i in range(len(smaller)):
            print("i={}".format(i))
            print("smaller = {}".format(smaller))
            print("smaller before insert = {}".format(smaller[i]))
            smaller[i].insert(i, a[n])
            print("smaller after insert = {}".format(smaller[i]))
            print()
    return smaller

def helper_mobile(a, i):
    m = -1
    if a[i][1] == '<-':
            if i-1 >= 0 and a[i-1][0] < a[i][0]:
                m = i
    else:
        if i+1 < len(a) and a[i+1][0] < a[i][0]:
            m = i
    return m
def get_mobile(a):
    mobile = -1
    for i in range(len(a)):
        m = helper_mobile(a, i)
        if m == -1:
            continue
        if mobile == -1 or a[m][0] > a[mobile][0]:
            mobile = m
    return mobile
def reverse(a, v):
    for i in range(len(a)):
        if a[i][0] > v[0]:
            if a[i][1] == '<-':
                a[i] = (a[i][0], '->')
            else:
                a[i] = (a[i][0], '<-')
def pretty_print(a):
    for p in a:
        for (i, j) in p:
            print(i, end="")
        print(" ", end="")
def trotter(n):
    l = []
    a = [(i+1, '<-') for i in range(n)]
    l.append(a.copy())

    m = get_mobile(a)
    while m > -1:
        v = a[m]
        if a[m][1] == '<-':
            a[m-1], a[m] = a[m], a[m-1]
        else:
            a[m+1], a[m] = a[m], a[m+1]
        reverse(a, v)
        l.append(a.copy())
        m = get_mobile(a)
    return l


def get_consecutive(l):
    largest = -1
    for i in range(1, len(l)):
        if l[i-1] < l[i]:
            if largest == -1 or i > largest:
                largest = i
    return largest


def lexi_perm(n):
    perm = []
    p = [i+1 for i in range(n)]
    perm.append(p)
    while get_consecutive(p):








def main():
    a = ['A', 'B', 'C']

    '''
    print(id(a))
    print(id(a.copy))
    '''

    b = [(1, '<-'), (2, '<-'), (3, '<-')]
    n = 3
    perm = trotter(n)
    pretty_print(perm)

    c = [1,2,3]
    print()
    print(get_consecutive(c))

if __name__ == "__main__":
    main()






