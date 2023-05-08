class Solution {
    public int diagonalSum(int[][] mat) {
        int length = mat[0].length;
        int primarySum = 0;
        int secondarySum =0;
        int result = 0;
        
        for(int i=0,j=0;i<length;i++,j++){
            primarySum+=mat[i][j];
        }
        for(int i=length-1,j=0;i>=0;i--,j++){
            secondarySum+=mat[i][j];
        }
        result = primarySum+secondarySum;
        if(length%2!=0){
            int centerIndex = length / 2;
            result -= mat[centerIndex][centerIndex];
        }
        
        return result;
    }
}