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

#O(1) solution
class RandomizedSet:

    def __init__(self):
        
        self.store = {}
        self.arr = []        

    def insert(self, val: int) -> bool:
        
        if val not in self.store:
            self.store[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        
        if(val not in self.store):
            return False
        index = self.store[val]
        self.store[self.arr[-1]] = index
        self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
        self.arr.pop()
        self.store.pop(val)
        return True

    def getRandom(self) -> int:        
        return random.choice(self.arr)

## APPROACH : HASHMAP ##
#   1. Insertion operation in list is O(1) but not deletion
#   2. So we create one Hashmap with key,index and other list
#   3. for deleting we go to hashmap, get index, go to that index in list, swap that element with last element.
#   4. save the index to last element in hashmap and delete list last element