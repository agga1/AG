from adjListConversion import getAdjList
from readGraph import loadWeightedGraph

G = loadWeightedGraph("res/g1")


def bfs(G, s, t, minWeight):
    adj = getAdjList(G)
    vis = [0 for i in range(0, len(adj))]
    vis[s] = 1
    mheap = []
    mheap.append(s)
    while len(mheap) > 0:
        curr = mheap.pop(0)
        vis[curr] = 1
        for neigh in adj[curr]:
            if neigh[1] < minWeight or vis[neigh[0]]:
                continue
            if neigh[0] == t:
                return True
            else:
                mheap.append(neigh[0])
    return False


print(bfs(G, 1, 2, 5))


