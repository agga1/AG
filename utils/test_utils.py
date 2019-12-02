import os
import re
import sys
from timeit import timeit
from utils.create_graph import create_graph
from typing import List, Tuple
from lab4.Node import Node


def test(data=None, loader=None, times=10):
    files = os.listdir(data)
    pairs = ((file, os.path.getsize(f"{data}/{file}")) for file in files)
    padd = max(map(len, files))

    def wrap(function):
        result = dict()
        for file, _ in sorted(pairs, key=lambda x: x[1]):
            solution, args = loader(f"{data}/{file}")
            res = []
            def run():
                res.append(function(*args))
            sys.stdout.write(file.rjust(padd))
            time = timeit(run, number=times)
            result[file] = { "time": time, "passed": res[0] == solution }
            passed = '✔' if res[0] == solution else '❌'
            time = str(round(time / times, 5)).rjust(10)
            print(f" {passed} ⌚ {time}")
            if res[0] != solution:
                print('solution:', solution, 'result:', res[0])
        return result
    return wrap


def load_graph_as_nodes(file: str) -> Tuple[int, List[List[Node]]]:
    solution = None
    with open(file, 'r') as f:
        line = f.readline()
        ss = line.split()
        assert (len(ss) > 1), "graph file incorrect"
        if ss[0] == 'c':
            solution = int(re.match(r"c.*solution.*?(\d+)", line).group(1))
        else:
            raise Exception("cant find solution")
    return solution, [create_graph(file)]
