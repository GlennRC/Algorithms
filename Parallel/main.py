import math

threads = int(input("Enter Threads: "))
length = int(input("Enter lenth of string: "))

print()
print("Number of threads: " + str(threads))
print("Length of String: " + str(length))
total = math.factorial(length)
print("Total permutations: " + str(total))

load = total/threads
totalExtra = total % threads
loadExtra = totalExtra/threads

print("load: {}, total extra: {}, load extra: {}".format(load, totalExtra, loadExtra))

print("Total load per thread: " + str(load+loadExtra))

