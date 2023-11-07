def dfs(graph, start):
    stack = [start]
    parents = {start:start}
    while stack:
        vertex = stack.pop(-1)
        for candidate in graph[vertex]:
            if candidate not in parents:
                stack.append(candidate)
                parents[candidate] = vertex
    return parents