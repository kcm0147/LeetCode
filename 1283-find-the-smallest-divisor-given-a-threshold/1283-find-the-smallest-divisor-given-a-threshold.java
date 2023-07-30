class Solution {
    int[] nums;
    int threshold;
    public int smallestDivisor(int[] _nums, int _threshold) {
        nums = _nums;
        Arrays.sort(nums);
        int maxValue = Arrays.stream(nums).max().getAsInt();
        threshold = _threshold;
        
        return binarySearch(0,maxValue);
    }
    
    public int binarySearch(int start,int end){
        int result = end;
        while(start<=end){
            int mid = (start+end)/2;
            int temp = 0;
            for(int i=0;i<nums.length;i++){
                double num = nums[i];
                temp+=Math.ceil(num/mid);
                if(temp>threshold){
                    start=mid+1;
                    break;
                }
            }
            if(temp<=threshold){
                result=Math.min(result,mid);
                end = mid-1;
            }
            
        }
        
        return result;
    }
}