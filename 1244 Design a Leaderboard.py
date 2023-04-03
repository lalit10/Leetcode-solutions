class Leaderboard:

    def __init__(self):
        self.store = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.store:
            self.store[playerId] = score
        else:
            self.store[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.store.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.store[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)