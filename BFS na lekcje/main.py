def bfs_dict(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while len(queue) != 0:
        current = queue.pop(0)
        for elem in graph[current]:
            if elem not in visited:
                visited.append(elem)
                queue.append(elem)
    return visited


def bfs_list(edges, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while len(queue) != 0:
        current = queue.pop(0)
        for u, v in edges:
            if u == current and v not in visited:
                visited.append(v)
                queue.append(v)
            elif v == current and u not in visited:
                visited.append(u)
                queue.append(u)
    return visited


def bfs_matrix(verticies, matrix, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while len(queue) != 0:
        current = queue.pop(0)
        index = verticies.index(current)
        i = 0
        for state in matrix[index]:
            if state == 1 and verticies[i] not in visited:
                visited.append(verticies[i])
                queue.append(verticies[i])
            i += 1
    return visited


G = {
  'A' : ['B', 'C'],
  'B' : ['A', 'D', 'E'],
  'C' : ['A', 'F'],
  'D' : ['B'],
  'E' : ['B', 'F'],
  'F' : ['C', 'E']
}
V = ['A', 'B', 'C', 'D', 'E', 'F']
E = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
M = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]


print(bfs_dict(G, 'A'))
print(bfs_list(E, 'A'))
print(bfs_matrix(V, M, 'A'))
