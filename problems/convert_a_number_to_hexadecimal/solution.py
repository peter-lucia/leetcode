class Solution:
    
    def __init__(self):
        self.lookup = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
           10: "a",
           11: "b",
           12: "c",
           13: "d",
           14: "e",
           15: "f"
        }
    def toHex(self, num: int) -> str:
        num_bits = 32
        if num < 0:
            # Since num is negative, we're doing 2^N - abs(num)
            # https://en.wikipedia.org/wiki/Two%27s_complement
            num += 1 << num_bits
        
        if 0 <= num < 16:
            return self.lookup[num]
        
        result = ""
        while num > 0:
            num, remainder = divmod(num, 16)
            result = self.lookup[remainder] + result
        return result