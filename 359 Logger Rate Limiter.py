class Logger:

    def __init__(self):
        self.store  ={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.store:
            self.store[message] = timestamp
            return True
        else:
            if timestamp - self.store[message] >=10:
                self.store[message] = timestamp
                return True
            else:
                return False

#Time Complexity: O(1)
#Space Complexity: O(n)

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)