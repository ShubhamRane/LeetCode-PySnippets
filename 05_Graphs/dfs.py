from typing import List, Dict

def dfs(graph: Dict[int, List[int]], vertex: int, visited: List[bool]) -> None:
    visited[vertex] = True
    print(str(vertex) + " ", end="")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)

# Example usage:
# The graph is represented as an adjacency list:
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
visited = [False] * len(graph)
dfs(graph, 0, visited)  # Starting DFS traversal from vertex 0