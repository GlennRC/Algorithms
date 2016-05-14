def incseq(seq):
    position = [None for i in range(len(seq))]
    middle = [None for i in range(len(seq))]

    length = 1
    middle[0] = 0

    for i in range(1, len(seq)):
        lower = 0
        upper = length

        if seq[middle[upper-1]] < seq[i]:
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[middle[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid
            j = lower
        position[i] = middle[j-1]

        if j == length or seq[i] < seq[middle[j]]:
            middle[j] = i
            length = max(length, j+1)

    result = []
    pos = middle[length-1]
    for i in range(length):
        result.append(seq[pos])
        pos = position[pos]

    return result[::-1]

a = [0, 8, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15, 4]

print(incseq(a))