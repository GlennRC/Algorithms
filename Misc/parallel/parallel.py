import math




def main():

    p = 1
    n = 10

    while (p <= 128):
        time_parallel = (n**2/p) + math.log(p,2)
        time_serial = n**2
        speedup = time_serial/time_parallel
        efficiency = speedup/p
        print(time_parallel, speedup, efficiency)
        p *= 2
    print()


    p = 1
    while (n <= 320):
        time_parallel = (n**2/p) + math.log(p,2)
        time_serial = n**2
        speedup = time_serial/time_parallel
        efficiency = speedup/p
        print(time_parallel, speedup, efficiency)
        n *= 2


if __name__ == "__main__":
    main()



