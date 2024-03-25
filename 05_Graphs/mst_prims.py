import heapq

# { vertex1: [(weight, vertex2), (weight, vertex3), ...] ...}
graph = { 
            1: [(1, 2), (1, 0)],
            2: [(1, 1), (1, 3), (2, 0)],
            3: [(1, 2), (2, 0)],
            0: [(1, 1), (2, 2), (2, 3)]
        }

# Graph
# 1 -------- 2 --------- 3
#  \         |          /
#   \        |         /
#    \______ 0 _______/

# MST
# 1 -------- 2 --------- 3
#  \       
#   \______ 0

visited = set()
heap = [(0, 0)]

cost = 0
while heap:
    weight, vertex = heapq.heappop(heap)
    if vertex not in visited:
        visited.add(vertex)
        cost += weight
        for w, neighbor in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(heap, (w, neighbor))
print(cost)