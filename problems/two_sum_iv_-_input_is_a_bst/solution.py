# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getValues(self, root: TreeNode) -> List[int]:
        values = []
        if root.val is not None:
            values += [root.val]
        if root.left:
            values += self.getValues(root.left)
        if root.right:
            values += self.getValues(root.right)
        return values
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        values = self.getValues(root)
        lookup = {}
        
        for i, val in enumerate(values):
            if lookup.get(k-val, False):
                return True
            lookup[val] = lookup.get(val, 0) + 1
        return False
            
            