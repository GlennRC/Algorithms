import os
import heapq
import time

"""
    This project was worked on Glenn Contreras and Neha Tammana
"""


def getFreq(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq.update({ch: freq.get(ch)+1})
        else:
            freq.update({ch: 1})
    return freq


def getHuffmanEncode(freq: dict):
    heap = []
    for key, val in freq.items():
        heap.append([val, [key, ""]])

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        for node in left[1:]:
            node[1] = '0' + node[1]

        right = heapq.heappop(heap)
        for node in right[1:]:
            node[1] = '1' + node[1]

        tree = [left[0] + right[0]]
        tree.extend(left[1:] + right[1:])
        heapq.heappush(heap, tree)

    heap = heap[0]
    heap.pop(0)
    return heap


def compress(text, huffman):
    def _comp(l):
        for item in huffman:
            if l == item[0]:
                return item[1]

    compressed = ""
    for letter in text:
        compressed += _comp(letter)
    return compressed


def uncompress(text, huffman):
    def match(_b):
        for item in huffman:
            if _b == item[1]:
                return item[0]
        return None

    t = text
    uncomp = ""
    bit = ""
    for letter in t:
        bit += letter
        m = match(bit)
        if m:
            uncomp += m
            bit = ""
    return uncomp


def main():
    uncompDir = "/Uncompressed"
    compDir = "/Compressed"

    print("This is an implementation of Huffman's compression algroithm.")
    filedir = input("Specify the directory located in the Uncompressed folder."
                    "\nDo not provide a backslash\n:")
    if filedir == "":
        print("No directory specified.")
        return

    files = []
    fileName = ""
    print("Enter the file name or files to be encoded. "
          "Press ENTER after each file name.\n Enter 'EXIT' "
          "to stop.\n Enter 'All' to compress everything in the dir.")
    while True:
        fileName = input("File name: ")
        if fileName.lower() != "exit" and fileName.lower() != "all":
            files.append(fileName)
        else: break

    if fileName.lower() == 'all':
        files = os.listdir(".{}/{}".format(uncompDir, filedir))
        thing = ".DS_Store"
        if thing in files:
            files.remove(thing)

    if not files:
        print("No files specified.")
        return

    for f in files:
        with open(".{}/{}/{}".format(uncompDir, filedir, f)) as uncompressed:
            text = uncompressed.read()
            huffman = getHuffmanEncode(getFreq(text))

            start = time.time()
            compressed = compress(text, huffman)
            end = time.time()
            uncompressed = uncompress(compressed, huffman)

            print("\nTime to compress {}: {}".format(f, end-start))
            print("Original: {}".format(text))
            print("Compressed: {}".format(compressed))
            print("Uncompressed: {}".format(uncompressed))

            with open(".{}/{}".format(compDir, f), "w") as file:
                file.write(compressed)


if __name__ == "__main__":
    main()


