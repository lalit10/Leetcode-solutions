class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

#Another solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []        
        while len(intervals) >=2:
            if intervals[1][0] <= intervals[0][1]:
                prev = heapq.heappop(intervals)
                curr = heapq.heappop(intervals)
                curr = [prev[0], max(prev[1], curr[1])]
                heapq.heappush(intervals, curr)
                #print(intervals)
            else:
                result.append(heapq.heappop(intervals))        
        result.append(intervals[0])
        return result