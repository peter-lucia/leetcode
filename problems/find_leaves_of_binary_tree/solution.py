# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bottom_view_hashmap(self, root, lookup, level, path, parent, is_left, deleted_list):
        
        if root is None:
            return
        
        if path in lookup:
            if level >= lookup[path][1]:
                lookup[path] = [root.val, level]
        else:
            lookup[path] = [root.val, level]
            

        
        if root.left is None and root.right is None:
            deleted_list.append(root.val)
            if is_left:
                parent.left = None
                
            else:
                parent.right = None
            del lookup[path]
            return
        
        self.bottom_view_hashmap(root.left,
                                lookup,
                                level + 1,
                                path + "-left",
                                root,
                                True,
                                deleted_list)
        self.bottom_view_hashmap(root.right,
                                lookup,
                                level + 1,
                                path + "-right",
                                root,
                                False,
                                deleted_list)

        
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
        result = []
        while root:
            deleted_list = []
            self.bottom_view_hashmap(root, lookup, 0, "", root, False, deleted_list)
            result.append(deleted_list)
            if not lookup:
                break
        
        return result
        