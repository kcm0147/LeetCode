
class Solution:
    def lcm(x, y) -> int:
        return abs(x * y) // math.gcd(x, y)
    
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm_value = lcm(divisor1, divisor2)
        
        left, right = 1, 10**10
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            not_div_by_1 = mid - (mid // divisor1)
            not_div_by_2 = mid - (mid // divisor2)
            not_div_by_both = mid - (mid // lcm_value)
            
            if not_div_by_1 >= uniqueCnt1 and not_div_by_2 >= uniqueCnt2 and not_div_by_both >= (uniqueCnt1 + uniqueCnt2):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer