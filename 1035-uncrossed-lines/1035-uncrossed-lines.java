class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int result = 0;
        
		int dpTable[][] = new int[nums1.length+1][nums2.length+1];
		
		for(int i=0;i<=nums1.length;i++)
			dpTable[i][0] = 0;
		
		for(int i=0;i<=nums2.length;i++)
			dpTable[0][i] = 0;
		
		for(int i=1;i<=nums1.length;i++) {
			for(int j=1;j<=nums2.length;j++) {
				
				if(nums1[i-1]==nums2[j-1]) {
					dpTable[i][j]=dpTable[i-1][j-1]+1;
				}else
					dpTable[i][j] = Math.max(dpTable[i-1][j], dpTable[i][j-1]);
			}
		}
        
        return dpTable[nums1.length][nums2.length];
    }
}