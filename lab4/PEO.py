
def check_if_PEO(G, ord):
    RN = [ set() ]* len(G)
    parent = [0]*len(G)
    for v in ord:
          # RN[v] -  zbiór sąsiadów pojawiających się wcześniej niż v
        for el in ord:
            if el == v:
                continue
            if el in G[v].out:
                RN[v].add(el)
                parent[v] = el
    for i in range(1, len(G)):
        print(RN[i])
