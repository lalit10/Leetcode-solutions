class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def helper(word):
            if not word:
                return
            char, count = [word[0]],[1]
            for i in range(1,len(word)):
                if word[i] == char[-1]:
                    count[-1] +=1
                else:
                    char.append(word[i])
                    count.append(1)
            return char, count

        s_char, s_count = helper(s) 
        result = 0
        for word in words:
            w_char, w_count = helper(word)
            counter = 0
            if s_char == w_char:
                #print(w_char,w_count, s_count)
                for i in range(len(w_char)):
                    if w_count[i]==s_count[i] or (w_count[i]<s_count[i] and s_count[i]>=3):
                        counter += 1
                if counter == len(w_char):
                    result+=1
        #print("Result is:-", result)
        return result