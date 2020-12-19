class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        
        tot=0
        t=0
        for i in range(n-1,-1,-1):
            tot+=int(num1[i])*10**t
            t+=1
            
        t=0
        for i in range(m-1,-1,-1):
            tot+=int(num2[i])*10**t
            t+=1
        return str(tot)