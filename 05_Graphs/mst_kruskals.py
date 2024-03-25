import sys
sys.path.append('05_Graphs/UnionFind/')

import quick_union
# { vertex1: [(weight, vertex2), (weight, vertex3), ...] ...}
graph = { 
            0: [(1, 1), (2, 2), (2, 3)],
            1: [(1, 2)],
            2: [(1, 3)],
            3: [],
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

# get edges from graph
edges = []
for vertex in range(len(graph)):
    for weight, neighbor in graph[vertex]:
        edges.append((vertex, neighbor, weight))

# Kruskal's Algorithm
uf = quick_union.UnionFind(len(edges)+1)

# sorted edges by weight
edges.sort(key=lambda x: x[2])
cost = 0
for v1, v2, w in edges:
    if uf.union(v1, v2):
        cost += w
print(cost)