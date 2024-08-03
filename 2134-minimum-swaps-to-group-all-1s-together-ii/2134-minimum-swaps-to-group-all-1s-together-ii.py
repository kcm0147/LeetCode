class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size = len(list(filter(lambda x: x == 1, nums)))
        result = 0
        for index in range(0, window_size):
            if nums[index] == 0:
                result += 1
        cur_result = result
        for index in range(1, len(nums)):
            prev = nums[index - 1]
            end = nums[(index + window_size - 1) % len(nums)]
            if prev == 0 and end == 1:
                cur_result -= 1
            elif prev == 1 and end == 0:
                cur_result += 1
            result = min(result, cur_result)
        return result