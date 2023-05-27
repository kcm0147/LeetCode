class Solution {
    List<String> result = new ArrayList<>();
    int digitSize;
    String digits;
    String[] digitAry = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    
    public List<String> letterCombinations(String _digits) {
        StringBuilder cur = new StringBuilder();
        digits=_digits;
        digitSize = digits.length();
        if(_digits.length() >= 1)
            dfs(0,cur);
        return result;
    }
    
    public void dfs(int n, StringBuilder cur){
        char digit = digits.charAt(n);
        
        for(int i=0;i<digitAry[digit-'0'].length();i++){
            cur.append(digitAry[digit-'0'].charAt(i));
            
            if(cur.length()==digitSize){
                result.add(cur.toString());
            }
            else{
                dfs(n+1,cur);
            }
            cur.deleteCharAt(cur.length()-1);
            
        }
    }
}