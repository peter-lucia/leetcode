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

    int maxDepth(TreeNode* root) {

        if (root == nullptr) {
            return 0;
        }

        deque<pair<TreeNode*, int>> stack;
        stack.push_back({root, 0});

        int currentLevel = 1;
        while (!stack.empty()) {

            pair<TreeNode*, int> p = stack.front();
            stack.pop_front();
            TreeNode* node = p.first;
            currentLevel = max(currentLevel, p.second);

            if (node->left != nullptr) {
                stack.push_back({node->left, currentLevel+1});
            }
            if (node->right != nullptr) {
                stack.push_back({node->right, currentLevel+1});
            }

        }

        return currentLevel;
    }
};
