class UndergroundSystem:

    def __init__(self):
        self.checkin_store = {}
        self.stationpair_store = collections.defaultdict(lambda: [0, 0])  #Total time and count both

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_store[id] = [stationName, t]  #Check in

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin_store.pop(id) #Check out
        self.stationpair_store[(startStation, stationName)][0] += (t - startTime)  #1st element is total time
        self.stationpair_store[(startStation, stationName)][1] += 1        #2nd element is total counts

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalCounts = self.stationpair_store[(startStation, endStation)] #Get total time and counts
        return totalTime / totalCounts #Return average time

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)