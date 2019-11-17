class Solution:
    def getTotal(self, n):
        total = 0
        while n > 0:
            n, rem = divmod(n, 10)
            total += rem**2
        return total
            
    
    def isHappy(self, n: int, last_num=None) -> bool:
        
        nums_seen = set()
        while n != 1 and n not in nums_seen:
            nums_seen.add(n)
            n = self.getTotal(n)
            
        return n == 1
        