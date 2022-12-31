class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        k, l = float('-inf'), 0

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                k = i
        if k == float('-inf'):
            nums.reverse()
            return 
        
        for i in range(k+1, len(nums)):
            if nums[k] < nums[i]:
                l = i
                
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[k+1:][::-1]  


