class Solution {
    int[] color;
    int[][] adj;
    boolean[] visit;
    int size;
    public boolean isBipartite(int[][] graph) {
        adj = new int[graph.length][graph.length];
        color = new int[graph.length];
        visit = new boolean[graph.length];
        size=graph.length;
        for(int i=0;i<graph.length;i++){
            for(int j=0;j<graph[i].length;j++){
                adj[i][graph[i][j]]=1;
            }
        }
        
        for(int i=0;i<graph.length;i++){
            if(!visit[i]){
                boolean result = bfs(i);
                
                if(!result){
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public boolean bfs(int v){
        Queue<Integer> que = new LinkedList<Integer>();
        color[v]=1;
        visit[v]=true;
        que.offer(v);
        
        while(!que.isEmpty()){
            int cur = que.poll();
            for(int i=0;i<size;i++){
                if(adj[cur][i]==1 && !visit[i]){
                    color[i] = color[cur]*-1;
                    visit[i]=true;
                    que.offer(i);
                }
                else if(adj[cur][i]==1 && visit[i] && color[i]==color[cur]){
                    return false;
                }
            }
            
        }
        return true;
    }
}