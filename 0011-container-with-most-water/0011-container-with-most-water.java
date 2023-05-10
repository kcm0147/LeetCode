class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length -1;
        int width = 0;
        int result = 0;
        while(left<right){
            width = right - left;
            int y = Math.min(height[left],height[right]);
            result = Math.max(result,width*y);
            if(height[left]<=height[right]){
                left++;
            }
            else
                right--;
        }
        
        return result;
    }
}