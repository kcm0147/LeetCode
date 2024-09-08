class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        sum_ary = [0] * len(edges)

        for index, target in enumerate(edges):
            sum_ary[target] += index

        return max(range(len(sum_ary)), key=lambda i: sum_ary[i])