class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = float('inf')
        res = 0
        
        for no in prices:
            temp = min(no, temp)
            profit = no -temp
            res = max(res, profit)
        return res

#Time Complexity: O(N)
#Space Complexity: O(1)