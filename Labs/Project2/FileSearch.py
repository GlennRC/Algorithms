import time


"This was worked on by Glenn Contreras and Neha Tammana"


def getShiftTable(pattern):
    table = {}

    for i in range(len(pattern)):
        table.update({pattern[i]: len(pattern)})

    for j in range(len(pattern)-1):
        table[pattern[j]] = len(pattern) - 1 - j

    table.update({"else": len(pattern)})

    return table


def matchString(p: str, t: str):
    e = 0
    if t.find(p) != -1:
        return e

    for i in range(len(p)):
        if p[i] != t[i]:
            e += 1

    return e


def horspools(pattern, text):
        text = text.lower()
        pattern = pattern.lower()
        table = getShiftTable(pattern)
        matches = []

        m = len(pattern)
        i = m-1

        while i <= len(text)-1:
            t = text[i-m+1:i+1]
            result = matchString(pattern, t)

            if result == 0:
                return [(i-m+1, t)]
            if result == 1:
                matches.append((i-m+1, t))

            if table.get(text[i]):
                i += table[str(text[i])]
            else:
                i += table["else"]

        return matches


def main():

    fileName = input("Enter the file name: ")
    fileName = "./SampleFiles/{}".format(fileName)
    pattern = input("Enter the pattern to match: ")

    with open(fileName) as file:
        content = file.read()

    start = time.time()
    matches = horspools(pattern, content)
    end = time.time() - start
    print("Number of matches: {}".format(len(matches)))
    if len(matches) == 1: print("Exact")
    print("Matches: {}".format(matches))
    print("Time: {}".format(end))


if __name__ == "__main__":
    main()
