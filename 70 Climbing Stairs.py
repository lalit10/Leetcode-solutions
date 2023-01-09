class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a,b=1,1
        for i in range(2,n+1):
            a,b=b,a+b
        return b

#Another solution
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        steps[0]= steps[1]=1
        for i in range(2, n+1):
            steps[i] = steps[i-1]+steps[i-2]
        return steps[n]