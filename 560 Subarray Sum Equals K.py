class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] =1
        temp_sum, result =0,0
        for no in nums:
            temp_sum+=no
            result+=store[temp_sum-k]
            store[temp_sum]+=1
        return result

# Time Complexity:  O(n)
# Space Complexity: O(n)