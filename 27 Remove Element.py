class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for ind, i in enumerate(nums):
            if i!=val:
                nums[k] = nums[ind]
                k+=1
        return k