class Solution:
    def find_distance(self, map: List[List[int]], n: int, cur_node: int, dp: List[int]) -> int:
        if cur_node == n - 1:
            return 0
        if dp[cur_node] != -1:
            return dp[cur_node]

        min_distance = n

        for next_node in map[cur_node]:
            min_distance = min(min_distance, self.find_distance(map, n, next_node, dp) + 1)
            dp[cur_node] = min_distance

        return min_distance

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dp = [-1] * n
        map = [[] for _ in range(n)]
        result = []

        for i in range(n - 1):
            map[i].append(i + 1)

        for x, y in queries:
            map[x].append(y)
            result.append(self.find_distance(map, n, 0, dp))

            dp = [-1] * n

        return result