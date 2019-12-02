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
