class Solution {
    public int longestSubarray(int[] nums) {
        
        int cur = 0;
        int prev = 0;
        int maxResult = 0;
        boolean existZero = false;
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                cur++;
            }
            
            if(nums[i]== 0){
                prev+=cur;
                maxResult = Math.max(maxResult,prev);
                prev = cur;
                maxResult = Math.max(maxResult,cur);
                cur=0;
                existZero = true;
            }
            else if(i == nums.length-1){
                prev+=cur;
                maxResult = Math.max(maxResult,prev);
                prev = cur;
                maxResult = Math.max(maxResult,cur);
                cur=0;
            }
            
        }
        if(!existZero){
            maxResult-=1;
        }
        
        return maxResult;
    }
}