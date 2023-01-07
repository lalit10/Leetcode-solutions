class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        #Creating the graph
        for course, prereq in prerequisites:
            courses[prereq].append(course)
        # -1 current visit stack, 1: visited, 0 not visited, for keeping track in dfs
        visited = [0 ] * numCourses
        #print(visited)
        result = []
        #DFS over the graph
        for course in range(numCourses):
            if not self.dfs(course, visited, result, courses):
                return []
        #print("Result is", result)
        return result[::-1]
    
    def dfs(self, course, visited, result, courses):
        # already visited in current DFS call, cycle! 
        if visited[course]==-1:
            return False
        # Node visited
        if visited[course] ==1:
            return True
        
        # currently visiting, so marked as -1
        visited[course]= -1
        for c in courses[course]:
            if not self.dfs(c, visited, result, courses):
                return False
        # Mark visited at the end of DFS
        visited[course] = 1
        # Traversed, add to result list
        result.append(course)
        return True
    

    