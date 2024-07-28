from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        result_arr = list()
        child = [0 for _ in range(numCourses)]
        visited = set()
        que = deque([])

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            child[prerequisite[0]] += 1

        for index, child_cnt in enumerate(child):
            if child_cnt == 0:
                que.append(index)
                visited.add(index)
        while que:
            node = que.pop()
            result_arr.append(node)
            
            for neighbor in graph[node]:
                child[neighbor]-=1
                if neighbor not in visited and child[neighbor] == 0:
                    visited.add(neighbor)
                    que.append(neighbor)

        return result_arr if len(visited) == numCourses else []
