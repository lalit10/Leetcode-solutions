class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        store = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        i,j = 0, len(num)-1

        while i<=j:
            #print(num[i], store[num[i]], num[j])
            if num[i] in store and store[num[i]]== num[j]:
                i+=1
                j-=1
            else:
                return False
        return True

#Time Complexity: O(n)
#Space Complexity: O(1)