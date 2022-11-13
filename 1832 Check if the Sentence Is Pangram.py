class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        store = collections.Counter(sentence)
        
        if len(store.keys()) == 26:
            return True
        else:
            return False
        