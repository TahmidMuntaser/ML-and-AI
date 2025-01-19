from collections import deque

def bfs(graph, start, goal):
    if start == goal: 
        return [start]
   
    queue = deque([start])
   
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        

        for neighbor in graph[current]:
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    
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
goal = 'G'


path = bfs(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found!")