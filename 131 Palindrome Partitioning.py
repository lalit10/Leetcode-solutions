class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(currList, k):
            if k == len(s):
                result.append(currList)
                return

            for i in range(k, len(s)):
                temp = s[k:i + 1]
                if temp == temp[::-1]:
                    dfs(currList + [temp], i + 1)

        dfs([], 0)
        return result

#Approach: Backtracking