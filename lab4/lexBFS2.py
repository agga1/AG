import os


def lexBFS(G):

    sets = []
    vs= []
    startSet = [x for x in range(1, len(G))]
    sets.append(startSet)
    while len(sets) > 0:
        v = sets[0].pop()
        vs.append(v)
        # print(v)
        if len(sets[0]) == 0:
            del sets[0]
        newSets = []
        for set in sets:
            neigh_v = []
            not_neigh_v = []
            for x in set:
                if x in G[v].out:
                    neigh_v.append(x)
                else:
                    not_neigh_v.append(x)
            if neigh_v:
                newSets.append(neigh_v)
            if not_neigh_v:
                newSets.append(not_neigh_v)
        sets = newSets
    return vs


