import random
class RandomizedSet:

    def __init__(self):
        self.store = {}

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.store[val] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        else:
            del self.store[val]
            return True
        

    def getRandom(self) -> int:
        return random.choice(list(self.store.keys()))
        
#Need to confirm the complexity of each function


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()