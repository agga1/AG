from lab7.dimacs import *
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort
from typing import Dict, Optional, List
import os

def getExpression(name):
    (V, F) = loadCNFFormula(name)
    return F

def toNxGraph(name):
    (V,F) = loadCNFFormula(name)
    G = nx.DiGraph()
    G.add_nodes_from([x for x in range(-V, V+1)])
    G.remove_node(0)
    for edge in F:
        G.add_edge(-edge[0], edge[1])
        G.add_edge(-edge[1], edge[0])
    # for x in G.nodes:
        # print("x: ",x , " ",G.adj[x])
    return G


def any2CNF(name: str) -> Optional[Dict[int, bool]]:
    G = toNxGraph(name)

    SCC = strongly_connected_components(G)  # returns generator
    SCCList = []
    mapVtoComp = {}
    t = 0
    for S in SCC:
        SCCList.append(S)
        for v in S:
            if -v in S:
                # print("in ", t, " both ", v, " and ", -v, " are present")
                return None
            mapVtoComp[v] = t
        t += 1

    H = nx.DiGraph()  # graf w którym wierzchołkami są silnie spójne składowe (dokladnie ich ind w SCCList
    H.add_nodes_from([x for x in range(0, t)])
    # print(mapVtoComp)
    for ind, S in enumerate(SCCList):
        for v in S:
            for u in G.adj[v].keys():
                if mapVtoComp[u] != mapVtoComp[v]:
                    H.add_edge(mapVtoComp[v], mapVtoComp[u])

    topSort = topological_sort(H)
    vBoolValues = {}
    for x in topSort:
        # print(x, " ", SCCList[x])
        for v in SCCList[x]:
            if v not in vBoolValues.keys():
                vBoolValues[v] = False
                vBoolValues[-v] = True

    return vBoolValues


def checkProposedEval(anyEval: Dict[int, bool], expr: List[List[int]]) -> bool:
    for pear in expr:
        if not (anyEval[pear[0]] or anyEval[pear[1]]):
            print("formula is incorrect!")
            return False
    return True


dirName = "graphs/sat"

for fileName in os.listdir(dirName):
    name = f"{dirName}/{fileName}"
    anyEval = any2CNF(name)
    if anyEval is not None:
        print(checkProposedEval(anyEval, getExpression(name)))
