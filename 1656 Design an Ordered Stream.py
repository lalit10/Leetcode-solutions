class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*(n+1) #Initialize stream with None
        self.ptr = 1# Pointer initialization is 1 instead of 0 as per question description.

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value  #Setting value to stream
        result = [] #Store result
        while self.ptr < len(self.stream) and self.stream[self.ptr]: #While pointer is less than length of stream and stream of that pointer is not None
            result.append(self.stream[self.ptr]) #Append stream of that pointer to result
            self.ptr += 1 #Increment pointer
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)