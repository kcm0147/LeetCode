class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        is_consecutive = all(nums[i+1] == nums[i]+1 for i in range(k-1))
        result.append(nums[k - 1] if is_consecutive else -1)

        for i in range(1, n - k + 1):
            if is_consecutive and nums[i + k - 1] - nums[i + k - 2] == 1:
                result.append(nums[i + k - 1])
            else:
                is_consecutive = all(nums[i + j + 1] - nums[i + j] == 1 for j in range(k - 1))
                result.append(nums[i + k - 1] if is_consecutive else -1)
            
                
        return result
        