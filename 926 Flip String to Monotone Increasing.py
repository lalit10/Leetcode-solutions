class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        result, ones = 0,0

        for no in s:
            if no =="1":
                ones+=1
            elif ones:
                ones-=1
                result+=1
        return result

# Time Complexity:  O(n)
# Space Complexity: O(1)