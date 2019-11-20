import os
from lab4.node import Node
from lab4.create_graph import create_graph
from lab4.PEO import check_if_PEO
from lab4.lexBFS2 import lexBFS

graphs = []
for name in os.listdir("res/chordal"):
    graphs.append(f"res/chordal/{name}")


def checkLexBFS(G, vs):
  n = len(G)
  pi = [None] * n
  for i, v in enumerate(vs):
    pi[v] = i

  for i in range(n-1):
    for j in range(i+1, n-1):
      Ni = G[vs[i]].out
      Nj = G[vs[j]].out

      verts = [pi[v] for v in Nj - Ni if pi[v] < i]
      if verts:
        viable = [pi[v] for v in Ni - Nj]
        if not viable or min(verts) <= min(viable):
          return False
  return True


for graph in graphs:
    G = create_graph(graph)
    vs = lexBFS(G)
    graph = graph.split("/")[-1]
    print( checkLexBFS(G, vs), graph)
    check_if_PEO(G, vs)
