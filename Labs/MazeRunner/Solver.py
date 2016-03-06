import os
import time

'''
This was worked on by Glenn Contreras and Neha Tammana.
The basic operation is the nodes we explore in the maze.
The input size is the size of the matrix(maze).
'''


def getMaze(path):
    matrix = []
    with open(path) as g:
        graph = g.read()
        graph = graph.split()
        for line in graph:
            matrix.append([i for i in line])
    return matrix


def findChar(maze, char):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == char:
                return row, col, 0
    print("shit has no char")
    return None


def isWall(maze, space):
    if maze[space[0]][space[1]] == '*':
        return True
    else:
        return False


def isVisited(queue, space):
    for pos in queue:
        if space[0] == pos[0] and space[1] == pos[1] and space[2] >= pos[2]:
            return True
    return False


def markMaze(maze, queue):
    for pos in queue:
        maze[pos[0]][pos[1]] = pos[2];


def isEnd(pos, end):
    if pos[0] == end[0] and pos[1] == end[1]:
            return True
    return False


def findShortestPath(maze, queue, end):
    count = 0
    for pos in queue:
        space = pos[0]+1, pos[1], pos[2]+1
        if not isWall(maze, space) and not isVisited(queue, space):
                queue.append(space)
        if isEnd(space, end):
            break
        space = pos[0]-1, pos[1], pos[2]+1
        if not isWall(maze, space) and not isVisited(queue, space):
                queue.append(space)
        if isEnd(space, end):
            break
        space = pos[0], pos[1]+1, pos[2]+1
        if not isWall(maze, space) and not isVisited(queue, space):
                queue.append(space)
        if isEnd(space, end):
            break
        space = pos[0], pos[1]-1, pos[2]+1
        if not isWall(maze, space) and not isVisited(queue, space):
                queue.append(space)
        if isEnd(space, end):
            break
        count += 1
    return count


def prettyPrint(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print(str(maze[row][col]), "\t", end="")
        print()


def isSolved(maze, end):
    if type(maze[end[0]+1][end[1]]) is int:
        return True
    if type(maze[end[0]-1][end[1]]) is int:
        return True
    if type(maze[end[0]][end[1]+1]) is int:
        return True
    if type(maze[end[0]][end[1]-1]) is int:
        return True
    return False


def showSolvedPath(maze, end, count):
    node = maze[end[0]+1][end[1]]
    if type(node) is int and node < count:
        maze[end[0]][end[1]] = '^'
        showSolvedPath(maze, (end[0]+1, end[1]), node)
        return
        
    node = maze[end[0]-1][end[1]]
    if type(node) is int and node < count:
        maze[end[0]][end[1]] = 'v'
        showSolvedPath(maze, (end[0]-1, end[1]), node)
        return

    node = maze[end[0]][end[1]+1]
    if type(node) is int and node < count:
        maze[end[0]][end[1]] = '<'
        showSolvedPath(maze, (end[0], end[1]+1), node)
        return

    node = maze[end[0]][end[1]-1]
    if type(node) is int and node < count:
        maze[end[0]][end[1]] = '>'
        showSolvedPath(maze, (end[0], end[1]-1), node)
        return


def main():
    mazes = os.listdir("mazes")
    try:
        print("Maze Solver")
        for fileName in mazes:
            if 'maze' in fileName:
                print(fileName)
                maze = getMaze('mazes/{}'.format(fileName))

                start = findChar(maze, 's')
                end = findChar(maze, 'e')
                queue = [start]

                s = time.time()
                opCount = findShortestPath(maze, queue, end)
                totalTime = time.time() - s

                markMaze(maze, queue)
                solved = isSolved(maze, end)
                numSteps = maze[end[0]][end[1]]
                showSolvedPath(maze, end, float('inf'))

                prettyPrint(maze)
                if solved:
                    print("Shortest Path: {}".format(numSteps))
                else:
                    print("No path")
                print("Time: {}".format(totalTime))
                print("Basic Operations: {}".format(opCount))

                print()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()