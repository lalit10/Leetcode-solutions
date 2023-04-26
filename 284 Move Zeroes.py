class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[left] = nums[i]
                left+=1
        for i in range(left, len(nums)):
            nums[i] = 0
        
class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        

        