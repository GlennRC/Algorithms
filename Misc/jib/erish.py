a = []

print("hello")


def minEditDist(p: str, t: str):
    p = " " + p
    t = " " + t
    matrix = [[0]*(len(p)) for _ in range(len(t))]

    for i in range(len(p)):
        matrix[0][i] = i

    for i in range(len(t)):
        matrix[i][0] = i

    def sub(a, b):
        return 0 if a == b else 2

    for i in range(1, len(t)):
        for j in range(1, len(p)):
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+sub(t[i], p[j]))

    return matrix[len(t)-1][len(p)-1]