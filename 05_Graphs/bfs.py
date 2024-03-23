from typing import List, Dict, Deque
from collections import deque

def bfs(graph: Dict[int, List[int]], start: int) -> None:
    visited: List[bool] = [False] * len(graph)

    # Mark the source node as visited and enqueue it
    queue: Deque[int] = deque([start])
    visited[start] = True

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(str(vertex), end=" ")

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent vertex has not been visited, mark it visited and enqueue it
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

# Example usage:
# The graph is represented as an adjacency list:
# For example, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]} means:
# Vertex 0 is connected to vertices 1 and 2
# Vertex 1 is connected to vertex 2
# Vertex 2 is connected to vertices 0 and 3
# Vertex 3 is connected to itself
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
bfs(graph, 0)  # Starting BFS traversal from vertex 0