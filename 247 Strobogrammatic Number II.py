class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        #store = {"0":"0","1":"1","6":"9","8":"8","9":"6"}

        store = [''] if n%2 ==0 else ["0","1","8"]
        #For odd 0,1,8
        #For others 1,8,6,9

        for i in range(n//2):
            temp = []
            for num in store:
                temp.append("1"+ num + "1")
                temp.append("8"+ num + "8")
                temp.append("6"+ num + "9")
                temp.append("9"+ num + "6")
                if len(num) < n-2:  #To avoid 0 at the start and end
                    temp.append('0' + num + '0')
            store = temp
        print(store)
        return store


#Another solution
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def recursion(n):
            if n== 0:
                return ""
            if n==1:
                return ["0","1","8"]
            if n==2:
                return ["00","11","88","69","96"]
            
            results = []
            
            for i in recursion(n-2):
                results.append("0"+i+"0")
                results.append("1"+i+"1")
                results.append("8"+i+"8")
                results.append("6"+i+"9")
                results.append("9"+i+"6")
            return results
        
        if n==1:
            return ["0","1","8"]
        return[no for no in recursion(n) if no[0]!= "0" and no[-1]!="0"]
