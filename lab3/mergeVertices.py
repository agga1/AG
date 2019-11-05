from lab3.dimacs import *
from lab3.node import Node

(V, L) = loadWeightedGraph( "res/clique5" )

G = [ Node() for i in range(V+1) ]

for (x, y, c) in L:
  G[x].addEdge(y, c)
  G[y].addEdge(x, c)


def mergeVertices( G, x, y):
    for key, weight in G[y].edges.items():
        print(key, weight)
        G[y].active = False
        if key == x:
            continue
        if key in G[x].edges:
            G[x].edges[key] += weight
        else:
            G[x].edges[key] = weight
        G[y].edges = {}


mergeVertices(G, 1 , 2)
print(G[1].edges)

