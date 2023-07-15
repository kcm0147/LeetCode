class Solution {
    public int minElements(int[] nums, int limit, int goal) {
        long sum = 0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        long diff = goal-sum;
        int result =  (int)(Math.abs(diff) / limit);
        int remain = (int)(Math.abs(diff) % limit);
        return remain == 0 ? result : result+1;
    }
}