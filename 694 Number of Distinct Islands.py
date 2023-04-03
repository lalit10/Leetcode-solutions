class Solution:
    def _dfs(self, grid, i, j, path, rootI, rootJ):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return path
        
        grid[i][j] = 0
        path.append((i - rootI, j - rootJ))
        self._dfs(grid, i, j+1, path, rootI, rootJ) # right
        self._dfs(grid, i+1, j, path, rootI, rootJ) # down
        self._dfs(grid, i, j-1, path, rootI, rootJ) # left
        self._dfs(grid, i-1, j, path, rootI, rootJ) # up
        return path
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinctIslands = set()
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num:
                    path = []
                    distinctIslands.add(tuple(self._dfs(grid, i, j, path, i, j)))
        return len(distinctIslands)
        
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)