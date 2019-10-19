from readGraph import loadWeightedGraph
from DFS import *

#G = loadWeightedGraph("res/clique1000")

def smallestWeight(G):
    ans = min(G[1], key=lambda p: p[2])
    return ans[2]


def biggestWeight(G):
    ans = max(G[1], key=lambda p: p[2])
    return ans[2]

def maxFlowPathBin(G, s, t):
    mini = smallestWeight(G)
    maxi = biggestWeight(G)
    mid = (maxi+mini)//2
    while (maxi-mini) > 1:
        if dfsWrap(G, s, t, mid):
            mini = mid
        else:
            maxi = mid
        mid = (maxi+mini)//2
    if dfsWrap(G, s, t, mini+1):
        return mini + 1
    else:
        return mini


#print(maxFlowPathBin(G, 1, 2))

"""
        if not dfsWrap(G, s, t, mid):
            print(mid, " is too high")
            maxi = mid - 1
            mid = mini+(maxi-mini)//2
            if maxi<mid:
                return -1
        else:
            if not dfsWrap(G, s, t, mid+1):
                print("cant go up")
                return mid
            mini = mid + 1
            mid = mini + (maxi - mini) // 2
"""