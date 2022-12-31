class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Sliding window and store max length
        store = defaultdict(int)
        result  = float('-inf')
        cnt = 0
        i,j = 0, 0
        while j < len(fruits):
            fruit = fruits[j]
            store[fruit] +=1
            while len(store) >2:
                store[fruits[i]]-=1
                if store[fruits[i]] ==0:
                    del store[fruits[i]]
                i+=1
            result = max(result, j-i+1)
            j+=1
        return result
