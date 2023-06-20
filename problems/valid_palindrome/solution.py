class Solution:
    def isPalindrome(self, s: str) -> bool:
      # two pointers start 
      # at beginning and end
      # move inward as long
      # as the values are equal
      i = 0
      s = s.lower()
      s = "".join([
        c for c in s 
        if c in
        "abcdefghijklmnopqrstuvwxyz0123456789"

      ])
      j = len(s) -1
      while i <= j:
        if not s[i] == s[j]:
          return False
        i +=1
        j -=1
      return True
      
        