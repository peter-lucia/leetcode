class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [c for c in num1]
        num1.reverse()
        num2 = [c for c in num2]
        num2.reverse()
        num1_int = 0
        i = 0
        for c in num1:
            num1_int += (10**i)*int(c)
            i += 1
        num2_int = 0
        i = 0
        for c in num2:
            num2_int += (10**i)*int(c)
            i += 1
        
        return str(num1_int * num2_int)