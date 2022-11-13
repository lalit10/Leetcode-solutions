class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        result = []
        for i in range(len(arr)-1,-1,-1):
            result.append(arr[i])
        #print("Result is:-", result)
        return " ".join(result)