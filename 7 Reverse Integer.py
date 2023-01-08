class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x = -x if x<0 else x
        res = 0
        while x:
            rem = x%10            
            res = (res*10) + rem
            x=x//10
        return 0 if res > pow(2, 31) else res * sign