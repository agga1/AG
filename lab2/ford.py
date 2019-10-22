from lab2.BFS import BFS
from lab2.dimacs import loadDirectedWeightedGraph
from lab1.adjListConversion import getAdjList

G = loadDirectedWeightedGraph("graphs-lab2/flow/clique20")


def fordFulkerson(G, s, t):
    max_flow = 0
    resG = createResidual(G) # residual graph represented by a matrix
    parent = [-1]*(G[0]+1)
    while BFS(resG, s, t, parent):
        path_flow = float("Inf")
        v = t
        while v != s:
            path_flow = min(path_flow, resG[parent[v]][v])
            v = parent[v]

        max_flow += path_flow
        v = t
        while v != s:
            u = parent[v]
            resG[u][v] -= path_flow
            resG[v][u] += path_flow
            v = parent[v]

    return max_flow


def createResidual(G):
    matrix = [[0 for x in range(G[0]+1)] for y in range(G[0]+1)]
    for edge in G[1]:
        matrix[edge[0]][edge[1]] = edge[2]
    return matrix


print(createResidual(G))

print(fordFulkerson(G, 1, G[0]))
