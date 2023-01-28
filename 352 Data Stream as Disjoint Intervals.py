class SummaryRanges:

    def __init__(self):
        self.intervals = []
        

    def addNum(self, value: int) -> None:
        heapq.heappush(self.intervals, [value, value])
        

    def getIntervals(self) -> List[List[int]]:
        temp = []

        while self.intervals:
            curr = heapq.heappop(self.intervals)
            if temp and curr[0] <= temp[-1][1] + 1:
                temp[-1][1] = max(temp[-1][1], curr[1])
            else:
                temp.append(curr)

        self.intervals = temp
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()