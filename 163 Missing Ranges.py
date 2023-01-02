class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        prev= lower-1
        store = []
        nums = [lower-1] + nums + [upper+1]

        for i in range(len(nums)-1):
            if nums[i+1] -nums[i] >1:
                store.append([nums[i]+1, nums[i+1]-1])
        #print("Store is:-", store)
        result = []
        for i in store:
            if i[0]==i[1]:
                result.append(str(i[0]))
            else:
                result.append(str(i[0]) + "->"+ str(i[1]))
        #print("Result is:-", result)
        return result
