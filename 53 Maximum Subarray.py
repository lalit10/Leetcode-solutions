class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Sliding window
        #Initialize sum with zero and create a temp variable to store subarray sum
        #start from next element
        #Compare ---- should work
        
        curSum = nums[0]
        maxSum =  nums[0] # float('-inf')
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# Time Complexity: O(N)
# Space Complexity: O(1)
        
        