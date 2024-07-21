class Solution:
    def dfs(self, graph, node, visit, components):
        stack = [node]
        visit.add(node)
        while stack:
            cur = stack.pop()
            components.append(cur)
            for neighbor in graph[cur]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    stack.append(neighbor)


    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        visit = set()
        result = 0
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if node not in visit:
                components = []
                self.dfs(graph, node, visit, components)
                is_complete = True
                for v in components:
                    if len(graph[v]) != len(components) - 1:
                        is_complete = False
                        break

                if is_complete:
                    result += 1

        return result