class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []  #Stack for history
        self.future = []  #Stack for future
        self.history.append(homepage)  #Append homepage to the history stack

    def visit(self, url: str) -> None:
        self.history.append(url) #Append url to the history stack
        self.future = [] #Empty the future stack

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:  #If there is at least one element in the history stack and the steps is greater than 0
            self.future.append(self.history[-1])  #Append the last element in the history stack to the future stack
            self.history.pop()  #Remove the last element in the history stack
            steps -= 1  #Decrement the steps
        return self.history[-1]  # Return last element in the history stack

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:  #If there is at least one element in the future stack and the steps is greater than 0
            self.history.append(self.future[-1])  #Append the last element in the future stack to the history stack
            self.future.pop()  #Remove the last element in the future stack
            steps -= 1 #Decrement the steps
        return self.history[-1]  #Return last element in the history stack


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)