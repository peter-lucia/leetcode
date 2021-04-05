class SparseVector:
    def __init__(self, nums: List[int]):
        self.lookup = {}
        self.size = len(nums)
        for idx, num in enumerate(nums):
            if num != 0:
                self.lookup[idx] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for idx in range(vec.size):
            if self.lookup.get(idx, None) is not None and vec.lookup.get(idx, None) is not None:
                result += self.lookup.get(idx) * vec.lookup.get(idx)

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)