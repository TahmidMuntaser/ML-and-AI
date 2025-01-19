import heapq

def ucs(graph, start, goal):
   
    queue = [(0, start, [start])]
    visited = set()  

    while queue:
       
        cost, current, path = heapq.heappop(queue)

      
        if current == goal:
            return path, cost

      
        if current in visited:
            continue

        
        visited.add(current)

       
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None, float('inf')  


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}


start = 'A'
goal = 'G'

path, cost = ucs(graph, start, goal)

if path:
    print(f"Path found: {path} with cost {cost}")
else:
    print("No path found!")
