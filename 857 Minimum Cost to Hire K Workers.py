class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        #Heapq use kar
        #1. wage i/wage j  = quality i / quality j
        #2. Minimum wage is to be paid

        #Store price by quality in one heap
        #Selected workers in another heap
        pq_store = []
        for i in range(len(wage)):
            heapq.heappush(pq_store, (float(wage[i]/quality[i]), quality[i]))
        #print("Price quality heap", pq_store)

        workers = []
        total_sum = 0
        result = float('inf')

        while pq_store:
            p,q = heapq.heappop(pq_store)
            heapq.heappush(workers,-q)

            total_sum+=q
            if len(workers) > k:
                total_sum+= heapq.heappop(workers)
            if len(workers) ==k:
                result = min (result, p * total_sum)
        #print(workers)
        return result

       
#Time Complexity: O(nlogn)
#Space Complexity: O(n)


