class Solution:
    def reverse(self, x: int) -> int:
        # detect if x is negative
        # convert digits of x excluding negative sign to a string
        # reverse those elements of the string
        # cast back to an integer
        
        neg = x < 0
        digits = str(abs(x))
        result = ""
        for digit in digits:
            result = digit + result
        result = int(result)
        if neg:
            result *= -1
        if -2**31 <= result <= 2**31-1:
            return result
        return 0
        
            