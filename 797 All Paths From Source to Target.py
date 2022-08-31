class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(current, path, result):
            
            new_path = list(path)
            new_path.append(current)
            
            if current == len(graph)-1:
                result.append(new_path)
                return
            
            for neighbor in graph[current]:
                dfs(neighbor, new_path, result)
        
        result = []
        dfs(0, [], result)
        return result