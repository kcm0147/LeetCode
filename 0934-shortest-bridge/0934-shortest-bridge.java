class Solution {
        int[][] map;
        boolean[][][] visit;
        int n,result;
        int[][] dir = {{0,1},{-1,0},{1,0},{0,-1}};
    public int shortestBridge(int[][] grid) {
        map = new int[grid[0].length][grid[0].length];
        visit = new boolean[grid[0].length][grid[0].length][10000];
        n = grid[0].length;
        int num = 0;
        result=Integer.MAX_VALUE;
        Node start = null;
    
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1 && !visit[i][j][0]){
                    if(start == null){
                        start=new Node(i,j,0);
                    }
                    convertMap(i,j,++num,grid);
                }
            }
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print(map[i][j]+ "");
            }
            System.out.println();
        }
        
        visit = new boolean[grid[0].length][grid[0].length][10000];
            
        bfs(start.x,start.y,map[start.x][start.y]);
        
        return result;
        
    }
    
    public void bfs(int x,int y,int initNum){
        
        Queue<Node> que = new LinkedList<>();
        que.offer(new Node(x,y,0));
        visit[x][y][0]=true;
    
    
        while(!que.isEmpty()){
            Node cur = que.poll();
            if(cur.value >= result) continue;
            // System.out.println(cur.value+" "+result);
            for(int i=0;i<4;i++){
                int nx= cur.x+dir[i][0];
                int ny= cur.y+dir[i][1];

                if(nx >=0 && ny>=0 && nx < n && ny <n){
                    
                    if(map[nx][ny]!=0 && map[nx][ny]!=initNum && !visit[nx][ny][cur.value]){
                        visit[nx][ny][cur.value]=true;
                        result=Math.min(result,cur.value);
                        
                    }
                    else if(map[nx][ny]==initNum && !visit[nx][ny][cur.value]){
                        visit[nx][ny][cur.value]=true;
                        que.offer(new Node(nx,ny,cur.value));
                    }
                    else if(map[nx][ny]==0 && !visit[nx][ny][cur.value+1]){
                        visit[nx][ny][cur.value+1]=true;
                        que.offer(new Node(nx,ny,cur.value+1));
                    }
                }
            }
            
        }
       
    }
    
    public void convertMap(int x,int y,int num,int[][] grid){
        Queue<Node> que = new LinkedList<>();
        que.offer(new Node(x,y,0));
        visit[x][y][0]=true;
        while(!que.isEmpty()){
            Node cur = que.poll();
            map[cur.x][cur.y]=num;
            for(int i=0;i<4;i++){
                int nx = cur.x+dir[i][0];
                int ny= cur.y+dir[i][1];
                
                if(nx >=0 && ny>=0 && nx < n && ny <n && !visit[nx][ny][0] && grid[nx][ny]==1){
                    map[nx][ny]=num;
                    visit[nx][ny][0]=true;
                    que.offer(new Node(nx,ny,0));
                
            }
            
        }
    }
    
}
}

class Node{
    int x,y,value;
    
    Node(int x,int y,int value){
        this.x=x;
        this.y=y;
        this.value=value;
    }
}