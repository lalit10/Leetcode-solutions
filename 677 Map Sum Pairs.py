class TrieNode:

    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.store = {}

    def insert(self, key: str, val: int) -> None:
        diff = val
        if key in self.store:
            diff = val -self.store[key]
        self.store[key] = val

        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.score +=diff

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        return curr.score
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)