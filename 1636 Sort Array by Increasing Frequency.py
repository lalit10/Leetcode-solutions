from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        store = Counter(nums)
        return sorted(sorted(nums, reverse=True), key=lambda x: store[x])



#We are going to use a dictionary to keep track of the frequency that a number appears in the array.
#  After we have done that we first sort the array in decreasing order and then sort it in increasing order by frequency.
#  This works because sorts are guarenteed to be stable. Read this if you need help understanding why this works. 
# https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts