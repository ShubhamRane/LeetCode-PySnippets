from collections import deque
from typing import *
from math import *

def bellmanFord(V: int, edges: List[List[int]], src: int, dst: int) -> int:
    distances = [inf for x in range(V)]
    parent = [None for x in range(V)]
    parent[src] = src
    distances[src] = 0
    
    for _ in range(V-1):
        prev = distances.copy()
        # for each edge
        for frm, to, weight in edges:
            if distances[to] > prev[frm] + weight:
                parent[to] = frm
            distances[to] = min(distances[to], prev[frm] + weight)
    
    if distances[dst] != inf:
        path = deque()
        cur = dst
        while cur != src:
            path.appendleft(cur)
            cur = parent[cur]
        path.appendleft(src)

        return path, distances[dst]
    return [], -1

V = 6 # number of vertices in graph named 0 to V-1
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

source, destination = 0, 4
print(bellmanFord(V, edges, source, destination))