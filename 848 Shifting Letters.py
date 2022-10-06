class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        if len(shifts)>1:
            for i in range(len(shifts)-2,-1,-1):
                shifts[i]+=shifts[i+1]                 
    
        result = ""
        for i in range(len(s)):
            c = chr(((ord(s[i])+shifts[i]-ord("a"))%26)+ord("a"))
            result+=c
        return result