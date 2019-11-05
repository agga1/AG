from queue import PriorityQueue
from lab3.dimacs import *
from lab3.node import *

def minimumCutPhase( G ):
    a = 1
    S = []
    S.append(a)
    q = PriorityQueue(len(G))
    q.put(10, a)
    q.put(8, a)
    print(q.get())
    # for vkey, vVal in G[a].edges.items():
    #     q.put(vVal, (vkey, vVal))
    # while len(S) < len(G):
    #     v = q.get()
    #     S.append(v)
    #     for vkey, vVal in G[v].edges.items():
    #         if vkey in S:
    #             continue
    #         currVal = q.get(vkey)
    #         q.put(vVal, vkey)
    #     print(v)


(V, L) = loadWeightedGraph("res/clique5")  # wczytaj graf
G = [Node() for i in range(V + 1)]

for (x, y, c) in L:
    G[x].addEdge(y, c)
    G[y].addEdge(x, c)

minimumCutPhase( G )