class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for course, prereq in prerequisites:
            courses[prereq].append(course)
        # -1 current visit stack, 1: visited, 0 not visited, for keeping track in dfs
        visited = [0] * numCourses

        for course in range(numCourses):
            if not self.dfs(course,visited, courses):
                return False
        return True

    def dfs(self, course, visited, courses):

        if visited[course]== -1:
            return False
        if visited[course]==1:
            return True

        visited[course]=-1
        for c in courses[course]:
            if not self.dfs(c, visited, courses):
                return False
        visited[course]=1
        return True
