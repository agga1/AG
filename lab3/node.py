from lab3.dimacs import *

class Node:
  def __init__(self):
    self.edges = {}    # słownik par mapujący wierzchołki do których są krawędzie na ich wagi
    self.active = True

  def addEdge( self, to, weight):
    self.edges[to] = self.edges.get(to,0) + weight  # dodaj krawędź do zadanego wierzchołka
                                                    # o zadanej wadze; a jeśli taka krawędź
                                                    # istnieje, to dodaj do niej wagę

  def delEdge( self, to ):
    del self.edges[to]                              # usuń krawędź do zadanego wierzchołka



(V, L) = loadWeightedGraph( "res/clique5" )        # wczytaj graf
G = [ Node() for i in range(V+1) ]

for (x,y,c) in L:
  G[x].addEdge(y,c)
  G[y].addEdge(x,c)
 