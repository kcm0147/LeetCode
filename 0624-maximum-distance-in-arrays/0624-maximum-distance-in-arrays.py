class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_heap = []
        min_heap = []

        for (index, array) in enumerate(arrays):
            max_num = array[-1]
            min_num = array[0]
            heapq.heappush(max_heap, (-max_num, index))
            heapq.heappush(min_heap, (min_num, index))

        max_num, max_index = heapq.heappop(max_heap)
        min_num, min_index = heapq.heappop(min_heap)

        if max_index == min_index:
            n_max_num, n_max_index = heapq.heappop(max_heap)
            n_min_num, n_min_index = heapq.heappop(min_heap)
            result = max((-n_max_num - min_num), (-max_num - n_min_num))
        else:
            result = -max_num - min_num

        return result