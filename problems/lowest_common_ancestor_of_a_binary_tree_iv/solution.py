# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # put the nodes in a set
        nodes = set(nodes)
        
        
        def explore(root):
            # no more paths to explore
            if root is None:
                return root
            
            # if root is in the nodes then going lower would exlclude root so we return root
            if root in nodes:
                return root
            
            # get the lowest common ancestor for the left side of the tree
            left = explore(root.left)
            
            # get the lowest common ancestor for the right side of the tree
            right = explore(root.right)
            
            # if a LCA exists for both the left and right sides, root is the LCA for all nodes below here
            if left is not None and right is not None:
                return root
            # here and below either left is None or right is None
            # so return whichever side is not None as the LCA
            if left is not None:
                return left
            if right is not None:
                return right
            
        return explore(root)