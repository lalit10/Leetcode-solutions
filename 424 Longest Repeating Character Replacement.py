def characterReplacement(self, s: str, k: int) -> int:
        if len(s) ==0:
            return 0
        
        left = 0
        max_length = 0
        
        store = {}
        
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]] = 1
            else:
                store[s[i]]+=1            
            
            length = i -left + 1
            
            if length - max(store.values()) <= k:  # Logic for k
                max_length = max(length, max_length)
            else:
                store[s[left]]-=1
                if not store[s[left]]:
                    store.pop(s[left])
                left +=1         
        
        return max_length