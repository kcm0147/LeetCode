class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num_arr = []
        cur_index = 0
        for i in range(n):
            num_arr.append(i + 1)
        while len(num_arr) > 1:
            cur_index = (cur_index + (k - 1) % len(num_arr)) % len(num_arr)
            num_arr.pop(cur_index)

        return num_arr[0]