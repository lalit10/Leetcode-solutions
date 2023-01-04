class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        #DFS , backtracking feels
        def dfs(word):
            m,n  = len(word), len(word[0])
            if m==n:
                result.append(word)
                return
            req_prefix = ""
            for i in range(m):
                req_prefix += word[i][m]
            #print("Required prefix is", req_prefix)            
            if req_prefix in prefix_dict:
                all_prefix = prefix_dict[req_prefix]
                for prefix in all_prefix:
                    dfs(word+[prefix])
            else:
                return
            
        no = len(words[0])
        if no==1:
            return words
        
        prefix_dict = defaultdict(set)
        for word in words:
            for i in range(no):
                prefix_dict[word[:i]].add(word)
        #print("Prefix dict is:-", prefix_dict)
        
        result = []
        
        for word in words:
            dfs([word])
        return result
        
#Time complexity: O(n. 26^n)
#At any node at max 26 branches can be there, and at max n nodes can be there so O(26^n)
#Space Complexity: O(nL + nL/2) where L is length of each word
#nL for prefix_dict and nL/2 for recursion stack