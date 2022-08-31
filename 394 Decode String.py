class Solution:
    def decodeString(self, s: str) -> str:
        # Two stacks: one for string and another for number
        string_stack = []
        num_stack = []
        
        #Strings to store number and other one to store the decoded string. 
        tempNum = ''
        result = ''        
        
        # start iterating throught the encoded string
        for char in s:
            # check if the char is a digit. 
            if char.isdigit():
                tempNum += char # add the number to tempNum
                
            # check if the char is an opening bracket
            elif char == '[':
                string_stack.append(result)
                num_stack.append(tempNum)
                tempNum = ''
                result = ''
                
            # check when the bracket closes
            elif char == ']':
                result = string_stack.pop() + (result * int(num_stack.pop()))
                #print("Result is:-", result)
                
            # else build the substring to repeat
            else:
                result += char            
                
        return result