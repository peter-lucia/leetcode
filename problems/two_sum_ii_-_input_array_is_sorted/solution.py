class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      # left pointer, i
      # right pointer, j
      # if nums[i] + nums[j] > target
      # decrease j
      # elif nums[i] + nums[j] < target
      # increase i
      # ensures the smallest increase
      # or decrease at each step
      i = 0
      ns = numbers
      j = len(ns) - 1
      while i < j:
        if ns[i] + ns[j] > target:
          j -= 1
        elif ns[i] + ns[j] < target:
          i += 1
        else:
          return [i+1,j+1]
      return [-1,-1]

        