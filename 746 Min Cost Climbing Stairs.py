class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Recurrence relation
        #dp[i] = min(dp[i-1], dp[i-2]) +nums[i]
        n =len(cost)
        dp = [0]*n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])

# Time Complexity: O(N)
#Space Complexity: O(N)