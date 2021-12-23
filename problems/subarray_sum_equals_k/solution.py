class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # LIS modeled solution
        # O(n^2) solution:
        # [1,1,1], k = 2
        # [1,1]
        #   [1,1]
        # result: 2
        
        # [1,2,3], k = 3
        # [1,2]
        #     [3]
        # result: 2
        
        # for i = 0 -> n - 1
        #    for j = 0 -> i-1
        #        if sum from j to i == k, increment total
        
        # Hashmap
        # O(n) solution
        # {
        #  sum: occurrences of sum
        #
        # }
        #
        #
        #
        lookup = defaultdict(int)
        lookup[0] = 1  # always a sum of 0
        n = len(nums)
        running_sum = 0
        result = 0
        for num in nums:
            running_sum += num
            if running_sum - k in lookup:
                # defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1})
                # k = 2
                #    [1,1,1]  lookup[3-k] = lookup[3-2] = lookup[1] = 1
                result += lookup[running_sum - k]
            lookup[running_sum] += 1
            
        return result
            
            
                    
        
        
        
        