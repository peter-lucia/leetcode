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
    int _sum = 0;
private:
    void getSumOfLeftLeaves(const TreeNode* root) {
        
        if (root != nullptr) {
            if (root->left != nullptr) {
                if (root->left->left == nullptr && root->left->right == nullptr)
                    _sum += root->left->val;
                getSumOfLeftLeaves(root->left);
            } 
            if (root->right != nullptr) {
                getSumOfLeftLeaves(root->right);
            }
        }
    }
public:
    int sumOfLeftLeaves(TreeNode* root) {
        /*
            3       sum = 0
           / \
          9  20     sum = 9
            /  \
           15   7   sum = 9+15 = 24
            
        */
        
        getSumOfLeftLeaves(root);
        return _sum;    
            
    }
};