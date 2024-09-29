class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        edge_list = [0 for _ in range(n)]

        for (u, v) in edges:
            graph[u].append(v)
            edge_list[v] += 1

        results = []
        for index, edge_count in enumerate(edge_list):
            if edge_count == 0:
                results.append(index)

        return -1 if len(results) > 1 else results[0]