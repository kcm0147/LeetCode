from collections import deque
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        restricted_set = set(restricted)
        visit = set()
        que = deque([0])
        visit.add(0)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        while que:
            node = que.pop()

            for neighbor in graph[node]:
                if neighbor not in visit and neighbor not in restricted_set:
                    visit.add(neighbor)
                    que.append(neighbor)
                    
        return len(visit)
