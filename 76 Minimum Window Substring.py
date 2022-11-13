from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        i,j =0,0     
        start_window, end_window = 0 , len(s) + 1
        t_dic = Counter(t)
        count = len(t_dic)
        min_string = ''
        
        while j < len(s):
            if s[j] in t_dic:
                t_dic[s[j]]-=1
                if t_dic[s[j]] ==0:
                    count-=1
            if count >0:
                j+=1
            elif count == 0:
                while count ==0:
                    if (j-i+1) < end_window:
                        end_window = j-i+1
                        min_string = s[i:j+1]
                        start_window = i
                    if s[i] in t_dic:
                        t_dic[s[i]] += 1
                        if t_dic[s[i]] == 1:
                            count += 1
                    i+=1
                j+=1
        if end_window == len(s)+1:
            return ""
        else:
            return min_string  # s[start_window: start_window + end_window]

class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
            if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
            target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while target_len==0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window
                