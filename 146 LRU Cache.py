class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1  
        val = self.store.pop(key)  #Remove it first before inserting it at the end again
        self.store[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.store:    
            self.store.pop(key)
        else:
            if len(self.store) == self.capacity:
                del self.store[next(iter(self.store))]     #Delete the first element
        self.store[key] = value
        
        
x = ["1","2","-7","15","300"]
y = sorted(x)
print("y:",y)
#Implementation detail of line 19: To iterate the dictionary keys, I chose to use a generator object 
# to simply generate a single key: next(iter(self.cache)), which is equivalent to list(self.cache.keys())[0] or self.cache.items()[0][0]. 
# The reason behind doing this is because we can avoid a little bit of overhead required to generate a whole list of keys,
#  which can be more time-consuming when capacity is large; i.e. generate one key O(1) versus a whole list of keys O(k).

#Beginning with Python 3.7, Dictionary objects naturally store key-value pairs in the order of key insertion.
#  So we can very easily identify the least recently used item with a single iteration of the dictionary keys,
#  i.e. one can treat dictionary keys like a stack and the first key is the least-recently-used as long as we always
#  replace accessed keys back to the top of the stack.

#Another approach is to use OrderedDict from collections module.
# OrderedDict is a dictionary subclass that remembers the order that keys were first inserted.
# The only difference between dict() and OrderedDict() is that: 
# A regular dict doesn’t track the insertion order, and iterating it gives you the values in an arbitrary order.
# By contrast, the OrderedDict remembers the order keys were first inserted. 
# When iterating an ordered dictionary, the items are returned in the order their keys were first added.
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
# The pairs are returned in LIFO order if last is true or FIFO order if false.

# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.dict = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.dict:
#             return -1
#         self.dict.move_to_end(key)
#         return self.dict[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.dict:
#             self.dict.pop(key)
            
#         self.dict[key] = value
#         if len(self.dict) > self.cap:
#             self.dict.popitem(last=False) 