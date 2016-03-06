'''
 Lab6: Topological sort
 By Glenn Contreras & Neha Tammana
'''

def getGraph(path):
    matrix = []
    try:
        with open(path) as g:
            graph = g.read()
            graph = graph.split()
            for line in graph:
                matrix.append([i for i in line])
        return matrix
    except Exception as e:
        print(e)
        return None

def removeSource(source, graph, ordered):
    for row in range(len(graph)):
        graph[source][row] = '0'
    graph[source][source] = '1'
    print(source)
    ordered.append(source)
    return graph

def stillSourcesLeft(graph):
    for col in range(len(graph)):
        for row in range(len(graph)):
            if graph[row][col] == '1':
                break
        else:
            return True

def isSource(source, graph):
    for row in range(len(graph)):
        if graph[row][source] == '1':
            return False
    return True

def topSort(graph):
    if graph == None:
        return
    ordered = []
    while(stillSourcesLeft(graph)):
        for node in range(len(graph)):
            if isSource(node, graph):
                removeSource(node, graph, ordered)
    if len(ordered) != len(graph):
        print("This is not an acyclic graph")

def main():

    # If you want to sort one graph at a time
    '''
    graphName = 'graph1'
    print('Sort for ' + graphName)
    graph = getGraph('graphs/{}.txt'.format(graphName))
    topSort(graph)
    '''

    # This will sort all the graphs in the graph folder
    numOfGraphs = 3
    for i in range(1, numOfGraphs + 1):
        print("Sort for graph{}".format(i))
        graph = getGraph('graphs/graph{}.txt'.format(i))
        topSort(graph)
        print()

if __name__ == "__main__":
    main()