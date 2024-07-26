import sys
import heapq


class Solution:

    def bfs(self, start, graph, distance, threshold):
        distance[start] = 0
        que = [(distance[start], start)]
        visit = set()
        while que:
            cur_distance, node = heapq.heappop(que)
            if node in visit:
                continue

            visit.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visit and cur_distance + weight <= threshold:
                    distance[neighbor] = cur_distance + weight
                    heapq.heappush(que, (distance[neighbor], neighbor))

        return len(visit) - 1

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = [[] for _ in range(n)]
        result = [0 for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))

        for i in range(n):
            distance = [sys.maxsize for _ in range(n)]
            result[i] = self.bfs(i, graph, distance, distanceThreshold)
            
        min_value = sys.maxsize
        max_index = -1
        for index, value in enumerate(result):
            if value < min_value:
                min_value = value
                max_index = index
            elif value == min_value:
                max_index = max(max_index, index)
        return max_index