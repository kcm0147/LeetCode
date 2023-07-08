class Solution {
    public int longestSubarray(int[] nums) {
        
        int cur = 0;
        int prev = 0;
        int maxResult = 0;

        
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                cur++;
            }
            if(nums[i]==0 || i==nums.length-1){
                prev+=cur;
                maxResult = Math.max(maxResult,prev);
                prev = cur;
                maxResult = Math.max(maxResult,cur);
                cur=0;
            }   
        }
       
        
        return maxResult == nums.length ? maxResult-1 : maxResult;
    }
}