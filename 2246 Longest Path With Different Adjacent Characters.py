class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        store = {}
        
        for i in range(len(parent)):
            if parent[i] in store:
                store[parent[i]].append(i)
            else:
                store[parent[i]] = [i]
                
        result = 1        
        def dfs(n):
            nonlocal result
            if n not in store:
                return 1
            
            largest=0 
            second_largest=0 
            for u in store[n]:
                curr = dfs(u)
                if s[u]!=s[n]:
                    if curr>largest:
                        second_largest = largest
                        largest = curr
                    elif curr>second_largest:
                        second_largest = curr
                        
            result = max(result,largest+second_largest+1) 
            
            return largest+1  
        
        dfs(0)
        return result

# Time Complexity:  O(n)
# Space Complexity: O(n)