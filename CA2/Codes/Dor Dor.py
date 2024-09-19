from collections import defaultdict, deque

def find_shortest_cycle(graph, n):
   shortest_cycle = float('inf')
   shortest_cycle_path = []
   
   for start_node in range(n):
      visited = [False] * n
      distance = [-1] * n
      parent = [-1] * n
      queue = deque([start_node])
      visited[start_node] = True
      distance[start_node] = 0
      
      while queue:
         current_node = queue.popleft()
         
         for neighbor in graph[current_node]:
               if not visited[neighbor]:
                  visited[neighbor] = True
                  distance[neighbor] = distance[current_node] + 1
                  parent[neighbor] = current_node
                  queue.append(neighbor)
               elif parent[current_node] != neighbor and distance[current_node] + distance[neighbor] + 1 < shortest_cycle:
                  shortest_cycle = distance[current_node] + distance[neighbor] + 1
                  shortest_cycle_path = get_cycle_path(parent, current_node, neighbor)
   
   return shortest_cycle_path

def get_cycle_path(parent, u, v):
   cycle_path = []

   while v != -1:
      cycle_path.append(v)
      v = parent[v]
   cycle_path.reverse()
   
   while u != -1:
      cycle_path.append(u)
      u = parent[u]
      
      

   
   return cycle_path

n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
   u, v = map(int, input().split())
   graph[u].append(v)
   graph[v].append(u)

shortest_cycle_path = find_shortest_cycle(graph, n)

print(len(shortest_cycle_path)-1)
print(*shortest_cycle_path)
