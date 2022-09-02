def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Graph bana
        #Create a set for visited
        #DFS function
        #Iterate on graph nodes and if in visited ignore else
        #add to all_paths
        #Return any all_paths
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        
        def dfs(node, dest):
            if node == dest:
                return True
                
            visited.add(node)
            
            all_paths = []
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                all_paths.append(dfs(neighbor, dest))
			# return true if any of the paths were able to find the value
            return any(all_paths)
        
        return dfs(source, destination)


#BFS Solution
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Graph bana
        #Create a set for visited
        #Create a queue for BFS
        #Append start to que
        #Iterate on que and popleft
        #Check if adjacent node in visited
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        
        que = collections.deque()
        visited.add(source)
        que.append(source)
        
        while que:
            node = que.popleft()
            if node == destination:
                return True
            
            for adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    que.append(adjacent_node)
                    visited.add(adjacent_node)
                    
        return False