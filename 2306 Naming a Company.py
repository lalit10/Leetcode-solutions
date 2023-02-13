class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        #Set of ideas
        #1st chars ka array
        #Freq ka ek dict usmei store
        #Create result
        #Finally check if word not in set, add to result
        store = set(ideas)
        frequency = Counter()
        letters = {x[0] for x in ideas}
        for i in ideas:
            for ch in letters:
                if ch+ i[1:] not in store:
                    frequency[i[0],ch]+=1  #Initial store first letter and the character
        result = 0
        for i in ideas:
            for ch in letters:
                if ch + i[1:] not in store:
                    result += frequency[ch, i[0]]   # Because swap karna hai letters ko
        return result

