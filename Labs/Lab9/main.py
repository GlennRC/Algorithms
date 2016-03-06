class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumLeaves(root):
    if not root.left and not root.right:
        return 1
    else:
        return sumLeaves(root.left) + sumLeaves(root.right)

"""
M(n) = M(n/2) + 1
C(n) = C(n-1) + 1
"""

def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a, n/2)*power(a,n/2)
    else:
        return (power(a, (n-1)/2))*(power(a,(n-1)/2))*a

def powerBF(a,n):
    if n == 0:
        return 1
    else:
        return a * powerBF(a,n-1)


def main():
    n = Node(19)
    n.left = Node(1)
    n.right = Node(21)
    t = Node(34)
    t.left = n
    a = Node(50)
    a.left = Node(46)
    a.right = Node(87)
    t.right = a

    print(power(3,3))

    print(str(sumLeaves(t)))


if __name__ == "__main__":
    main()