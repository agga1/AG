from lab3.dimacs import *
from lab3.node import Node

# (V, L) = loadWeightedGraph( "res/clique5" )
#
# G = [ Node() for i in range(V+1) ]
#
# for (x, y, c) in L:
#   G[x].addEdge(y, c)
#   G[y].addEdge(x, c)


def mergeVertices(G, x, y):  # y will be deleted
    print(" merging ", x, y)
    for key, weight in G[y].edges.items():
        G[y].active = False
        G[key].delEdge(y)
        if key == x:  # ignore x-y edge
            continue
        G[key].addEdge(x, weight)
        G[x].addEdge(key, weight)
    G[y].edges = {}  # redundant, maybe delete to keep inf about original graph?
    G[x].mergedWith.append(y)

# mergeVertices(G, 1 , 2)
# print(G[1].edges)

