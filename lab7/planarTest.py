import networkx as nx
from lab7.dimacs import loadWeightedGraph
from networkx.algorithms.planarity import check_planarity
import os


def toNxGraph(name):
    myG = loadWeightedGraph(name)
    G = nx.Graph()
    G.add_nodes_from([x for x in range(1, myG[0] + 1)])
    for edge in myG[1]:
        G.add_edge(edge[0], edge[1])
    return G


graphs = []
for name in os.listdir("graphs/plnar"):
    graphs.append(f"graphs/plnar/{name}")

for graph in graphs:
    G = toNxGraph(graph)

    res = check_planarity(G)[0]
    print(graph, "\t", res)


