class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        comb_store = defaultdict(list)

        for word in wordList:
            for i in range(L):
                comb_store[word[:i]+"*"+word[i+1:]].append(word)

        #print("All combinations:-", comb_store) 
        que = deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)
        while que:
            curr_word, level = que.popleft()
            for i in range(L):
                temp = curr_word[:i] + "*"+ curr_word[i+1:]
                for word in comb_store[temp]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        que.append((word, level+1))
        return 0

# Time Complexity: O(M^2 * N) where M is the length of each word and N is the total number of words in the input word list.
# Space Complexity: O(M^2 * N) 