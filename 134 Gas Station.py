class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #gas i less than cost i ignore
        
        if sum(gas) < sum(cost):
            return -1
            
        tank, start = 0,0

        for i in range(len(gas)):
            tank+= gas[i] - cost[i]

            if tank<0:
                start=i+1
                tank = 0
        return start
            
# Time Complexity: O(N)
#Space Complexity: O(1)