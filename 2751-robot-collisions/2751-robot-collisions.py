from collections import deque


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robot_list = list(range(n))
        stack = deque()
        robot_list.sort(key=lambda x: positions[x])
        for i in robot_list:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top_index = stack.pop()

                    if healths[top_index] > healths[i]:
                        healths[top_index] -= 1
                        healths[i] = -1
                        stack.append(top_index)
                    elif healths[top_index] < healths[i]:
                        healths[i] -= 1
                        healths[top_index] = -1
                    else:
                        healths[i] = -1
                        healths[top_index] = -1
        return [healths[i] for i in range(n) if healths[i] != -1]
