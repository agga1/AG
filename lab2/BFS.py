from lab1.adjListConversion import getAdjList


def BFS(resG, s, t, parent):
    # Mark all the vertices as not visited
    visited = [False] * (len(resG))
    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    # Standard BFS Loop
    while queue:

        # Dequeue a vertex from queue and print it
        u = queue.pop(0)

        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(resG[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

                # If we reached sink in BFS starting from source, then return
    # true, else false
    return True if visited[t] else False