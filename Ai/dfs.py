def dfs(graph, start, goal, visited=None, path=None):
   
    if visited is None:
        visited = set()
    if path is None:
        path = []


    visited.add(start)
    path.append(start)

    if start == goal:
        return path


    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result: 
                return result


    path.pop()
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


start = 'A'
goal = 'F'


path = dfs(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found!")
