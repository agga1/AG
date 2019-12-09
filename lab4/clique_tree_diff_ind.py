from typing import List
from lab4.Node import Node
from lab4.lexBFS import lexBFS
import os
from utils.create_graph import create_graph


def clique_tree(G: List[Node]):
    ord = lexBFS(G)
    parent = [0] * len(G)
    cliques = []  # list of all cliques
    clique_par = [0]*len(G)  # index of parent clique
    clique_nr = [0] * len(G)  # nr of clique corresponding to vertex i
    # creating RN list
    RN = [set() for _ in range(len(G))]  # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
    for v in ord:
        for el in ord:
            if el == v:
                break
            if el in G[v].out:
                RN[v].add(el)
                parent[v] = el
    # creating tree
    v = ord[0]
    cliques.append({v})
    clique_nr[v] = 0
    clique_par[0] = 0
    for i in range(1, len(ord)):
        v = ord[i]
        # print(" \t at v ", v)
        if len(RN[v].symmetric_difference(cliques[clique_nr[parent[v]]])) == 0:
            clique_nr[v] = clique_nr[parent[v]]
            cliques[clique_nr[v]].add(v)
            # print(" adding to cliq nr ", clique_nr[v], " and now " ,cliques[clique_nr[v]])
            # print(" now clique is : ", cliques[clique_nr[v])
        else:
            cliques.append(RN[v] | {v})
            newInd = len(cliques)-1
            clique_nr[v] = newInd
            # print(" new clique nr ", newInd, " w parent ", clique_nr[parent[v]])
            # print(" now clique is : ", cliques[clique_nr[v])
            clique_par[newInd] = clique_nr[parent[v]]
    print(cliques)
    print(clique_par)

graphs = []
for name in os.listdir("res/interval"):
    graphs.append(f"res/interval/{name}")
# graphs = ["res/chordal/cycle4"]
for ind, graph in enumerate(graphs):
    # if ind > 0:
    #     break
    G = create_graph(graph)
    graph = graph.split("/")[-1]
    clique_tree(G)



