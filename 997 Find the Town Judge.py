class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_store, trusted_store = defaultdict(int), defaultdict(int)

        for i,j in trust:
            trust_store[i]+=1
            trusted_store[j]+=1
        
        for i in range(1,n+1):
            if trust_store[i] ==0 and trusted_store[i]== n-1:
                return i
        return -1