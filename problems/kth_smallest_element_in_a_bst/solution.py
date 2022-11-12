# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Use in order traversal to go through each elements in sorted order
        The kth element found will be the one we want
        """

        self.num_elems = 0
        def dfs(node: TreeNode):

            if not node:
                return

            if node.left:
                res = dfs(node.left)
                if res is not None:
                    return res
            self.num_elems += 1
            if self.num_elems == k:
                return node.val
            if node.right:
                res = dfs(node.right)
                if res is not None:
                    return res

        return dfs(root)