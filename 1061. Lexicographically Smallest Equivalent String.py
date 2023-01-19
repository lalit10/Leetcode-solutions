class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        store = {i: i for i in ascii_lowercase}

        def parent(x):
            if store[x] == x: 
                return x
            x = parent(store[x])
            return x
        
        def union(x, y):
            u, v = parent(x), parent(y)
            store[u] = store[v] = min(u, v)
        
        for a, b in zip(s1, s2):
            union(a, b)
        
        return ''.join([parent(i) for i in baseStr])