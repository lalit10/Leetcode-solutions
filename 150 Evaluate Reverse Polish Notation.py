class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in tokens:
            if i in '+-*/':
                a = result.pop()
                b = result.pop()
                if i == '+':
                    result.append(b+a)
                if i == '-':
                    result.append(b-a)
                if i == '*':
                    result.append(a*b)
                if i == "/":
                    result.append(int(float(b)/a))
            else:
                result.append(int(i))
        #print("Result is:", result)
        return result.pop()
                