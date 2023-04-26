class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        result = []
        for i in range(len(arr)-1,-1,-1):
            result.append(arr[i])
        #print("Result is:-", result)
        return " ".join(result)



class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        l,r = 0,len(w)-1
        while l < r:
            w[l],w[r] = w[r],w[l]
            l += 1
            r -= 1
        return ' '.join(w)
        
        
            
            
        