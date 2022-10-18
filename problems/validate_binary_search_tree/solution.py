# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(node: TreeNode, lower_bound: int, upper_bound: int) -> bool:

            if not (lower_bound < node.val < upper_bound):
                return False

            left_okay = True
            right_okay = True
            
            if node.left:
                left_okay = dfs(node.left, lower_bound, node.val)

            if node.right:
                right_okay = dfs(node.right, node.val, upper_bound)

            return left_okay and right_okay

        return dfs(root, -math.inf, math.inf)





