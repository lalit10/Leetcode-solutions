class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["I","X","C","M"]
        fives = ["V","L","D"]
        
        result = []
        i = 0
        
        while num>0:
            n = num%10
            if 1 <= n <= 3:
                result.append(ones[i]*n)
            elif n ==4:
                result.append(ones[i] + fives[i])
            elif 5 <= n <= 8:
                result.append(fives[i]+ones[i]*(n-5))
            elif n==9:
                result.append(ones[i]+ones[i+1])
            
            i+=1
            num=num //10
        #print("Result is:-", result)
        return "".join(result[::-1])