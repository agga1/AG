class TTNode:

  def __init__(self, idx, parent):
    self.idx = idx            # indeks wierzcholka w kolejnosci DFS (nie jego nazwa w grafie!)
    self.parent = parent      # rodzic wierzcholka (nazwa)
    self.children = set()     # zbior nazw potomkow tego wierzcholka w drzewie DFS
    self.back = set()         # zbior nazw wierzcholkow, do ktorych prowadza krawedzie wsteczne
    self.out = []             # lista wierzchołków docelowych krawedzi wychodzacych w kolejnosci TT-prec
