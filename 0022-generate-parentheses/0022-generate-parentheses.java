class Solution {
    List<String> answer;
    int n;
    public List<String> generateParenthesis(int _n) {
        n = _n;
        answer = new ArrayList<>();
        dfs(n,0,new StringBuilder());
        
        return answer;
    }
    
    public void dfs(int left,int right,StringBuilder cur){
        if(right==0 && left==0){
            answer.add(cur.toString());
            return;
        }
        if(left>0){
            dfs(left-1,right+1,cur.append('('));
            cur.deleteCharAt(cur.length()-1);
        }
        if(right>0){
            dfs(left,right-1,cur.append(')'));
            cur.deleteCharAt(cur.length()-1);
        }
        
    }
}