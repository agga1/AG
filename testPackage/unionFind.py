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


par = [x for x in range(0, 10)]
print(par)
conns = [(0, 1), (2, 3)]
for e in conns:
    union(par, e[0], e[1])


