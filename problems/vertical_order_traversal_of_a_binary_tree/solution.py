# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Keys in the lookup are the horizontal distances
        # need horizontal distance
        # need level

        lookup = defaultdict(list)

        def dfs(root: TreeNode, level: int, hd: int):
            if root is None:
                return

            # since we sort the nodes at the end, pre-order, inorder, or post-order doesn't matter
            lookup[hd].append((root.val, level))
            dfs(root.left, level + 1, hd - 1)
            dfs(root.right, level + 1, hd + 1)
        dfs(root, 0, 0)

        # sort the values
        result = []
        # ensure horizontal distances are in sorted order increasing
        # this ensures the order of columns is returned from left to right
        keys = sorted(lookup.keys())
        for key in keys:
            # ensure the nodes higher up in the tree for a single column come first
            # before nodes lower in the tree
            rw = sorted(lookup[key], key=lambda val: (val[1], val[0]))  # increasing
            rw = [a[0] for a in rw]
            result.append(rw)
        return result
        