class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Sort the word
        #Check if in dict, if yes append else create one
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())