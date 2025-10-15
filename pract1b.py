#A program to implement Breadth First Search 

#Python Code:
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

def bfs (start):
    queue = [start]
    levels = {}
    levels[start] = 0
    visited = set([start])
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour] = levels[node] + 1
    
    print (levels)
    return visited

print (bfs('A'))

def bfs_paths (graph, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

result = list(bfs_paths(graph, 'A', 'F'))
print (result)

def shortest_path (graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

result1 = shortest_path(graph, 'A', 'F')
print (result1)