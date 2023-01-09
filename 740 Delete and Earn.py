class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
            This question is similar to https://leetcode.com/problems/house-robber.
            The only difference here is we need to first calculate the money in each house.
            Let us consider, we have houses from 0 to max(nums). Now each time a number occurs in nums,
            we add that number to its corresponding house.
            At the end we will left with houses and the money they have.
            
        """
        if not nums:
            return 0

        store = [0] * (max(nums)+1)
        for n in nums:
            store[n] += n       

        dp = [0] * len(store)
        dp[1] = store[1]
        for i in range(2, len(store)):
            dp[i] = max(store[i] + dp[i-2], dp[i-1])

        return dp[len(store)-1]

        

# Time Complexity: O(N)
# Space Complexity: O(N)

# Another solution
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # We need to find the max value of the array
        max_val = max(nums)
        # We need to create an array of size max_val + 1
        # The reason is that we need to store the count of each element in the array
        # For example, if we have an array like [2, 2, 3, 3, 3, 4]
        # We need to create an array of size 5, where we store the count of each element
        # So, the array will look like [0, 0, 2, 3, 1]
        # The reason we have 0 at index 0 is because we don't have 0 in the input array
        arr = [0] * (max_val + 1)
        for n in nums:
            arr[n] += n
        # Now, we need to apply the house robber problem
        # Since we can't choose the adjacent elements, we need to find the maximum sum
        # We need to find the maximum sum of the array
        # We need to create a dp array of size max_val + 1
        # The reason is that we need to store the maximum sum till that index
        # So, the dp array will look like [0, 0, 2, 4, 4]
        # The reason we have 0 at index 0 is because we don't have 0 in the input array
        dp = [0] * (max_val + 1)
        dp[1] = arr[1]
        for i in range(2, max_val + 1):
            dp[i] = max(arr[i] + dp[i-2], dp[i-1])
        return dp[max_val]