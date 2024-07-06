class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div = time // (n - 1)
        rest = time % (n - 1)
        
        if div % 2 == 0:
            result = 1 + rest
        else:
            result = n - rest
        
        return result