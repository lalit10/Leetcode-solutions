class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        no = 0
        for i in num:
            no = (no*10) + i 
        no = no + k
        result = []
        while no:
            rem = no % 10
            result.append(rem)
            no = no // 10
        return result[::-1]