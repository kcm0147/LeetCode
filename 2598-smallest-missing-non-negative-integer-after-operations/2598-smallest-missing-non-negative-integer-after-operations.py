class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = {}
        for num in nums:
            remainder = num % value
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        mex = 0

        while True:
            remainder = mex % value

            if remainder_count.get(remainder, 0) == 0:
                break

            remainder_count[remainder] -= 1
            mex += 1


        return mex