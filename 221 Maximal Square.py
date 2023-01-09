class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #Recurrence relation compare with all rem 3 and add 1 with min value
        if not matrix:
            return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        #print(dp)
        res = 0
        for i in range(1,m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])        
        return res*res

# Time Complexity: O(M*N)
# Space Complexity: O(M*N)