class Solution:
    def is_distribute(self, quantities: List[int], k: int, n: int) -> bool:
        j = 0
        remain = quantities[j]

        for i in range(n):
            if remain <= k:
                j += 1
                if j == len(quantities):
                    return True
                remain = quantities[j]
            else:
                remain -= k

        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 0
        right = max(quantities)

        while left < right:
            middle = (left + right) // 2
            if self.is_distribute(quantities,middle,n):
                right = middle
            else:
                left = middle+1

        return left