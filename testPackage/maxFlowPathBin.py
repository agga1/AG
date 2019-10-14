from testPackage.readGraph import loadWeightedGraph
from testPackage.DFS import *

G = loadWeightedGraph("res/clique5")

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

# TODO fix!
def maxFlowPathBin(G, s, t):
    mini = smallestWeight(G)
    maxi = biggestWeight(G)
    mid = mini+(maxi-mini)//2
    while True:
        print(mid)
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

print(maxFlowPathBin(G, 1, 2))

