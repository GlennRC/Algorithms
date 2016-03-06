
def theAlgo(a):
    for i in range(len(a)-1):
        if a[i+1] - a[i] > 1:
            return a[i] + 1


def main():
    a = [1,2,3,4,5,6,7,9]
    print(theAlgo(a))

if __name__ == "__main__":
    main()