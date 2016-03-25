import string
import random
import time

'''
This lab was worked on by Glenn Contreras, Neha Tammana, and Ben Liu
'''

def shiftTable(pattern, isBit):
    if isBit:
        var = ['0', '1']
    else:
        var = string.ascii_lowercase + ' '

    table = {}
    for i in range(len(var)):
        table.update({var[i]: len(pattern)})
    for j in range(len(pattern)-1):
        table[pattern[j]] = len(pattern) - 1 - j

    return table


def horspool(pattern, text, isBit):
    table = shiftTable(pattern, isBit)
    m = len(pattern)
    i = m-1
    while i <= len(text)-1:
        k = 0
        while k <= m-1 and pattern[m-1-k] == text[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else:
            i += table[str(text[i])]
    return -1


def bruteForceStringMatch(Text, Pattern):
    n = len(Text)
    m = len(Pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and Pattern[j] == Text[i+j]:
            j += 1
        if j == m:
            return i
    return -1


def genBits():
    l = []
    for i in range(1000000):
        l.append(random.randrange(0, 2))
    return l


def main():
    pattern = "pizzazzy"
    bitPattern = "01110100"

    print("1) Part a")
    print(pattern)
    print(shiftTable(pattern.lower(), False))

    print("\nPart b")
    print(bitPattern)
    print(shiftTable(bitPattern, True))

    text = "I don't want to go to the party looking too pizzazzy"
    print("\n2)")
    index = horspool(pattern.lower(), text.lower(), False)
    if index != -1:
        print("Found {} at index {}".format(pattern, index))
    else:
        print("{} not found in text".format(pattern))

    bitText = genBits()
    bitPattern = '0000000000'

    print("\nPerformance comparison against Horspool's and the bruteforce algorithm")
    start = time.time()
    print(horspool(bitPattern, bitText, True))
    print("Horspool's time: {}".format(time.time() - start))

    start = time.time()
    print(bruteForceStringMatch(bitText, bitPattern))
    print("Brute force time: {}".format(time.time() - start))


if __name__ == "__main__":
    main()
