
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        cur_sum = 0
        result = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            freq[nums[i]] += 1

            if i >= k:
                cur_sum -= nums[i - k]
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]

            if len(freq) == k:
                result = max(result, cur_sum)

        return result
