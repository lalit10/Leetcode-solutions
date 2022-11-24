from collections import deque,defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #BFS
        
        store_x = defaultdict(list)
        store_y = defaultdict(list)
        
        visited = set()

        for x,y in stones:
            store_x[x].append(y)
            store_y[y].append(x)
        
        shared_components = 0
        
        for x,y in stones:
            
            if (x,y) not in visited:
                que = deque([(x,y)])
                while que:
                    xx,yy = que.popleft()
                    
                    if(xx,yy) not in visited:
                        visited.add((xx,yy))
                        for nei in store_x[xx]:
                            que.append((xx,nei))
                        for nei in store_y[yy]:
                            que.append((nei,y))
                shared_components +=1
        
        return len(stones) - shared_components

