class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #No of zeros divided by 2 and store that index
        #Look for edge cases like end/start seats

        no = len(seats)
        empty,result,a,b = 0,0,-1,-1

        for i in range(no):
            if seats[i] ==1:
                empty = 0
                if a==-1:
                    a=i
                b=i
            else:
                empty+=1
                result = max(result,(empty+1)//2)
        result = max(result,a,no-1-b)  # Yeh edge cases ke liye
        #print("Result is:-", result)
        return result
