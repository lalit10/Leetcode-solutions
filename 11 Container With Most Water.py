class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        result = float("-inf")
        area = 0
        width = 0

        while i < j:
            curr_height = min(height[i],height[j])
            width = j-i
            area = width * curr_height
            result = max(result, area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return result
            