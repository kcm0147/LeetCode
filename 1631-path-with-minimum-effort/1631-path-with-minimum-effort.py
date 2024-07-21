import heapq
import sys
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        distance_ary = [[sys.maxsize for _ in range(len(heights[0]))]
                        for _ in range(len(heights))]
        n = len(heights) * len(heights[0])
        cur = (0, 0)
        distance_ary[cur[0]][cur[1]] = 0
        heap = []
        heapq.heappush(heap, (distance_ary[cur[0]][cur[1]], cur, heights[cur[0]][cur[1]]))

        move_ary = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while heap:
            max_distance, cur_position, cur_height = heapq.heappop(heap)
            
            for move in move_ary:
                new_x = cur_position[0] + move[0]
                new_y = cur_position[1] + move[1]

                if 0 <= new_x < len(distance_ary) and 0 <= new_y < len(distance_ary[0]):
                    diff = abs(cur_height - heights[new_x][new_y])
                    new_distance = max(diff,max_distance)
                    
                    if new_distance < distance_ary[new_x][new_y]:
                        distance_ary[new_x][new_y] = new_distance
                        heapq.heappush(heap, (distance_ary[new_x][new_y], (new_x, new_y), heights[new_x][new_y]))

        return distance_ary[len(heights) - 1][len(heights[0]) - 1]
