from testPackage.adjListConversion import getAdjList
from testPackage.maxFlowPathBin import biggestWeight
from testPackage.readGraph import *

G = loadWeightedGraph("res/clique1000")


def maxFlowPathDij(G, s, t):
    print("start")
    adj = getAdjList(G)
    gVal = biggestWeight(G)
    maxFlow = [0]*len(adj)
    maxFlow[s] = gVal
    mheap = []
    mheap.append(s)
    while len(mheap)>0:
        curr = mheap.pop(0)
        for edge in adj[curr]:
            if maxFlow[edge[0]] < min(maxFlow[curr], edge[1]):
                maxFlow[edge[0]] = min(maxFlow[curr], edge[1])
                mheap.append(edge[0])

    print(maxFlow[t])
    return maxFlow[t]


maxFlowPathDij(G, 1, 2)
