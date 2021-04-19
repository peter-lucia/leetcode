# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, sequence: List[int]) -> bool:
          if root is None and len(sequence) > 0:
              return False
            
          if len(sequence) > 0 and root.val == sequence[0]:
              if len(sequence) == 1 and root.left is None and root.right is None:
                  return True

              return self.isValidSequence(root.left, sequence[1:]) or self.isValidSequence(root.right, sequence[1:])
          return False