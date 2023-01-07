class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0
        for price in costs:
            if price<=coins:
                result += 1
                coins -= price
            else:
                break
        return result

#Time Complexity: O(nlogn)
#Space Complexity: O(1)