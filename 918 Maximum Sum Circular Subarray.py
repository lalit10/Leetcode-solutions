class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #Kadane's algorithm study it, Problem 53,152
        currentMax = nums[0]
        maxSoFar = nums[0]
        currentMin = nums[0]
        minSoFar = nums[0]
        for num in nums[1:]:
            currentMax = max(num, currentMax + num)
            maxSoFar = max(currentMax, maxSoFar)
            currentMin = min(num, currentMin + num)
            minSoFar = min(currentMin, minSoFar)
        if sum(nums) == minSoFar:    
            return maxSoFar
        return max(maxSoFar, sum(nums) - minSoFar)

# Time Complexity:  O(n)
# Space Complexity: O(1)