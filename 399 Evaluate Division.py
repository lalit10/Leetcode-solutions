class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        for (dividend, divisor), value in zip(equations,values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1/value
        
        result = []
        
        for dividend,divisor in queries:
            temp = 0
            if dividend not in graph or divisor not in graph:
                temp = -1.0
            elif dividend == divisor:
                temp = 1.0
            else:
                visited = set()
                temp = self.evaluate(dividend, divisor, 1, visited, graph)
            result.append(temp)
        return result
    
    def evaluate(self, source, target, prod, visited, graph):
        visited.add(source)
        temp = -1.0
        
        neighbours = graph[source]
        
        if target in neighbours:
            temp = prod * neighbours[target]
        else:
            for node, val in neighbours.items():
                if node in visited:
                    continue
                temp = self.evaluate(node, target, prod*val, visited, graph)
                if temp != -1.0:
                    break
        visited.remove(source)
        return temp

# Time Complexity: O(M*N) where M is the number of queries and N is the number of equations
# Space Complexity: O(N))