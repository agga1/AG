from lab2.dimacs import loadDirectedWeightedGraph

G = loadDirectedWeightedGraph("graphs-lab2/connectivity/clique100")

from lab2.fordDictRepr import fordFulkerson


def graphConnectivity (G):
    if len(G[1]) < G[0]/2:  # graph is already disconnected
        return 0
    max_flow = G[0]
    s = 1
    t = 2
    while t <= G[0]:
        loc_max_flow = fordFulkerson(G, s, t)
        # print(s, t)
        # print(loc_max_flow)
        t += 1
        max_flow = min(max_flow, loc_max_flow)
    return max_flow


print(graphConnectivity(G))
