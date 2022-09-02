class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return board

        crushed = True 
        m, n = len(board), len(board[0])
        crush_coordinates = set()
        #Crush rows find out
        for x in range(m):
            for y in range(n-2):
                if board[x][y] == board[x][y+1] == board[x][y+2] != 0:
                    crushed = False
                    crush_coordinates.update([(x,y),(x,y+1),(x,y+2)])   
        
        #Crush columns find out
        for x in range(m-2):
            for y in range(n):
                if board[x][y] == board[x+1][y] == board[x+2][y] != 0:
                    crushed = False
                    crush_coordinates.update([(x,y),(x+1,y),(x+2,y)])  
        
        if crushed:
            return board
        #print("Crush coordinates are:-", crush_coordinates)   
        
        for x,y in crush_coordinates:
                board[x][y] = 0
                
        for c in range(n):
            # move all pos nums down
            idx = m - 1
            for r in range(m - 1, -1, -1):
                if board[r][c] > 0:
                    board[idx][c] = board[r][c]
                    idx -= 1

            # put 0s for missing pieces
            for r in range(idx, -1, -1):
                board[r][c] = 0

        return board if crushed else self.candyCrush(board)

'''
Mark where the candies can be crushed horizontally
Loop through the board and check 3 spots at a time to see if there is the same character and that character isn't 0
Mark where the candies can be crushed vertically
Same thing, but vertically
Crush the candies
Go through the set of crushable locations, and edit the original board
Shift candies down if there are zeroes below them.
Pay attention to the columns. We will start from the bottom of the board, and work our way up,
shifting the candies that were not crushed into their "fallen" position.
Find out where to determine whether or not a board's candies can be crushed anymore
If we loop through the entire board, and no candy was crushed, then we are finished.
'''