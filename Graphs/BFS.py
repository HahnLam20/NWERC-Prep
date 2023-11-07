def bfs(graph, start):
    queue = [start]
    queued = [start]
    while queue:
        vertex = queue.pop(0)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queue.append(candidate)
                queued.append(candidate)
    return queued

