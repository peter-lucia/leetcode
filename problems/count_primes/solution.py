class Solution:
    def countPrimes(self, n: int) -> int:
        """
        O(sqrt(n) log(log(n))) Time
        O(n) space 
        """
        if n <= 2:
            return 0
        
        composites = set()
        for i in range(2, int(sqrt(n))+1):
            if i not in composites:
                for multiple in range(i*i, n, i):
                    composites.add(multiple)
        # exclude '1' and the number itself
        return n - len(composites) - 2
                