class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      # create dict mapping
      # num -> true / false
      # true if next num is
      # in the table, false
      # otherwise
      if not nums:
        return 0
      t = {}
      for _ in range(2):
        for c in nums:
          if c+1 in t:
            t[c] = True
          else:
            t[c] = False
      r = 1
      ks = set(t.keys())
      while ks:
        k = ks.pop()
        i = 1
        while t.get(k) is True:
          i += 1
          r = max(r, i)
          k += 1
          ks.discard(k)
      return r

      

      
