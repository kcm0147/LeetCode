class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> edge = new ArrayList<>();
        int[] edgeCountAry = new int[numCourses];
        int finishCouresCnt = 0;
        boolean find = true;
        for(int i=0;i<numCourses;i++){
            edge.add(new ArrayList<>());
        }
        for(int i=0;i<prerequisites.length;i++){
            int first = prerequisites[i][1];
            int second = prerequisites[i][0];
            edgeCountAry[second]++;
            edge.get(first).add(second);
        }
        
        while(find){
            find = false;
            for(int i=0;i<edgeCountAry.length;i++){
                if(edgeCountAry[i]==0){
                    find = true;
                    finishCouresCnt++;
                    edgeCountAry[i]=-1;
                    List<Integer> edges = edge.get(i);
                    for(int j=0;j<edges.size();j++){
                        edgeCountAry[edges.get(j)]--;
                    }
                }
            }
        }
        return finishCouresCnt==numCourses ? true : false;
        
    }
}