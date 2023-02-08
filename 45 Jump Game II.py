class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest_reach = 0
        result = 0 
        left = right = 0
        while right < len(nums)-1:
            for i in range(left,right+1):
                farthest_reach = max(farthest_reach, i+nums[i])
            result+=1
            left = right+1
            right = farthest_reach
        return result
        