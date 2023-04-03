class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        temp = 0
        for i in range(len(nums)):
            if total - nums[i] -temp == temp:
                return i
            else:
                temp+=nums[i]
        return -1
            