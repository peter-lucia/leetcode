class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # get cum product left to right
      # get cum profuct right to left
      # for each i, mult arr[i-1]*arr[i+1]
      a = nums
      n = len(a)
      s = 1
      lr = []
      for i in range(n):
        s *= a[i]
        lr.append(s)

      s = 1
      rl = []
      for i in range(n-1,-1,-1):
        s*=a[i]
        rl.append(s)
      rl.reverse()

      return [rl[1]]+[
        lr[i-1]*rl[i+1]
        for i in range(1,n-1)
      ]+[lr[-2]]


        