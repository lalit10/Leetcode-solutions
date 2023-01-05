from heapq import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        minheap = []
        maxheap = []
        def balanceheap():
            while len(minheap) > len(maxheap):
                val = heappop(minheap)
                heappush(maxheap,-val)
            while len(maxheap) > len(minheap) + 1:
                val = heappop(maxheap)
                heappush(minheap,-val)


        while nums1 and nums2:
            heappush(minheap, nums1.pop(0))
            heappush(minheap, nums2.pop(0))
            balanceheap()

        while nums1:
            heappush(minheap, nums1.pop(0))
            balanceheap()
        
        while nums2:
            heappush(minheap, nums2.pop(0))
            balanceheap()

        #print(minheap[0], maxheap[0])
        #print(len(minheap), len(maxheap))
        if len(minheap) == len(maxheap):
            return (minheap[0]- maxheap[0]) /2
        else:
            return -maxheap[0]

