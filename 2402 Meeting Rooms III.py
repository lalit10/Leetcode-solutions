# Algorithm:
# Two Heap:
#      One heap record the ready room
#      another heap record the room holding meeting and the end time
# Also, use the ans arry to record the times each used.
# if there is a ready room, push the room to the meeting room
# if there is not a ready room, pop the room with earliest end time, and push again with new end time

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key= lambda x:x[0])

        curr_room = []
        ready_room = [i for i in range(n)]
        heapify(ready_room)
        num_meetings = [0]*n

        for start, end in meetings:
            while curr_room and curr_room[0][0]<=start:
                a,b = heappop(curr_room)  # a = time, b = room no
                heappush(ready_room, b)
            
            if ready_room:
                # If room available, push it along with end time
                room_no = heappop(ready_room)
                heappush(curr_room, [end, room_no])
                num_meetings[room_no]+=1
            else:
                #Pop the latest available room and push to it with updated end time
                time, room_no = heappop(curr_room)
                heappush(curr_room, [(time +end- start), room_no])
                num_meetings[room_no]+=1
        #print(num_meetings)
        ind, res = 0, num_meetings[0]
        for i in range(n):
            if num_meetings[i] > res:
                ind, res = i, num_meetings[i]
        return ind

# Time Complexity: O(NlogN)
# Space Complexity: O(N)