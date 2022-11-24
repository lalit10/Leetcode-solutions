class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        current = values[0]
        result = 0
        
        for i in range(1,len(values)):
            result = max(result, current + values[i]-i)
            current = max( current, values[i]+i)
        return result
        
# Time Complexity: O(n)
# Space Complexity: O(1)