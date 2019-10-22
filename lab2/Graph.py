from lab1.adjListConversion import getAdjList

class Graph:

    def __init__(self, graph, V, L):
        self._graph = graph
        self.V = V
        self.L = L
        self.adj = getAdjList((V, L))
