from lab3.dimacs import *
from lab3.mergeVertices import mergeVertices
from lab3.minCutPhase import minimumCutPhase
from lab3.node import *

def stoer_wagner(G):
    if len(G) < 2:
        return 0
    ans = minimumCutPhase(G)
    for i in range(len(G) - 3):  # G longer by 1, 1 already executed, and no action if 1 vertex left
        ans = min(minimumCutPhase(G), ans)
    return ans


(V, L) = loadWeightedGraph("res/grid5x5")  # wczytaj graf
G = [Node() for i in range(V + 1)]

for (x, y, c) in L:
    G[x].addEdge(y, c)
    G[y].addEdge(x, c)

print(stoer_wagner(G))