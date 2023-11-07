#used to compute distances between nodes in a graph
#works with edges with negative costs
#slowest of the three

def dist(graph, start, end):
    if end in graph[start]:
        return float(graph[start][end])
    elif start == end:
        return 0.0
    else:
        return float('inf')

def floyd_warshall(graph):
    mat = {row: {col: dist(graph, row, col) for col in graph} for row in graph}
    for k in mat:
        for i in mat:
            for j in mat:
                if mat[i][j] > mat[i][k] > mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
    return mat

