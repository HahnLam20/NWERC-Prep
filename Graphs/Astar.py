from math import inf, sqrt
from heapq import heappop, heappush

#Manhattan heuristic
def heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance

#Euclidean heuristic
def euclidean(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return sqrt(x_distance * x_distance + y_distance * y_distance)

def astar(graph, start, target):
    count = 0
    paths_and_distances = {}
    for vertex in graph:
        paths_and_distances[vertex] = [inf, [start.name]]

    paths_and_distances[start][0] = 0
    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbor, target)
            if new_distance < paths_and_distances[neighbor][0]:
                paths_and_distances[neighbor][0] = new_distance
                paths_and_distances[neighbor][1] = paths_and_distances[current_vertex][1] + [neighbor.name]
                heappush(vertices_to_explore, (new_distance, neighbor))
                count += 1

    return paths_and_distances[target][1], count

