class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        minDiff = float('inf')
        index = 0
        sum_arr = sum(nums)
        n = len(nums)
        temp = 0
        for i, val in enumerate(nums):
            temp +=val
            first = temp // (i+1)
            if i != n-1:
                second = (sum_arr - temp) // (n-i-1)
            else:
                second = 0
            diff = abs(first-second)
            if diff < minDiff:
                minDiff = diff
                index = i
        #print("Index is:-", index)
        return index