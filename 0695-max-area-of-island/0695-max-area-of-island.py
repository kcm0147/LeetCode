class Solution:
    def __init__(self):
        self.grid = []
        self.visited = []

    def isIsland(self, x: int, y: int, mx: int, my: int) -> bool:
        if 0 <= x < mx and 0 <= y < my and self.visited[x][y] == False and self.grid[x][y] == 1:
            return True
        return False

    def bfs(self, x: int, y: int) -> int:
        que = deque()
        que.append((x, y))
        self.visited[x][y] = True
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cur_result = 0
        while que:
            x, y = que.popleft()
            cur_result += 1
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if self.isIsland(nx, ny, len(self.grid), len(self.grid[0])):
                    self.visited[nx][ny] = True
                    que.append((nx, ny))

        return cur_result


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        result = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1 and self.visited[x][y] == False:
                    result = max(result, self.bfs(x, y))

        return result