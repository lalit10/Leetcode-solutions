class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]

        if not curr and len(nums) >1:
            return False
        
        for no in nums[1:len(nums)-1]:
            curr = max(curr-1, no)
            if not curr:
                return False
        return True

# Time Complexity: O(N)
# Space Complexity: O(1)
