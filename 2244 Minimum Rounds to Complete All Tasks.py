class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        store = Counter(tasks)
        result = 0
        for val in store.values():
            if val ==1:
                return -1
            elif val%3==1:
                result += val//3 +1
            elif val%3==2:
                result+= val//3 +1
            elif val%3==0:
                result+= val//3
            else:
                result += val//2
        return result
            