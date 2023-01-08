class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        store_s = {}
        store_t = {}
        for i in range(len(s)):
            if s[i] not in store_s:
                store_s[s[i]] = t[i]
            if t[i] not in store_t:
                store_t[t[i]] = s[i]
            if store_s[s[i]] != t[i] or store_t[t[i]] != s[i]:
                return False
        return True