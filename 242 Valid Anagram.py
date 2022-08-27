from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = Counter(s)
        t_dic = Counter(t)
        
        if s_dic == t_dic:
            return True
        return False