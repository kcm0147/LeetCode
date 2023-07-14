class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        int result = 1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            Integer curAnswer = map.get(arr[i] - difference);
            if (curAnswer == null) {
                map.put(arr[i], 1);
            } else {
                map.put(arr[i], curAnswer + 1);
                result = Math.max(result, curAnswer + 1);
            }
        }
        return result;
    }
}