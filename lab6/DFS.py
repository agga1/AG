
def dfs(adj, s, t, minWeight, vis):
    vis[s] = 1
    for neigh in adj[s]:
        if neigh[1] < minWeight or vis[neigh[0]]:
            continue
        if neigh[0] == t:
            return True
        if dfs(adj, neigh[0], t, minWeight, vis):
            return True
    return False


def dfsWrap(G, s, t, minWeight):
    adj = getAdjList(G)
    vis = [0 for i in range(0, len(adj))]
    vis[s] = 1
    for neigh in adj[s]:
        if neigh[1] < minWeight or vis[neigh[0]]:
            continue
        if neigh[0] == t:
            return True
        if dfs(adj, neigh[0], t, minWeight, vis):
            return True
    return False

