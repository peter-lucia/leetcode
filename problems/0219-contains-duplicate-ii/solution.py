class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # lookup stores last index at which a number was 
        # last seen
        # if a number has not been seen, add it to lookup
        # if a number has been seen, update q, then update the last seen
        # index in the lookup
        # Example:
        # [1,2,3,1]
        """
        q = math.inf
        1 -> 0, q = math.inf
        2 -> 1, q = math.inf
        3 -> 2, q = math.inf
        1 -> 3, q = abs(3 - 0) = 3

        return q <= k

        """
        lookup = {}
        q = math.inf
        for i, c in enumerate(nums):
            if c not in lookup:
                lookup[c] = i
            else:
                q = min(q, abs(lookup[c] - i))
                lookup[c] = i
        return q <= k

        
        
