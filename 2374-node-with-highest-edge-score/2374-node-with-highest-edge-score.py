class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = {}
        sum_ary = [0] * len(edges)
        max_value = -1
        max_index = -1

        for index, target in enumerate(edges):
            graph.setdefault(target, []).append(index)
            sum_ary[target] += index
        for index, current_sum in enumerate(sum_ary):
            if max_value < current_sum:
                max_value = current_sum
                max_index = index
        return max_index