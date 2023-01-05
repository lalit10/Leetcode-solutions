class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()       
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]    
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, trie.root, "", res)                
        return res
    
    def dfs(self, board, i, j, node, path, result):
        if node.isEnd:
            result.append(path)
            node.isEnd = False
        
        m, n = len(board), len(board[0])
		
        if i < 0 or i >=m or j < 0 or j >= n or board[i][j] not in node.children:
            return         
		
        temp = board[i][j]
        board[i][j], curr = '$', node.children[temp]
       
        self.dfs(board, i+1,j, curr, path+temp, result)
        self.dfs(board, i-1,j, curr, path+temp, result)
        self.dfs(board, i,j+1, curr, path+temp, result)
        self.dfs(board, i,j-1, curr, path+temp, result)
        board[i][j] = temp
        
        # pruning: if it is a leaf and a matched word is found for it already, pop it to decrease trie size
        if len(node.children[temp].children) == 0:
            del node.children[temp]

#Time Complexity: O(m*n*4^l) where m is the number of rows, n is the number of columns and l is the length of the longest word in the dictionary
#Space Complexity: O(m*n) for the recursion stack and O(l) for the path string

#Once verify time and space complexity