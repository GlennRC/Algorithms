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
    if n == 1:
        return [[], [a[0]]]
    else:
        smaller = bottom_up(a, n-1)
        for subset in smaller:
            subset.append(subset.extend(subset))
            subset.append(subset.extend(a[len(a)-1]))
        return subset


'''
 INPUT: n, an integer

    p   ← permute(n-1)
    end ← left
    for each item in p
        start at end and insert n in all possible positions
        toggle end [left ←→ right]
'''



def main():
    a = ['A', 'B']
    print(bottom_up(a, len(a)))


if __name__ == "__main__":
    main()






