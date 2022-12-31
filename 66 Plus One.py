class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no = 0
        for i in range(len(digits)):
            no += (digits[i] * pow(10, (len(digits)-i-1)))
        #print("No is:", no)
        return [int(i) for i in str(no+1)]

#Another solution:

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         length = len(digits) - 1
#         while digits[length] == 9:
#             digits[length]=0
#             length-=1
#         if length <0:
#             digits = [1]+ digits
#         else:
#             digits[length] +=1
#         return digits