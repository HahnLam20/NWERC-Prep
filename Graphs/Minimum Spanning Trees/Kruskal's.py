#Picks shortest edges from global pool containing all edges
#O(ElogE) time
#O(E) space
#1. Put all edges into heap and sort so shortest edges are on top
#2. Create set of trees where each only contains one vertex (disjoint set)
#3. Repeat these operations until solution doesn't contain as many edges as number of vertices in graph
#   a. Choose shortest edge from heap
#   b. Determine whether two vertices connected by edge appear in different trees from sets of connected trees
#   c. When trees differ, connect trees using edge
#   d. When vertices appear in same tree, discard efge
#   e. Repeat steps for remaining edges
from gettext import find
from retworkx import union


def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    edges.sort()
    parents = {vertex: vertex for vertex in graph}
    mst = []
    for weight, u, v in edges:
        if find(u, parents) != find(v, parents):
            union(u, v, parents)
            mst.append((u, v, weight))
    return mst