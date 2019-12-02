from typing import List
from lab4.Node import Node
from lab4.is_chordal import is_chordal
from utils.test_utils import test
from utils.test_utils import load_graph_as_nodes
from lab4.lexBFS import lexBFS


# @test(data="res/maxclique", loader=load_graph_as_nodes)
def biggest_clique(G: List[Node]) -> int:
    """ returns size of the biggest clique in given chordal graph """
    assert (is_chordal(G)), "Received graph is not chordal! "
    ord = lexBFS(G)
    max_size = 0
    RN = [set() for _ in range(len(G))]  # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
    for v in ord:
        for el in ord:
            if el == v:
                break
            if el in G[v].out:
                RN[v].add(el)
        max_size = max(max_size, len(RN[v])+1)

    return max_size


# graphs = []
# for name in os.listdir("res/maxclique"):
#     graphs.append(f"res/maxclique/{name}")
# # graphs = ["res/chordal/cycle4"]
# for ind, graph in enumerate(graphs):
#     # if ind > 0:
#     #     break
#     G = create_graph(graph)
#     graph = graph.split("/")[-1]
#     print(biggest_clique(G), " for ", graph)
