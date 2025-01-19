import heapq

def a_star(graph, heuristics, start, goal):
    if start == goal: 
        return [start]
    
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    
    g_score = {}
    for node in graph:
        g_score[node] = float('inf')
    g_score[start] = 0
    
    f_score = {}
    for node in graph:
        f_score[node] = float('inf')
    f_score[start] = heuristics[start]
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristics[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None
    


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 5,
    'G': 0  
}

start = 'A'
goal = 'G'

path = a_star(graph,heuristics, start, goal)

if path: 
    print('Shortest Path: ', path)
else:
    print('path not found!')