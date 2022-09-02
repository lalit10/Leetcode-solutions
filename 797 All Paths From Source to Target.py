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

#BFS Solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        que = collections.deque()
        path = [0]
        que.append(path)
        while  que:
            current_path = que.popleft()
            node = current_path[-1]
            for item in graph[node]:
                temp = current_path.copy()
                temp.append(item)
                
                if item ==len(graph) -1:
                    paths.append(temp)
                else:
                    que.append(temp)
        return paths