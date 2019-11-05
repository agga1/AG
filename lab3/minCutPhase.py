from queue import PriorityQueue
from lab3.dimacs import *
from lab3.node import *
import heapq

def minimumCutPhase( G ):
    a = 1
    S = []
    S.append(a)
    q = []
    currFlow = 0
    for vkey, vVal in G[a].edges.items():
        q.append([vVal, vkey])
        currFlow += vVal
    heapq.heapify(q)
    prevFlow = currFlow
    print(list(q))
    while not len(q)==0:
        v = heapq.heappop(q)
        print("\npopped ", v)
        S.append(v[1])
        prevFlow = currFlow
        currFlow = 0
        for key, val in G[v[1]].edges.items():
            print(" neigh ", key, end=" ")
            if key in S:
                continue
            i = 0
            while len(q)> i and q[i][1]!=key:
                i += 1
            if len(q) == i:
                print(key, " not in q ")
                heapq.heappush(q, [val, key])
                currFlow += val
                print(list(q))
                continue
            if q[i][1] == key:
                print("updating ",q[i], end="")
                q[i][0] += val
                currFlow += q[i][0]
                heapq.heapify(q)
    print(S)
    print("flow ", prevFlow)



(V, L) = loadWeightedGraph("res/cycle")  # wczytaj graf
G = [Node() for i in range(V + 1)]

for (x, y, c) in L:
    G[x].addEdge(y, c)
    G[y].addEdge(x, c)

minimumCutPhase( G )