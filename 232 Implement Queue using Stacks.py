class MyQueue:

    def __init__(self):
        self.store1 = []
        self.store2 = []

    def push(self, x: int) -> None:
        self.store1.append(x)

    def pop(self) -> int:        
        if not self.store2:
            while self.store1:
                self.store2.append(self.store1.pop())
        return self.store2.pop()

    def peek(self) -> int:
        if not self.store2:
            while self.store1:
                self.store2.append(self.store1.pop())
        return self.store2[-1]

    def empty(self) -> bool:
        return len(self.store1) == 0 and len(self.store2) == 0