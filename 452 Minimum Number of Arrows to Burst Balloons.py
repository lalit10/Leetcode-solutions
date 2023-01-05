class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #Similar to merge intervals, just count of number of intervals at the end
        points.sort(key = lambda x : x[0])
        result = []
        for start, end in points:
            if len(result)>0 and result[-1][1] >= start:
                last_start, last_end = result.pop()
                result.append( [max(start, last_start), min(end, last_end)])
                #print(result)
            else:
                result.append([start, end])
        return len(result)

#Time Complexity: O(nlogn)
#Space Complexity: O(n)