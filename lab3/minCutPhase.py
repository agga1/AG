from lab3.dimacs import *

(V, L) = loadWeightedGraph( "g1" )        # wczytaj graf
for (x, y, c) in L:                        # przeglądaj krawędzie z listy
  print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj
