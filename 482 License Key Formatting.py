class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:        
        s = s.replace('-', '')        
        k =int(k)
        rem = len(s) % k        
        store = []
        if rem:
            store.append( s[:rem] )
                    
        for i in range(rem, len(s), k ):
            store.append(s[i:i+k])
        
        return '-'.join(store).upper()

# Time Complexity: O(n)
# Space Complexity: O(n)

#Another solution:

# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         s_without = s.replace('-', '')
#         len_new = len(s_without)
#         k = int(k)
#         result = "" 
#         if len_new % k == 0:
#             for i in range(0,len_new,k):
#                 result = result + s_without[i:i+k] + "-"
#         else:
#             result = result + s_without[0:len_new % k] + "-"
#             for i in range(len_new % k, len_new,k):
#                 result = result + s_without[i:i+k] + '-'        
#         return result[0:len(result)-1].upper()