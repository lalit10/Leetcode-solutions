class Solution:
    def removeDuplicateLetters(self, s: str) -> str:        
        
        stack = []
        seen = set()
        store = {}
        for i in range(len(s)):
            store[ s[i] ] = i
        
        # print(store)
        
        for i, ch in enumerate(s):
            if( ch in seen ):
                continue
            else:
                # 3
                while( stack and stack[-1] > ch and store[stack[-1]] > i ):
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                seen.add(ch)
                stack.append(ch)
            # print(stack)
        return ''.join(stack)

        ## LOGIC ##
		#	1. We add element to the stack
		#	2. IF we get bigger element, we just push on top
		#	3. ELSE we pop if and only if there are other occurances of same letter again in the string, otherwise we donot pop
		#	4. If an element is already in the stack, we donot push.
		## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
	
		## EXAMPLE : "cdadabcc"	##
		## STACK TRACE ##
        # {'c': 7, 'd': 3, 'a': 4, 'b': 5}
        # ['c']
        # ['c', 'd']
        # ['a']
        # ['a', 'd']
        # ['a', 'd', 'b']
        # ['a', 'd', 'b', 'c']