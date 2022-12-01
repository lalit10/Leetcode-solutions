class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False    

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):            
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
        
            

#My coded solution
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:         
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 #print("Word is:-", word)
#                 if self.dfs(board, word, i, j):
#                     return True
#         return False
                
#     def dfs(self, board, word, i, j):        
#         if i <= -1 or i >= len(board) or j <= -1 or j >= len(board[0]):
#             return False
#         if board[i][j] == -1 or board[i][j] != word[0]:
#             return False
#         if len(word) == 1:
#             return True
#         temp, board[i][j] = board[i][j], "#"
#         if self.dfs(board, word[1:], i+1, j) or self.dfs( board, word[1:], i-1, j) or self.dfs(board, word[1:],i, j+1) or self.dfs(board,word[1:], i, j-1):
#             return True
#         board[i][j] = temp
#         return False
        
            
        
        
        