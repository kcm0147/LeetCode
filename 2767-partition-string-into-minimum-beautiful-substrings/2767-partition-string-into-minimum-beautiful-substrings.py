class Solution:
    
    def is_power_of_five(self,num):
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return num == 1
    
    
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                substring = s[j:i]
                if substring[0] != '0':  
                    number = int(substring, 2) 
                    if self.is_power_of_five(number):
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1