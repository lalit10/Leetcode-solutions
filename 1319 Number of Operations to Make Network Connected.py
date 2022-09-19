class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #Defaultdict use kar graph bana
        #DFS laga ke visited mei check kar
        
        if len(connections) < n-1: 
            return -1        
        
        store=collections.defaultdict(list) 
        
        for i ,j in connections:
            store[i].append(j)
            store[j].append(i)
        
        visited = set()
        result = 0
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
            for i in store[node]:
                if i not in visited:
                    dfs(i)
        
        for i in range(n): 
            if i not in visited:
                result +=1
                dfs(i)
        return result-1
            