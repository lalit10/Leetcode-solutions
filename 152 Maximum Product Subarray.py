class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curSum = 1
        maxSum = nums[0]
        
        for no in nums:
            curSum*=no
            maxSum = max(curSum, maxSum)
            if curSum == 0:
                curSum =1
        
        curSum = 1
        
        for no in reversed(nums):
            curSum*=no
            maxSum = max(curSum, maxSum)
            if curSum == 0:
                curSum =1
        return maxSum

# Time Complexity: O(N)
# Space Complexity: O(1)

#Another solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
			
            res = max(res, curMax)
            
        return res

