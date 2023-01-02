class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        #Simultaneous operations so use dictionary
        #Create a combined dictionary, use zip of python to do so
        #Trying iterating over array first
        no = len(indices)
        res = list(s)
        for i in range(no):
            if s[indices[i]:indices[i]+len(sources[i])] == sources[i]:
                res[indices[i]] = targets[i]
                for j in range(indices[i]+1,indices[i]+len(sources[i])):
                    res[j] = ""
        #print("Result is:-", res)
        return "".join(res)
