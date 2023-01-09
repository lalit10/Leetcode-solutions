def longestPalindrome(self, s):
        longest_palindrom = (0, 1)
        dp = [[0]*len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  # if the chars matches
                    # if len sliced sub_string is just one letter if the characters are equal, we can say they are palindome dp[i][j] =True 
                    # if the sliced sub_string is longer than 1, then we should check if the inner string is also palindrome (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrome sequence 
                        if longest_palindrom[1] - longest_palindrom[0] < j - i + 1:
                            longest_palindrom = (i, j+1)
                
        return s[longest_palindrom[0]:longest_palindrom[1]]

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

#https://leetcode.com/problems/longest-palindromic-substring/solutions/900639/python-solution-with-detailed-explanation-using-dp/?orderBy=most_votes&languageTags=python3