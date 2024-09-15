class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for cur in strs:
            key = ''.join(sorted(cur))
            result[key].append(cur)
            
        return list(result.values())