class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.hot_degree = 0
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence, hot_degree):
        curr = self.root
        for c in sentence:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        if curr.isEnd:
            curr.hot_degree += hot_degree
        else:
            curr.isEnd = True
            curr.hot_degree = hot_degree

    def search(self, word):
        def traverse(node, sentence):
            nonlocal results
            if node.isEnd:
                to_insert = (node.hot_degree, sentence)
                results.append(to_insert)
            for char in node.children:
                traverse(node.children[char], sentence + char)

        results = []
        curr = self.root
        for c in word:
            if c not in curr.children:
                return results
            curr = curr.children[c]
        traverse(curr, word)
        #print(results)
        results.sort(key=lambda x:(-x[0], x[1])) #Sorting in descending order by hot degree and for breaking ties use the sentence to sort by lexicographic order, ie, ascending order
        #print(results)
        return [x[1] for x in results[:3]]

    

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.search_input = ""
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search_input, 1)
            self.search_input = ""
        else:
            self.search_input += c
            return self.trie.search(self.search_input)



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)