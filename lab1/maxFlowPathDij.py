from adjListConversion import getAdjList
from readGraph import *
import sys

G = loadWeightedGraph("res/clique1000")
from lab1.Heap import Heap


def biggestWeight(E):
    return max(E, key=lambda p: p[2])[2]


def maxFlowPathDij(G, s, t):
    adj = getAdjList(G)
    gVal = biggestWeight(G[1])
    maxFlow = [0]*len(adj)
    maxFlow[s] = gVal
    mheap = Heap(None)
    mheap.push(s)
    while not mheap.is_empty():
        curr = mheap.top()
        for edge in adj[curr]:
            if maxFlow[edge[0]] < min(maxFlow[curr], edge[1]):
                maxFlow[edge[0]] = min(maxFlow[curr], edge[1])
                mheap.push(edge[0])

    #print(maxFlow[t])
    return maxFlow[t]


#print(maxFlowPathDij(loadWeightedGraph(sys.argv[1]), 1, 2))

#print(sys.argv[1])
print(maxFlowPathDij(G, 1, 2))
