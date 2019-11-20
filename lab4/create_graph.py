from lab4.dimacs import loadWeightedGraph
from lab4.node import Node

def create_graph(name):
    (V, L) = loadWeightedGraph(name)

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    return G
