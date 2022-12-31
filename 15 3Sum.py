class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            target = 0- nums[i]
            while j <k:
                if nums[j] + nums[k] == target:
                    result.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    j+=1
        return list(result)
            
        