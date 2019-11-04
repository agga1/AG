from lab2.dimacs import loadDirectedWeightedGraph
from lab2.BFSDictRepr import BFS

G = loadDirectedWeightedGraph("graphs-lab2/flow/trivial2")


def fordFulkerson(G, s, t):
    max_flow = 0
    V = G[0]
    resG = createResidual(G) # residual graph represented by a dict of dict
    # print(resG)
    parent = [-1]*(V+1)
    while BFS(resG, s, t, parent, V):
        # print("exist path")
        path_flow = float("Inf")
        v = t
        while v != s:
            path_flow = min(path_flow, resG[parent[v]][v])
            v = parent[v]
        # print("path_flow", path_flow)
        max_flow += path_flow
        v = t
        while v != s:
            u = parent[v]
            resG[u][v] -= path_flow
            resG[v][u] += path_flow
            v = parent[v]
        # print(resG)

    return max_flow


def createResidual(G):  # G - G[0] = |V|, G[1] - list of edges (u, v, weight)
    edgesDict = {}
    for edge in G[1]:
        edgesDict[edge[0]] = {}
        edgesDict[edge[1]] = {}
    for edge in G[1]:
        edgesDict[edge[0]][edge[1]] = edge[2]
        edgesDict[edge[1]][edge[0]] = edge[2]  # in dir = 0

    # print(edgesDict)
    return edgesDict


# print(createResidual(G))
# resG = createResidual(G)
# parent = [-1]*(G[0]+1)
# print(parent)
# print(BFS(resG, 1, 2, parent, G[0]))
# print(parent)
# print(fordFulkerson(G, 1, G[0]))
