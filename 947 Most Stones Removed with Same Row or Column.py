from collections import deque,defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #BFS
        #Two graphs for x and y each
        #Check in x or in y
        
        graph_x = defaultdict(list)
        graph_y = defaultdict(list)

        visited = set()

        for x,y in stones:
            graph_x[x].append(y)
            graph_y[y].append(x)

        result = 0

        for x,y in stones:

            if (x,y) not in visited:
                que = deque([(x,y)])
                while que:
                    xx,yy = que.popleft()
                    
                    if (xx,yy) not in visited:
                        visited.add((xx,yy))
                        for nei in graph_x[xx]:
                            que.append((xx,nei))
                        for nei in graph_y[yy]:
                            que.append((nei,yy))
                result+=1        
        return len(stones) - result

# Time Complexity: O(N) where N is the number of stones
# Space Complexity: O(N)