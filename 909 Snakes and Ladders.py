class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #Ek dict mei snake and ladder daal de
        #BFS kar
        store = {}
        
        current_position = 0
        direction = 1
        for row in board[::-1]:
            for val in row[::direction]:
                current_position += 1
                if val > -1:
                    store[current_position] = val
            direction = -direction
        
        queue = deque()
        queue.append((1, 0))
        visited = set()
        while queue:
            pos, turn = queue.popleft()
            for roll in range(1,7):
                new_pos = pos + roll
                
                if new_pos not in visited:
                    visited.add(new_pos)
                    new_pos = store.get(new_pos, new_pos)
                    queue.append((new_pos, turn + 1))
                
                if new_pos == current_position:
                    return turn + 1                    
        return -1
