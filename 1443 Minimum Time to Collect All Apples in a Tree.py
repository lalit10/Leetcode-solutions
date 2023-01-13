class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        store = defaultdict(list)
        
        # Build graph
        for src, dst in edges:
            store[src].append(dst)
            store[dst].append(src)
        
        # Record of visited nodes
        visited = set()
        def dfs(curr_node):
            
            visited.add(curr_node)
            
            cost = 0            
            for node in store[curr_node]:                
                if node in visited:
                    continue         
                
                cost_node = dfs(node)
                
                if cost_node or hasApple[node]:                   
                    cost += cost_node + 2
            
            return cost
        
        return dfs(0)