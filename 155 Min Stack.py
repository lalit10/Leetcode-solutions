class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))     

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min[-1]
        

#Time Complexity: O(1)
#Space Complexity: O(n)