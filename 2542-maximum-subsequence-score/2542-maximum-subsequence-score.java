class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] nums = new int[n][2];
        long sum =0;
        PriorityQueue<Integer> que = new PriorityQueue<>();
       
        for (int i = 0; i < n; ++i) {
            nums[i] = new int[] {nums1[i], nums2[i]};
        }
        
        Arrays.sort(nums, (a, b) -> b[1] - a[1]);
        
        for(int i=0;i<k;i++){
            sum+=nums[i][0];
            que.offer(nums[i][0]);
        }
        
        long result = sum*nums[k-1][1];
        
        for(int i=k;i<n;i++){
            int top = que.poll();
            sum-=top;
            sum+=nums[i][0];
            que.offer(nums[i][0]);
            result=Math.max(result,sum*nums[i][1]);
        }
        
        return result;
        
    }
}