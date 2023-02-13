class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = (high - low) //2
        result = 0
        if high %2==1:
            result+=1
        if low%2==1:
            result+=1
        if high%2==1 and low%2==1:
            result-=1
        result+=diff
        return result