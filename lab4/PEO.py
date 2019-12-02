import os

from lab4.create_graph import create_graph
from lab4.lexBFS import lexBFS
from lab4.Node import Node
from typing import List


def check_if_PEO(G: List[Node], ord: List[int]) -> bool:
    RN = [ set() ]* len(G)
    parent = [0]*len(G)
    for v in ord:
        # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
        for el in ord:
            if el == v:
                break
            if el in G[v].out:
                RN[v].add(el)
                parent[v] = el
        if parent[v] != 0:
            RN[v].remove(parent[v])

    for v in ord:
        if not RN[v] <= RN[parent[v]]:
            return False
    return True


graphs = []
for name in os.listdir("res/chordal"):
    graphs.append(f"res/chordal/{name}")


for ind, graph in enumerate(graphs):
    if ind > 0:
        break
    G = create_graph(graph)
    vs = lexBFS(G)
    graph = graph.split("/")[-1]
    print(check_if_PEO(G, vs))
