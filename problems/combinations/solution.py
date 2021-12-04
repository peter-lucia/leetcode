class Solution:

    @staticmethod
    def get_all_combinations(nums: List[int], k: int) -> List[List[int]]:
        """
        move left: don't add n to list
        move right: add n to list
        n = 3
                             []                              2^0 combinations
                  /                     \
        1        []                     [1]                  2^1 combinations
                /    \               /        \
        2      []     [2]          [1]        [1,2]          2^2 combinations
              /  \    /  \       /    \       /   \
        3    []  [3] [2] [2,3]  [1]   [1,3] [1,2]  [1,2,3]   2^3 combinations of any size

        n choose k = n! / ((n-k)!*k!)
        """
        if not nums:
            return [[]]

        left_num = nums[0]

        combinations_without_first = Solution.get_all_combinations(nums[1:], k)
        combinations_with_first = []
        for comb in combinations_without_first:
            combinations_with_first.append([left_num] + comb)
        return combinations_without_first + combinations_with_first

    def combine(self, n: int, k: int) -> List[List[int]]:



        all_combs = Solution.get_all_combinations(list(range(1,n+1)), k)
        result = []
        for comb in all_combs:
            if len(comb) == k:
                result.append(comb)
        return result
        
    
        
        
        
        