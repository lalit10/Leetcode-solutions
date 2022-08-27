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
                