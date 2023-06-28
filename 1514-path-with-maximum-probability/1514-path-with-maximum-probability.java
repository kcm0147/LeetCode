class Solution {
    List<List<Edge>> graph = new ArrayList<>();
    double[] costAry;
    double result;
    double minProb;
    
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        costAry = new double[n];
        for(int i=0;i<n;i++){
            graph.add(new ArrayList<>());
        }
        for(int i=0;i<edges.length;i++){
            int one = edges[i][0];
            int other = edges[i][1];
            graph.get(one).add(new Edge(other,succProb[i]));
            graph.get(other).add(new Edge(one,succProb[i]));
            minProb=Math.min(minProb,succProb[i]);
        }
        
        return bfs(start,end);
        
    }
    
    public double bfs(int start,int end){
        Queue<Node> que = new LinkedList<>();
        que.add(new Node(start,1));
        costAry[start]=1;
        while(!que.isEmpty()){
            Node cur = que.poll();
            List<Edge> edges = graph.get(cur.index);
            for(int i=0;i<edges.size();i++){
                int next = edges.get(i).index;
                double nextCost = edges.get(i).cost;
                if(costAry[next]<costAry[cur.index]*nextCost){
                    costAry[next]=costAry[cur.index]*nextCost;
                    que.add(new Node(next,costAry[next]));
                }
            }
        }
        return costAry[end];
    }
}
    


class Edge{
    int index;
    double cost;
    Edge(int index,double cost){
        this.index=index;
        this.cost=cost;
    }
}
    
class Node{
    int index;
    double cost;
    Node(int index,double cost){
        this.index=index;
        this.cost=cost;
    }
}
