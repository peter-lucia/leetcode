class Solution:
    def maxArea(self, height: List[int]) -> int:
      # track max area int
      # left and right pointers, i, j
      # if hs[i] < hs[j], i +=1
      # otherwise, j-= 1
      # at each step calc max area

      i = 0
      hs = height
      j = len(hs)-1
      ma = 0
      while i < j:
        a = min(
          hs[i],
          hs[j]
        ) * (j-i)
        ma = max(
          ma,
          a
        )
        if hs[i] < hs[j]:
          i += 1
        else:
          j -= 1
      return ma

          