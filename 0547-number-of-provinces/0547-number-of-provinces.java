class Solution {    
    boolean[] visit;
    int n;
    int result=0;
    public int findCircleNum(int[][] isConnected) {
        n = isConnected.length;
        visit = new boolean[isConnected.length];
        for(int i=0;i<n;i++){
            if(!visit[i]){
                bfs(i,isConnected);
            }
        }
        
        return result;
    }

    public void bfs(int index,int[][] isConnected){
        result++;
        Queue<Integer> que = new LinkedList<>();
        visit[index]=true;
        que.add(index);
        
        while(!que.isEmpty()){
            int cur = que.poll();
            
            for(int i=0;i<n;i++){
                if(isConnected[cur][i]==1 && i!=cur && !visit[i]){
                    visit[i]=true;
                    que.add(i);
                }
            }
        }
    }
}