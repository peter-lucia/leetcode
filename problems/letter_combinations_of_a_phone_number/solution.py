class Solution:
    
    def get_combos(self, list1, list2, size):
        result = set()
        for each in list1:
            for each2 in combinations(list2, size-1):
                result.add("{0}{1}".format(each, "".join(each2)))
        return list(result)
        
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            "1": [],
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"],
        }
        
        if len(digits) == 1:
            return lookup[digits]
        elif len(digits) == 2:
            return self.get_combos(lookup[digits[0]], lookup[digits[1]], 2)
        elif len(digits) == 3:
            combos = self.get_combos(lookup[digits[0]], lookup[digits[1]], 2)
            return self.get_combos(combos, lookup[digits[2]], 2)
        elif len(digits) == 4:
            combos = self.get_combos(lookup[digits[0]], lookup[digits[1]], 2)
            combos = self.get_combos(combos, lookup[digits[2]], 2)
            return self.get_combos(combos, lookup[digits[3]], 2)
        
            
        
        