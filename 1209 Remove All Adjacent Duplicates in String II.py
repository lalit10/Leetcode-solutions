class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  #Create a stack to store character and count
        
        for char in s:          
            if stack and stack[-1][0] == char:  #If the top of the stack is the same as the current character, increase the count
                stack[-1][1] += 1
                if stack[-1][1] == k: #If the count is equal to k, pop the top of the stack
                    stack.pop()
            else:
                stack.append([char, 1]) #If the top of the stack is not the same as the current character, add the current character and count to the stack
        
        return ''.join(char * count for char, count in stack)