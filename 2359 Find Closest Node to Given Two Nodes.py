class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        # run bfs on both nodes
        # record the min distance using store1 and store2
        def bfs(root, cost):
            queue = deque([(root, 0)])
            seen = {root} # to mark visited nodes
            while queue:
                node, step = queue.popleft()
                cost[node] = min(cost[node], step) # record min distance between root and node
                if edges[node] != -1 and edges[node] not in seen:
                    seen.add(edges[node])
                    queue.append((edges[node], step + 1))
        store1 = [math.inf]*n 
        store2 = [math.inf]*n
        bfs(node1, store1)
        bfs(node2, store2)
        # calculate the max of the two distances
        # find the minimum among them and return the node value
        ans = -1 # initialise with -1 so if there is no possible answer, return -1
        cost = math.inf
        for i in range(n):
            if cost > max(store1[i], store2[i]):
                cost = max(store1[i], store2[i])
                ans = i
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)