class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #Binary search and DP inside
        low, high = max(nums), sum(nums)
        while low<high:
            mid = (low+high)//2
            n , curr = 1, 0
            for i in nums:
                curr+=i
                if curr > mid:
                    curr = i
                    n+=1
            if n<=k:
                high = mid
            else:
                low = mid+1
        return low

#Time Complexity: O(NlogN)
#Space Complexity: O(1)

#https://leetcode.com/problems/split-array-largest-sum/solutions/89846/Python-solution-with-detailed-explanation/

