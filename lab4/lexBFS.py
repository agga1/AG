from lab4.dimacs import loadWeightedGraph

V, L = loadWeightedGraph("res/chordal/example-fig5")
print(L)

def to_adj_dict(G):
    neighs = [{} for x in range(V + 1)]
    for edge in G[1]:
        neighs[edge[0]][edge[1]] = edge[2]
        neighs[edge[1]][edge[0]] = edge[2]
    return neighs


def lexBFS(G):
    V = G[0]
    neighs = to_adj_dict(G)
    sets = []
    startSet = [x for x in range(1, V+1)]
    sets.append(startSet)
    while len(sets) > 0:
        v = sets[0].pop()
        print(v)
        if len(sets[0]) == 0:
            del sets[0]
        newSets = []
        for set in sets:
            neigh_v = []
            not_neigh_v = []
            for x in set:
                if x in neighs[v]:
                    neigh_v.append(x)
                else:
                    not_neigh_v.append(x)
            if neigh_v:
                newSets.append(neigh_v)
            if not_neigh_v:
                newSets.append(not_neigh_v)
        sets = newSets

lexBFS((V,L))
