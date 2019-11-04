
def BFS(resG, s, t, parent, nrOfV):  # resG repr as dictionary of dict
    # Mark all the vertices as not visited
    visited = [False] * (nrOfV+1)
    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for keyV, weight in resG[u].items():  # resG[u] - dict { "vertexNo": weight, ...}
            if (not visited[keyV]) and weight > 0:
                queue.append(keyV)
                visited[keyV] = True
                parent[keyV] = u

    return True if visited[t] else False
