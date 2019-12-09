from lab4.Node import Node
from typing import List
from utils.test_utils import test
from utils.test_utils import load_graph_as_nodes
from lab4.lexBFS import lexBFS
import os
from utils.create_graph import create_graph


# @test(data="res/coloring", loader=load_graph_as_nodes)
def graph_coloring(G: List[Node]) -> int:
    color = [0]*len(G)
    ordered = lexBFS(G)
    for v in ordered:
        neigs = G[v].out
        used = {color[u] for u in neigs}
        min_free_col = 1
        while min_free_col <= len(G):
            if min_free_col not in used:
                break
            min_free_col += 1
        color[v] = min_free_col
    return max(color)


graphs = []
for name in os.listdir("res/coloring"):
    graphs.append(f"res/coloring/{name}")
# graphs = ["res/chordal/cycle4"]
for ind, graph in enumerate(graphs):
    if ind == 0:
        continue
    G = create_graph(graph)
    graph = graph.split("/")[-1]
    print(graph_coloring(G), " for ", graph)
