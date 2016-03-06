# This was worked on by Glenn Contreras, Neha Tammana, TianXiang liu
import time
import random

def getInput(path):
    with open(path) as file:
        lines = file.read()
        lines = lines.split("\n")
        return lines

def getDict(lines):
    d = {}
    for line in lines:
        if line == '':
            continue
        l = line.split(" ")
        d[l[0]] = l[1]
    return d

def getLists(lines):
    l1 = []
    l2 = []
    for line in lines:
        if line == '':
            continue
        l = line.split(" ")
        l1.append(l[0])
        l2.append(l[1])
    return (l1, l2)

def getRandInts():
    randInt = []
    for i in range(100):
        randInt.append(random.randrange(100000))
    return randInt

def usingDictionary(randInts, d):
    now = time.time()

    d = getDict(d)

    print("This is using a dictionary")
    for i in randInts:
        print("key:{} val:{}".format(i, d.get(str(i))))

    print("It took this long {}.".format(time.time() - now))

def usingLists(randInts, d):
    now = time.time()

    lists = getLists(d)
    l1 = lists[0]
    l2 = lists[1]

    print("This is using a list")
    for i in randInts:
        index = l1.index(str(i))
        print("key:{} val:{}".format(i, l2[index]))

    print("It took this long {}.".format(time.time() - now))


def main():
    d = getInput("/Users/GlennRC/Desktop/data.txt")
    randInts = getRandInts()
    usingDictionary(randInts, d)
    usingLists(randInts, d)

if __name__ == "__main__":
    main()
