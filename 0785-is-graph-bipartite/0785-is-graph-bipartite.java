class Solution {
    int[] color;
    boolean[] visit;
    int size;
    public boolean isBipartite(int[][] graph) {
        color = new int[graph.length];
        visit = new boolean[graph.length];
        size=graph.length;

        
        for(int i=0;i<graph.length;i++){
            if(!visit[i]){
                boolean result = bfs(graph,i);
                
                if(!result){
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public boolean bfs(int[][] graph,int v){
        Queue<Integer> que = new LinkedList<Integer>();
        color[v]=1;
        visit[v]=true;
        que.offer(v);
        
        while(!que.isEmpty()){
            int cur = que.poll();
            for(int i=0;i<graph[cur].length;i++){
                int next = graph[cur][i];
                if(!visit[next]){
                    color[next] = color[cur]*-1;
                    visit[next]=true;
                    que.offer(next);
                }
                else if(visit[next] && color[next]==color[cur]){
                    return false;
                }
            }
            
        }
        return true;
    }
}