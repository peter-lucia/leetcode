class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # set contains current
      # slidingwindow chars
      # if duplicate,
      # move left edge
      # otherwise move right
      # edge
      n = len(s)
      if not n:
        return 0
      elif n==1:
        return 1
      i = 0
      r = 0
      while i < n:
        size = 1
        cc = set([s[i]])
        j = i+1
        while j < n:
          if s[j] not in cc:
            cc.add(s[j])
            size += 1
            j += 1
          else:
            break
        i += 1
        r = max(r, size)
      return r

        
          



        