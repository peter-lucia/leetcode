class Solution:
    def sweep(self, arr, idx):
        result = []

        arr = arr.copy()
        val = arr.pop(idx)
        if val == ")":
            pos = idx
            while pos < len(arr):
                arr.insert(pos, val)
                result.append(arr.copy())
                arr.pop(pos)
                pos += 1
        elif val == "(":
            pos = idx
            while pos >= 0:
                arr.insert(pos, val)
                result.append(arr.copy())
                arr.pop(pos)
                pos -= 1
        return result

    def get_results_for_base(self, base, result):
        for idx in range(0, len(base)):
            temp = self.sweep(base, idx)
            for each in temp:
                result.add("".join(each))

        return result

        
    def generateParenthesis(self, n: int) -> str:
        # move each pair of left and right parentheses
        # to the left edge and to the right edge from the
        # base case until all combinations have been formed
        
        """
        ()()()()
        (())()()
        (()())()
        """
        result = set()
        base = "()"*n
        result.add("("*n+")"*n)
        base = list(base)
        result = self.get_results_for_base(base, result)
        while True:
            new_results = set()
            for each in list(result):
                base = list(each)
                new_results = self.get_results_for_base(base, new_results)

            if result.issuperset(new_results):
                break
            else:
                result = result.union(new_results)
        return list(result)

if __name__ == '__main__':
    s = Solution()
    result = s.generateParenthesis(3) 
    print(result)
    assert set(result) == set(["((()))","(()())","(())()","()(())","()()()"])

    result = s.generateParenthesis(4) 
    print(result)
    assert set(result) == set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])