class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap) *-1
            y = heapq.heappop(heap) *-1
            res = x-y
            heapq.heappush(heap, -1*res)
        return heap[0]*-1

#Time Complexity: O(nlogn)
#Space Complexity: O(n)