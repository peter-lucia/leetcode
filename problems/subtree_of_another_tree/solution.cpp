/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    bool leftEqualsRight(const TreeNode  *s, const TreeNode *t)
    {
        // both s and t are null
        if (s == nullptr && t == nullptr)
            return true;
        // either s or t is null
        if (s == nullptr || t == nullptr)
            return false;
        // if s's val and t'val are equal and the left and right sides are equal, return true
        return s->val == t->val && leftEqualsRight(s->left, t->left) && leftEqualsRight(s->right, t->right);
    }
    
    bool isSubtree(TreeNode* s, TreeNode* t) {
        // if s is empty, t cannot be a subtree of it
        if (s == nullptr)
            return false;
        // if the left side of s equals the right side of t, return true
        if (leftEqualsRight(s,t))
            return true;
        // if the left side of s has a subtree equal to t return true
        // if the right side of s has a subtree equal to t return true
        return (isSubtree(s->left, t) || isSubtree(s->right, t));
    }
};