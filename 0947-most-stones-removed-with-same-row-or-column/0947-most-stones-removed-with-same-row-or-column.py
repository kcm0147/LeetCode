class Solution:

    def __init__(self):
        self.result = 0
        self.visit = set()

    def dfs(self, cur, graph):
        self.visit.add(cur)
        count = 1
        for next_node in graph[cur]:
            if next_node not in self.visit:
                count += self.dfs(next_node, graph)

        return count

    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}

        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if i != j:
                    if x1 == x2 or y1 == y2:
                        if (x1, y1) not in graph:
                            graph[(x1, y1)] = []
                        graph[(x1, y1)].append((x2, y2))

        for node in graph:
            if node not in self.visit:
                self.result += (self.dfs(node, graph) - 1)

        return self.result