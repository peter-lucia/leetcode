class Solution:

    def __init__(self, nums: List[int]):
        self.original = copy.deepcopy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        # https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
        # Time complexity: O(n)
        # Space complexity: O(n)
        for i in range(len(self.nums)):
            j = random.randint(0, len(self.nums)-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()