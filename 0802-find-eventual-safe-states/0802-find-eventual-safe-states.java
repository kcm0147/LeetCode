class Solution {
    List<List<Integer>> edge = new ArrayList<>();
    int[] isSafeNode;
    
    public List<Integer> eventualSafeNodes(int[][] graph) {
        boolean[] visit;
        List<Integer> result = new ArrayList<>();
        isSafeNode = new int[graph.length];
        Arrays.fill(isSafeNode,-1);
        
        for(int i=0;i<graph.length;i++){
            edge.add(new ArrayList<>());
            for(int j=0;j<graph[i].length;j++){
                edge.get(i).add(graph[i][j]);
            }
        }
        for(int i=0;i<edge.size();i++){
            if(edge.get(i).size()==0){
                isSafeNode[i]=1;
            }
        }
        
        for(int i=0;i<edge.size();i++){
            visit = new boolean[graph.length];
            if(dfs(i,visit)){
                isSafeNode[i]=1;
            }
            else
                isSafeNode[i]=0;
        }
        
        for(int i=0;i<isSafeNode.length;i++){
            if(isSafeNode[i]==1){
                result.add(i);
            }
        }
    
        return result;
    }
    
    public boolean dfs(int node, boolean[] visit){
        visit[node]=true;
        for(int i=0;i<edge.get(node).size();i++){
            int next = edge.get(node).get(i);
            if(isSafeNode[next]==0){
                return false;
            }
            else if(isSafeNode[next]==1)
                continue;
            else if(isSafeNode[next]==-1 && visit[next]){
                return false;
            }
            else if(isSafeNode[next]==-1 && !visit[next]){
                if(!dfs(next,visit)){
                    isSafeNode[next]=0;
                    return false;
                }
                else{
                    isSafeNode[next]=1;
                }
            }
           
        }
        
        
        return true;
    }
        
}