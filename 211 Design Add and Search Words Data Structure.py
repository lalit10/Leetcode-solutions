class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.max_word_length = 0

    def addWord(self, word: str) -> None:
        curr =  self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        self.max_word_length = max(self.max_word_length, len(word))

    def search(self, word: str) -> bool:
        if len(word) > self.max_word_length:  #Hack to get it accepted so that cases are discarded
            return False
        def dfs(word, root):            
            for i, char in enumerate(word):
                if char == ".":
                    for child in root.children:
                        childNode = root.children[child]
                        if dfs(word[i+1:], childNode):
                            return True
                    return False
                else:
                    if char not in root.children:
                        return False
                    root = root.children[char]
            return root.isEnd
        
        root = self.root
        return dfs(word, root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)