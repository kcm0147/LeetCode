class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        undetected = 0
        guard = 1
        wall = 2
        detected = 3
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        result = m * n - (len(guards) + len(walls))

        map = [[0] * n for _ in range(m)]
        for x, y in guards:
            map[x][y] = guard
        for x, y in walls:
            map[x][y] = wall

        for x, y in guards:
            for nx, ny in dir:
                cur_x = x + nx
                cur_y = y + ny
                while self.isDetect(cur_x, cur_y, m, n, map):
                    if map[cur_x][cur_y] is undetected:
                        map[cur_x][cur_y] = detected
                        result -= 1
                    cur_x += nx
                    cur_y += ny

        return result

    def isDetect(self, x: int, y: int, m: int, n: int, map: List[List[int]]) -> bool:
        if 0 <= x < m and 0 <= y < n and map[x][y] != 1 and map[x][y] != 2:
            return True
        return False