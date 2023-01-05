class Trie:

    def __init__(self):
        self.prefix_tree = {}

    def insert(self, word: str) -> None:
        store = self.prefix_tree
        for c in word:
            if c not in store:
                store[c] = {}
            store = store[c]
        store["$"] = True  #Used to end the string

    def search(self, word: str) -> bool:
        store = self.prefix_tree
        for c in word:
            if c not in store:
                return False
            store = store[c]
        return "$" in store        

    def startsWith(self, prefix: str) -> bool:
        store = self.prefix_tree
        for c in prefix:
            if c not in store:
                return False
            store = store[c]
        return True

        
#Time Complexity: O(n)
#Space Complexity: O(n)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#Another solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True