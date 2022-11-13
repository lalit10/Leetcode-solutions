class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        #BFS se ho jaana chahiye 
        #Queue bana popleft
        # Check in bank and remove ya fir visited mei daal 
        
        queue, visited = deque([(start, 0)]), {start}  
                                                        
        while queue:
            s, n = queue.popleft()                     
                                                       
            if s == end: 
                return n                      
                                                       
            for i in range(8):                          
                for ch in 'ACGT':
                    word = s[:i] + ch + s[i+1:]                
                    if word in bank and word not in visited:      
                        visited.add(word)
                        queue.append((word, n+1))
        return -1

# Space Complexity: O(N) where N is the length of bank