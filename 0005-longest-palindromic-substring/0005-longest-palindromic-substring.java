class Solution {
    public String longestPalindrome(String s) {
        boolean[][] dp = new boolean[s.length()+1][s.length()+1];
        int left =0;
        int right=0;
        
        for(int i=0;i<s.length();i++){
            char second = s.charAt(i);
            for(int j=0;j<i;j++){
                char first = s.charAt(j);
                
                dp[j][i] = (first == second) && ((i-j <=2) || dp[j+1][i-1]); 
                    
                if(dp[j][i]){
                    if(i-j > right-left){
                        left = j;
                        right = i;
                    }
                }
                
            }
        }
        
        return s.substring(left,right+1);
    }
}