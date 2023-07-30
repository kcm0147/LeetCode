class Solution {
    Set<Character> set = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
    
    public int maxVowels(String s, int k) {
        int sum = 0;
        int start = 0;
        int result = Integer.MIN_VALUE;
        
        for(int end=0;end<s.length();end++){
            sum += set.contains(s.charAt(end)) ? 1: 0;
            if(end >=k-1){
                result = Math.max(sum,result);
                sum-= set.contains(s.charAt(start)) ? 1: 0;
                start++;
            }
        }
        
        return result;
        
        
    }
    
    
}