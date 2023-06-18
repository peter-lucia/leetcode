class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      # make sure there are no duplicates in each row, col, square

      b = defaultdict(list)
      n = len(board)
      m = len(board[0])
      for r in board:
        r1 = [
          v for v in r 
          if v != "."
        ]
        if len(set(r1)) != len(r1):
          return False
        for j in range(n):
          b[j].append(r[j])
      for j in b:
        c1 = [
          v for v in b[j]
          if v != "."
        ]
        if len(set(c1)) != len(c1):
          return False

      for i in [0,3,6]:
        for j in [0,3,6]:
          e = []
          for ii in range(3):
            for jj in range(3):
              v = board[i+ii][j+jj]
              if v != ".":
                e.append(v)
          if len(e) != len(set(e)):
            return False
      
      return True



      

      

        