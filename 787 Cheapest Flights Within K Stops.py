class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #BFS se hona chahiye
        graph = defaultdict(list)
        dist =  [-1] * n
        for f, to, price in flights:
            graph[f].append([to, price])

        dist[src], q, step = 0, deque([src]), 0

        while q and step <= k:
            temp = len(q)
            new_dist = list(dist)
            for _ in range(temp):
                cur = q.popleft()
                for neighbor in graph[cur]:
                    if new_dist[neighbor[0]] == -1 or new_dist[neighbor[0]] > dist[cur]+neighbor[1]:
                        new_dist[neighbor[0]] = dist[cur] + neighbor[1]
                        q.append(neighbor[0])
            step += 1
            dist = new_dist

        return dist[dst]


# Time Complexity: O(n)
# Space Complexity: O(n)