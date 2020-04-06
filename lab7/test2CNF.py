from lab7.check2CNF import *
from typing import Dict, List
import os, re


def getExpression(name):
    (V, F) = loadCNFFormula(name)
    return F


def checkProposedEval(anyEval: Dict[int, bool], expr: List[List[int]]) -> bool:
    for pear in expr:
        if not (anyEval[pear[0]] or anyEval[pear[1]]):
            print("formula is incorrect!")
            return False
    return True


dirName = "graphs/sat"

for fileName in os.listdir(dirName):
    name = f"{dirName}/{fileName}"
    anyEval = any2CNF(name)
    if anyEval is not None:
        print(checkProposedEval(anyEval, getExpression(name)))
    else:
        with open(name, 'r') as f:
            line = f.readline()
            ss = line.split()
            assert (len(ss) > 1), "graph file incorrect"
            if ss[0] == 'c':
                expected = int(re.match(r"c.*solution.*?(\d+)", line).group(1))
            else:
                raise Exception("cant find solution")
        print(expected == 0)

