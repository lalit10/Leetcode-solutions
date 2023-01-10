def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        
        left = 0
        max_length = 0
        
        store = {i: 0 for i in s}
        
        for i in range(len(s)):
            
            store[s[i]]+=1
            while store[s[i]] > 1:
                left +=1
                store[s[left-1]]-=1   #Modified from i to left-1  because we are moving left pointer
            length = i -left + 1
            
            max_length = max(length, max_length)
        
        return max_length
# Time Complexity: O(N)
# Space Complexity: O(N)

#Another solution:

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) ==0:
#             return 0
#         result = float('-inf')
#         store = defaultdict(int)
#         i,j= 0, 0
#         length = 0
#         while j < len(s):
#             curr = s[j]
#             store[curr]+=1            
#             while store[curr]>1:
#                 store[s[i]] -=1
#                 i+=1
#             length =j-i+1
#             result =max(result,length)
#             j+=1
#         return result

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         ans = 0
#         if len(s) == 0:
#             return ans
#         seen = set()
#         l = 0
#         for r in range(len(s)):
#             while s[r] in seen:
#                 seen.remove(s[l])
#                 l += 1
#             seen.add(s[r])
#             ans = max(ans, r-l+1)
#         return ans
                    