class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxElement = max(nums)
        for no in nums:
            if no != maxElement:
                if no*2 > maxElement:
                    return -1
        return nums.index(maxElement)