class Solution:
    def intToRoman(self, num: int) -> str:
        
        # key points
        
        # Create hash table of symbols mapping value to the symbol
        # 1: 'I'
        # 5: 'V'
        # ...
        
        # Convert num to str, handle each digit individually
        # If 4 or 9 * 10^x is found, handle it separately
        # otherwise, use a separate function to determine sum of each digit
        
        # Procedure: Iterate over each digit from right to left
        # i = 0
        # for each digit (right to left)
        #   if digit is 4 or 9: special handling
        #   otherwise, use function
        #   i += 1
        
        lookup = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        
        digits = [c for c in str(num)][::-1]
        i = 0
        result = ""
        while i < len(digits):
            tens_mult = 10**i
            digit = int(digits[i])*tens_mult
            if digits[i] in ['4', '9']:
                # ...4... = "I" + "V" + existing result
                result = (self.get_symbols(tens_mult, lookup) 
                        + self.get_symbols(int(digit) + tens_mult, lookup) 
                        + result)
            else:
                result = self.get_symbols(int(digit), lookup) + result
            i += 1
                
        return result
                
    def get_symbols(self, num: int, lookup: dict) -> str:
        """
        Recursively find the largest symbol where remainder is >= 0 until remainder is 0
        
        Assumes 4 and 9 are not present
        
        Example:  
            subtract value of symbol, add symbol to result, keep going until
            remainder is 0

            Start with 27
            largest symbol where remainder is >= 0 is X
            27 - lookup[X] = 27-10 = 17

            17
            largest symbol where remainder is >= 0 is X
            17 - 10 = 7

            7
            largest symbol where remainder is >= 0 is V
            7 - 5 = 2

            2
            largest symbol where remainder is >= 0 is I
            2 - 1 = 1

            1
            largest symbol where remainder is >= 0 is I
            1 - 1 = 0 -> we are done
            XXVII = 27
        """
        ks = list(lookup.keys())
        result = ""
        while num > 0:
            # get last key that's just less than the num
            i = bisect.bisect(ks, num) - 1
            result += lookup[ks[i]]
            num -= ks[i]
        return result
                    
        
        