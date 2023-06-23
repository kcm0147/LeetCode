class Solution {
    fun longestArithSeqLength(nums: IntArray): Int {
        val dp = Array<HashMap<Int, Int>>(nums.size) { hashMapOf() }
        var result = 0

        for (i in 1 until nums.size) {
            for (j in 0 until i) {
                val different = nums[i] - nums[j]
                dp[i][different] = (dp[j][different] ?: 1) + 1
                result = result.coerceAtLeast(dp[i][different]!!)
            }
        }

        return result
    }
}