from testPackage.readGraph import *
from testPackage.unionFind import *


def maxFlowPath(G, s, t):  # G[0] = V, G[1] = L
    V = G[0]
    G = sortEdges(G)
    printEdges(G)
    L = G[1]
    par = [x for x in range(0, V+1)]
    flow = 0
    for edge in L:
        union(par, edge[0], edge[1])
        flow = edge[2]
        if connected(par, s, t):
            return flow
    return flow


G = loadWeightedGraph("res/clique5")
print(maxFlowPath(G, 1, 4))
