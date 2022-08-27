def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        
        left = 0
        max_length = 0
        
        store = {i: 0 for i in s}
        
        for i in range(len(s)):
            
            store[s[i]]+=1
            while store[s[i]] > 1:
                left +=1
                store[s[left-1]]-=1   #Modified from i to left-1  because we are moving left pointer
            length = i -left + 1
            
            max_length = max(length, max_length)
        
        return max_length