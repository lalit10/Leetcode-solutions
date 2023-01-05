class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        result = []
        words = sentence.split(' ')
        for word in words:
            curr = trie.root
            prefix_in_tree = False
            temp = ''

            for c in word:
                if curr.isEnd:
                    prefix_in_tree = True
                    break
                if c in curr.children:
                    temp+=c
                    curr = curr.children[c]
                else:
                    break
            if temp and prefix_in_tree:
                result.append(temp)
            elif not temp or not prefix_in_tree:
                result.append(word)
        return " ".join(result)

