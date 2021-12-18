class Solution:
    def originalDigits(self, s: str) -> str:
        # approach
        
        # create a list of numbers 0-9 in english
        
        # zero - number of z's since it's the only one that has a z
        # one - number of o's minus counts for others with an o: zero, two, four
        # two - number of w's
        # three - number of t's minus counts for others with a 't': two and eight
        # four - number of u's
        # five - number of f's minus count for others with f: four
        # six - number of x's
        # seven - number of s's minus count for others with s: six
        # eight - number of g's
        # nine - number of i's minus count for others with i: eight: six, five
        
        # build {'a': 1, 'b': 2, 'c': 3}
        lookup = Counter(s)
        
        result = ""
        result += "0"*(lookup['z'])
        result += "1"*(lookup['o'] - lookup['z'] - lookup['w'] - lookup['u'])
        result += "2"*(lookup['w'])
        result += "3"*(lookup['t'] - lookup['w'] - lookup['g'])
        result += "4"*(lookup['u'])
        result += "5"*(lookup['f'] - lookup['u'])
        result += "6"*(lookup['x'])
        result += "7"*(lookup['s'] - lookup['x'])
        result += "8"*(lookup['g'])
        result += "9"*(lookup['i'] - lookup['g'] - lookup['x'] - (lookup['f'] - lookup['u']))
        
        return result
        
        
        