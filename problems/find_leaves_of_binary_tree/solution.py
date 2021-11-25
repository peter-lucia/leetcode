# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
            Example:
                      20                       20               20        20
                    /    \                   /    \           /
                  8       22               8       22       8
                /   \    /   \              \
              5      3  4    25               3
                    / \
                  10    14

        - level 0 nodes: 5, 10, 14, 4, 25
        - level 1 nodes: 3, 22
        - level 2 nodes: 8
        - level 3 nodes: 20
        Output:
        {
            0: [5, 10, 14, 4, 25],
            1: [3, 22],
            2: [8],
            3: [20]
        }
        """
        lookup = collections.defaultdict(list)

        def dfs(node: TreeNode, level: int):
            """
            Gets the maximum depth from the left and right subtrees
            of a given node
            """
            if not node:
                return level
            max_left_level = dfs(node.left, level)
            max_right_level = dfs(node.right, level)
            level = max(max_left_level, max_right_level)
            lookup[level].append(node.val)
            return level + 1
        dfs(root, 0)
        # lookup.values() for defaultdict returns
        # a list of lists for all values
        return lookup.values()
        