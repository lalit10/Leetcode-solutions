class Solution:
    def nextClosestTime(self, time: str) -> str:
        h,m  = time.split(":")
        h,m = int(h), int(m)
        #print(h,m)
        digits = [int(i) for i in time if i.isdigit()]
        #print(digits)
        
        while True:
            m += 1
            if m >= 60:
                h += 1
                m = m % 60
                if h >= 24:
                    h = h % 24
            if all([x in digits for x in [h%10, m%10, h//10, m//10]]):
                #return str(h)+":"+str(m)  Important because if you do this, you will get 1:1 instead of 01:01, missed a test case
                return f'{h:02d}:{m:02d}'
        #print(h,m)

        