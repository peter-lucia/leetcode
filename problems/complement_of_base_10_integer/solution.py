class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit_length = n.bit_length()    # e.g. num = 5, bit_length = 3
        if n == 0:
            return 1
        mask = (1 << bit_length) - 1
        return mask ^ n
                
        