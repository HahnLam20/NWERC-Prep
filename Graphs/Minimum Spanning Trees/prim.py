#Used to convert graph into MST
#1. Track both edges of MST and used verices
#2. Start from any vertex and place into solution
#3. Determine whether there are vertices that aren't part of solution:
#   a. Enumerate edges that touch vertices in solution
#   b. Insert edge with minimum weight into spanning tree

from heapq import heappop, heappush
def prim(graph, start):
    visited = {start}
    mst = []
    edges = []
    for edge in graph[start]:
        heappush(edges, edge)
    while edges:
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for edge in graph[v]:
                heappush(edges, edge)
    return mst