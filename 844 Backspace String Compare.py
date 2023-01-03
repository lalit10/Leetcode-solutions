class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for i in s:
            if i != '#':
                stack_s.append(i)
            else:
                if stack_s:
                    stack_s.pop()
        #print(stack_s)
        stack_t = []
        for i in t:
            if i != '#':
                stack_t.append(i)
            else:
                if stack_t:
                    stack_t.pop()
        #print(stack_t)
        return stack_s == stack_t
        
#Time Complexity: O(n)
#Space Complexity: O(n)

#Another solution
class Solution:
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1

#Time Complexity: O(n)
#Space Complexity: O(1)