import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> List[int]:
    distances: List[int] = [float('inf')] * len(graph)
    distances[start] = 0
    priority_queue: List[Tuple[int, int]] = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage with the weighted graph:
graph = {
    0: [(1, 2), (2, 4)],
    1: [(2, 3)],
    2: [(0, 4), (3, 2)],
    3: [(3, 0)]
}
start_vertex = 0
distances = dijkstra(graph, start_vertex)
print(f"Distances from vertex {start_vertex}: {distances}")
