from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = []  #Max Heap
        self.large = []  #Min heap
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -self.small[0])
        heappop(self.small)
        
        if len(self.small) < len(self.large) :
            heappush(self.small, -self.large[0])
            heappop(self.large)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return - self.small[0]
        else:
            return (self.large[0]- self.small[0]) /2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()