class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r,c = len(strs), len(strs[0])
        result = 0

        for i in range(c):
            for j in range(1,r):
                if strs[j][i] < strs[j-1][i]:
                    result += 1
                    break
        
        return result

#Time Complexity: O(n*m)
#Space Complexity: O(1)