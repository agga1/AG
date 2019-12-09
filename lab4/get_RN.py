from lab4.Node import Node
from typing import List
from lab4.lexBFS import lexBFS


def get_RN(G: List[Node]) -> List[set[int]]:
    RN = [set() for _ in range(len(G))]
    parent = [0] * len(G)
    ord = lexBFS(G)
    for v in ord:
        # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
        for el in ord:
            if el == v:
                break
            if el in G[v].out:
                RN[v].add(el)
                parent[v] = el
    return RN
