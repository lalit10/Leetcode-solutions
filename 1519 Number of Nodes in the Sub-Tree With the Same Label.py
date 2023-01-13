class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        store, label_count, result = defaultdict(list), defaultdict(int), [0] * n
        
        for a, b in edges:                             
            store[a].append(b)
            store[b].append(a)
        
        def dfs(node=0, par=None):                    
            prev = label_count[labels[node]]
            label_count[labels[node]] += 1
            
            for child in store[node]:
                if child != par: dfs(child, node)

            result[node] = label_count[labels[node]] - prev    

        dfs()
        return result   