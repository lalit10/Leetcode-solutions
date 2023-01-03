class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = []
        endTimes = []
        
        for interval in intervals:
            startTimes.append(interval[0])
            endTimes.append(interval[1])
        
        #print("Start time is:-", startTimes)
        startTimes.sort()
        endTimes.sort()
        
        start = end = 0
        result = available = 0
        
        while start <len(startTimes):
            if startTimes[start] < endTimes[end]:  #If the start time is less than the end time, then we can use the room
                if available == 0:  #If there are no rooms available, then we need to create a new room
                    result += 1
                else: #If there are rooms available, then we can use the room
                    available -= 1
                    
                start += 1
            else:  #If the start time is greater than the end time, then we can't use the room
                available += 1
                end += 1
        
        return result
        
        
#Another solution:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:        
        #Using minheap to store endTimes
        intervals.sort(key = lambda x:x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heapreplace(rooms, i[1])
            else:
                heapq.heappush(rooms,i[1])
        return len(rooms)

