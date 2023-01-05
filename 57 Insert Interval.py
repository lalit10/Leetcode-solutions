class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        while(i<len(intervals) and intervals[i][0] < newInterval[0]):
            i+=1
        intervals.insert(i, newInterval)
        print(intervals)
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

#Time Complexity: O(n)
#Space Complexity: O(n)