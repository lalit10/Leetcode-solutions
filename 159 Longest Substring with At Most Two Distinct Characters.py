class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        store = defaultdict(int)
        result  = float('-inf')
        cnt = 0
        i,j = 0, 0
        while j < len(s):
            curr = s[j]
            store[curr] +=1
            while len(store) >2:
                store[s[i]]-=1
                if store[s[i]] ==0:
                    del store[s[i]]
                i+=1
            result = max(result, j-i+1)
            j+=1
        return result
