from testPackage.readGraph import loadWeightedGraph
from testPackage.DFS import *

G = loadWeightedGraph("res/clique1000")

def smallestWeight(G):
    ans = G[1][1][2]
    for edge in G[1]:
        ans = min(ans, edge[2])
    return ans


def biggestWeight(G):
    ans = 0
    for edge in G[1]:
        ans = max(ans, edge[2])
    return ans

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