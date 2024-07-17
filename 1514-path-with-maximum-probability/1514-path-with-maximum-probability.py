import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        graph = {i: {} for i in range(n)}
        distance = [-1.0 for _ in range(n)]
        distance[start_node] = 1.0
        priority_que = [(-1.0, start_node)]

        for index, (u, v) in enumerate(edges):
            graph[u][v] = succProb[index]
            graph[v][u] = succProb[index]

        while priority_que:
            current_distance, current_node = heapq.heappop(priority_que)
            current_distance = -current_distance

            if current_distance < distance[current_node]:
                continue

            for neighbor, weight in graph[current_node].items():
                new_prob = current_distance * weight
                if distance[neighbor] < new_prob:
                    distance[neighbor] = new_prob
                    heapq.heappush(priority_que,(-new_prob, neighbor))

        return 0 if (distance[end_node] == float(-1)) else distance[end_node]
