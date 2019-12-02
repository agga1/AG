import os

from utils.create_graph import create_graph
from lab4.lexBFS import lexBFS
from lab4.Node import Node
from typing import List


def is_PEO(G: List[Node], ord: List[int]) -> bool:
    RN = [ set() for _ in range(len(G))]
    parent = [0]*len(G)
    for v in ord:
        # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
        for el in ord:
            if el == v:
                break
            if el in G[v].out:
                RN[v].add(el)
                parent[v] = el

    for v in ord:
        diff = RN[v] - RN[parent[v]]
        diff.discard(parent[v])
        if len(diff) > 0:
            return False
    return True


# graphs = []
# for name in os.listdir("res/chordal"):
#     graphs.append(f"res/chordal/{name}")
#
# graphs = ["res/chordal/cycle4"]
# for ind, graph in enumerate(graphs):
#     if ind > 0:
#         break
#     G = create_graph(graph)
#     vs = lexBFS(G)
#     graph = graph.split("/")[-1]
#     print(is_PEO(G, vs))
