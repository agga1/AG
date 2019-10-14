from testPackage.readGraph import loadWeightedGraph

G = loadWeightedGraph("res/g1")


def getAdjList(G):  # G[0] = V, G[1] = L
    """returns list of lists of [vNr, edgeWeight]
    al[vertexNr] = [[neigh1Nr, edgeWeight], [neigh2Nr, edgeWeight], ...]
    """
    al = []
    for i in range(0, G[0]+1):
        al.append([])
    for edge in G[1]:
        al[edge[0]].append([edge[1], edge[2]])
        al[edge[1]].append([edge[0], edge[2]])
    return al


#getAdjList(G)


