class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        #Sliding window ka modification
        # Min Position and max position ke values nikal
        min_pos, max_pos, temp = -1,-1,-1
        result = 0
        for i in range(len(nums)):
            if minK <= nums[i] <=maxK:
                if nums[i] == minK:
                    min_pos = i
                if nums[i] == maxK:
                    max_pos = i
                result += max(0, min(min_pos,max_pos) - temp)
            else:
                temp = i 
        return result

# Time Complexity: O(N)
# Space Complexity: O(1)

# 1. We will use sliding window technique to solve this problem
# 2. We will have two pointers min_pos and max_pos
# 3. We will have a temp variable to keep track of the last position where we found a value between minK and maxK
# 4. We will iterate through the array and if we find a value between minK and maxK, we will update the min_pos and max_pos
# 5. We will also update the result by adding the max of 0 and min of min_pos and max_pos and temp
# 6. If we find a value which is not between minK and maxK, we will update the temp to the current position
# 7. We will return the result
