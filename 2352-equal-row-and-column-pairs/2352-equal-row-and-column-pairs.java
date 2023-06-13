class Solution {
    public int equalPairs(int[][] grid) {
        
           int result = 0;
        int n = grid[0].length;
        for(int row=0;row<n;row++){
            
            for(int col=0;col<n;col++){
            
                for(int index=0;index<n;index++){
                    if(grid[row][index]!=grid[index][col]){
                        break;
                    }
                    if(index==n-1){
                        result++;
                    }
                }
            }
        }
    return result;
    }
}