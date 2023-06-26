class Solution {
    public int[] getAverages(int[] nums, int k) {
        System.out.println(nums.length);
        System.out.println(k);
        int[] result = new int[nums.length];
        long[] prefixSum = new long[nums.length];
        prefixSum[0]=nums[0];
        for(int i=1;i<nums.length;i++){
            prefixSum[i]=prefixSum[i-1]+nums[i];
        }
        
        for(int i=0;i<nums.length;i++){
            if(i-k<0 || i+k>nums.length-1){
                result[i]=-1;
            }
            else{
                long sum = prefixSum[i+k];
                if(i-k-1>=0){
                    sum-=prefixSum[i-k-1];
                }
                result[i]=(int)(sum/(k*2+1));
            }
        }
        return result;
        
    }
}