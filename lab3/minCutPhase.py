from queue import PriorityQueue
from lab3.mergeVertices import mergeVertices
from lab3.dimacs import *
from lab3.node import *


def minimumCutPhase(G, active_vertices=None):
    a = 1
    S = [a]
    if active_vertices is None:  # get actual nr of vertices, without merged ones
        active_vertices = len(G)-1
        for node in G:
            if not node.active:
                active_vertices -= 1

    q = PriorityQueue()
    q_dict = {}  # contains actual flow from key to all vert in S
    currFlow = 0
    for vkey, vVal in G[a].edges.items():
        q.put((-vVal, vkey))
        q_dict[vkey] = -vVal
    while len(S) < active_vertices:
        v = q.get()
        print(" got ", v)
        if v[1] not in q_dict:  # vertex is already in S, this entry has been updated with bigger weight before
            continue
        del q_dict[v[1]]
        S.append(v[1])
        currFlow = -1*v[0]
        for key, val in G[v[1]].edges.items():
            if key in S:  # edge v-key inside S
                continue
            q_dict[key] = q_dict.get(key, 0) - val
            q.put((q_dict[key], key))
    mergeVertices(G, S[-1], S[-2])
    return currFlow

#
# (V, L) = loadWeightedGraph("res/grid5x5")  # wczytaj graf
# G = [Node() for i in range(V + 1)]
#
# for (x, y, c) in L:
#     G[x].addEdge(y, c)
#     G[y].addEdge(x, c)

# ans = len(G)-1
# for i in range(len(G)-2):
#     ans = min(minimumCutPhase( G ), ans)
# print(ans)