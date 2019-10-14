def find(par, i):
    if par[i] != i:
        par[i] = find(par, par[i])
    return par[i]


def union(par, i, j):
    pi, pj = find(par, i), find(par, j)
    if pi != pj:
        par[pi] = pj


def connected(par, i, j):
    return find(par, i) == find(par, j)



