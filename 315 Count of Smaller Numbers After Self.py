from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = SortedList(nums)
        result = []
        for no in nums:
            i = sorted_nums.index(no) #O(logN) https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.index
            #i =  bisect_left(sorted_nums,no) Same time complexity O(logN)
            result.append(i)
            sorted_nums.discard(no)  #O(logN) https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.remove
        #print(result)
        return result
        
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

#Another solution
from bisect import bisect_left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        for no in nums:
            i =  bisect_left(sorted_nums,no)
            result.append(i)
            del sorted_nums[i]
        #print(result)
        return result

# Time Complexity: O(nlogn)
# Space Complexity: O(n)