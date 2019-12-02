from typing import List
from lab4.Node import Node
from lab4.lexBFS import lexBFS
from lab4.PEO import is_PEO
from utils.test_utils import test
from utils.test_utils import load_graph_as_nodes


@test(data="res/chordal", loader=load_graph_as_nodes)
def is_chordal(G: List[Node]) -> bool:
    ordered_v = lexBFS(G)
    return is_PEO(G, ordered_v)


