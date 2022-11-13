class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x,y in points:
            dist = math.sqrt((x*x) + (y*y))
            
            if len(max_heap)<k :
                heapq.heappush(max_heap,(-dist,(x,y)))
            else:
                heapq.heappushpop(max_heap,(-dist,(x,y)))
        return[max_heap[i][1] for i in range(k)]

#Time Complexity: O(nlogk)
#Space Complexity: O(k)