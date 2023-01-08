class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        visited = set()
        
        def dfs(s, last_n):
            
            if len(visited) == k**n:
                return s
            if len(last_n)< n:
                if len(s+ "0") ==n:
                    visited.add(s+"0")
                res = dfs(s+"0", last_n+"0")
                return res
            res = None
            for i in range(k):
                temp = last_n[1:]+ str(i)
                if temp not in visited:
                    visited.add(temp)
                    res  = dfs(s+str(i), temp)
                    if res:
                        return res
                    visited.remove(temp)
        return dfs("","")
                