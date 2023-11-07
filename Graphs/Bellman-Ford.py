#used to find shortest path to reach each router in server network
#can be distributed
#can detect negative cycles

def bellman_ford(graph, start):
    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    for _ in range(len(graph) - 1):
        for u in range(len(graph)):
            for v, w in graph[u]:
                dist[v] = min(dist[v], dist[u] + w)
    return dist

