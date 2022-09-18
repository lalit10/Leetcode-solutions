from collections import Counter
class Solution:
      def minSteps(self, s: str, t: str) -> int:
        s_arr = Counter(s)  # s_arr is a dictionary with key as the character and value as the count of the character
        result = 0
        for char in t:  # Iterate through the characters in t
            if s_arr[char] > 0: 
                s_arr[char] -= 1
            else:
                result += 1
        return result