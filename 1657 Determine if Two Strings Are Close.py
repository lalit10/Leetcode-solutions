class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False
        else:
            store1 = Counter(word1)
            store2 = Counter(word2)
            if store1.keys() == store2.keys() and sorted(store1.values()) == sorted(store2.values()):
                return True
            return False
        