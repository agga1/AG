
class Node:
  def __init__(self):
    self.edges = {}    # słownik par mapujący wierzchołki do których są krawędzie na ich wagi

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę

  def delEdge( self, to ):
    del self.edges[to]                              # usuń krawędź do zadanego wierzchołka


G = [ Node() for i in range(V) ]

for (x,y,c) in L:
  G[x].addEdge(y,c)
  G[y].addEdge(x,c)
 