class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
                
        first = Counter(s[:len(s)//2])
        second = Counter(s[len(s)//2:])        
       
        sum_first_half = sum(first[v] for v in vowels)
        sum_second_half = sum(second[v] for v in vowels)
        
        return sum_first_half == sum_second_half

#Another solution
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         vowels = set('aeiouAEIOU')
#         first,second = 0,0
#         for i in range(len(s)//2):
#             if s[i] in vowels:
#                 first+=1
#             if s[len(s)//2 + i] in vowels:
#                 second+=1
#         return first==second
        