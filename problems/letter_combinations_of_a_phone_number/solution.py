class Solution:

    def __init__(self):
        self.lookup = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        
        """In backtracking, we use recursion to explore all the possibilities
        until we get the best result for the problem."""
        
        result = []
        def backtrack(combinations, remaining_digits):
            if len(remaining_digits) == 0:
                result.append(combinations)
            else:
                for letter in self.lookup[int(remaining_digits[0])]:
                    backtrack(combinations + letter, remaining_digits[1:])
        
        if digits:
            backtrack("", digits)

        return result
                    

        