class Solution {
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp,10001);
        
        dp[0]=0;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<=nums[i];j++){
                int next = (i+j >= nums.length) ? (nums.length-1) : (i+j) ;
                dp[next]=Math.min(dp[next],dp[i]+1);
            }
        }
        
        return dp[nums.length-1];
    }
}