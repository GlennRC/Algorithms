import random


def genRandSubIntervals():
    intervals = []
    for i in range(10):
        start = random.uniform(0.0, 1.0)
        end = random.uniform(start, 1.0)
        intervals.append((start, end))
    return intervals


def earliestFinishedFirst(a: list):
    a.sort(key=lambda tup: tup[1])
    print(a)
    optimal = [a.pop(0)]
    print("optimal: {}".format(optimal))
    print("a: {}".format(a))

    for i in range(len(a)):
        start, end = a[i]
        for j in range(len(optimal)):
            s, e = optimal[j]
            if e > start:
                break
        else:
            optimal.append(a[i])

    return optimal


def main():
    a = [(8, 16), (15, 16), (8, 9), (10, 11), (10, 23)]
    intervals = genRandSubIntervals()
    print(earliestFinishedFirst(intervals))


if __name__ == "__main__":
    main()
