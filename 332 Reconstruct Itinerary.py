class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Create graph
        store = defaultdict(list)
        
        for src, dest in tickets:
            store[src].append(dest)
        
        for key in store:
            # Sort children list in descending order so that we can pop last element 
            # instead of pop out first element which is costly operation
            store[key].sort(reverse = True)
            
        stack = []
        result = []
        stack.append("JFK")
        
        # Start with JFK as starting airport and keep adding the next child to traverse 
        # for the last airport at the top of the stack. If we reach to an airport from where 
        # we can't go further then add it to the result. This airport should be the last to go 
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traverse it's children
        while len(stack) > 0:
            elem = stack[-1]
            if elem in store and len(store[elem]) > 0: 
                stack.append(store[elem].pop())
            else:
                result.append(stack.pop())
        
        return result[::-1]
        