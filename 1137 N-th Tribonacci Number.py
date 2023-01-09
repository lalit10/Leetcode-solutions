class Solution:
    def tribonacci(self, n: int) -> int:       
        
        if n ==0:
            return 0
        elif n ==1 or n==2:
            return 1
        else:
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1]= dp[2] = 1
            for i in range(3, n+1):
                dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
# Time Complexity: O(N)
#Space Complexity: O(N)

#Another solution
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:            
            return 0
        if n == 1 or n==2:           
            return 1
        thirdLast = 0
        secondLast = 1        
        last = 1             
        current = None     
        for i in range(1,n-1):   
            current =thirdLast + secondLast + last  
            thirdLast = secondLast
            secondLast = last  
            last = current
        return current 
        
# Time Complexity: O(N)
#Space Complexity: O(1)