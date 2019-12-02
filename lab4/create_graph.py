from lab4.dimacs import loadWeightedGraph
from lab4.Node import Node
from typing import List


def create_graph(name: str) -> List[Node]:
    (V, L) = loadWeightedGraph(name)

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    return G
