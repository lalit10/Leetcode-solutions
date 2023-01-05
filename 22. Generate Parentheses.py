class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Add ")" only after length of "(" has increased

        def dfs(left, right, stack):

            if len(stack) == n*2:
                #print("Stack is:-",stack)
                result.append(stack)
                return

            if left < n:
                dfs(left+1, right, stack + "(")
            
            if right < left:
                dfs(left, right+1, stack+ ")")
        result = []
        dfs(0,0,"")
        return result
