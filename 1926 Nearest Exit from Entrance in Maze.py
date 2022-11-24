from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #BFS karneka
        m,n = len(maze), len(maze[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]        
        que = deque([[entrance[0],entrance[1],0]])
        maze[entrance[0]][entrance[1]] = '+'
        
        while que:
            x,y,steps = que.popleft()
            #print(x,y,steps)
            #Breaking condition 
            if (x == m-1 or y==n-1 or 0 in [x,y]) and [x,y]!= entrance:
                return steps
            
            for i,j in directions:
                x1,y1 = x+i, y+j                
                if 0<= x1<m and 0<=y1<n and maze[x1][y1] == '.':
                    maze[x1][y1] = "+"
                    que.append([x1,y1,steps+1])
                
        return -1
        