class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None

        minheap = []
        for no in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, no)
            else:
                if no > minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, no)
        return minheap[0]

#Time Complexity: O(nlogk)
#Space Complexity: O(k)