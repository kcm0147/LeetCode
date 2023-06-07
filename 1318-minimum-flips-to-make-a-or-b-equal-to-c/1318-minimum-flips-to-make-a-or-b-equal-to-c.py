class Solution(object):
    def minFlips(self, a, b, c):
        modifications = 0
        while a > 0 or b > 0 or c > 0:
            ca = a & 1
            cb = b & 1
            cc = c & 1

            # If current bit in c is 0
            if cc == 0:
                modifications += ca + cb  
            elif cc == 1:
                modifications += 1 - max(ca, cb)

            a >>= 1
            b >>= 1
            c >>= 1
        return modifications
        