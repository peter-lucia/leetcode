# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def bfs(visited: List[TreeNode], node: TreeNode):
            queue = []
            depth = 1
            queue.append((node, depth))

            while queue:
                # if neighbor is not visited, add it to the queue
                elem, depth = queue.pop(0)
                visited.append(elem)

                if elem.left is None and elem.right is None:
                    return depth

                if elem.left and elem.left not in visited:
                    queue.append((elem.left, depth + 1))
                if elem.right and elem.right not in visited:
                    queue.append((elem.right, depth + 1))
        visited = []
        min_depth = bfs(visited, root)
        return min_depth


