from lab4.dimacs import loadWeightedGraph


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)

    def __repr__(self):
        return str(self.idx)

#
#
# (V, L) = loadWeightedGraph("res/chordal/AT")
#
# G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka
#
# for (u, v, _) in L:
#   G[u].connect_to(v)
#   G[v].connect_to(u)



