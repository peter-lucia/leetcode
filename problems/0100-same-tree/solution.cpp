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
    vector<pair<int,int>> bfs(TreeNode* node) {
        // bfs uses a queue,
        // nodes are processed left to right
        // return level-order traversal with value and its vertical position
        // to enable simple comparison

        if (node == nullptr)
            return {};

        vector<pair<int, int>> result;

        deque<pair<TreeNode*, int>> queue;
        queue.push_back({node, 0});

        while (!queue.empty()) {
            pair<TreeNode*, int> p = queue.front();
            queue.pop_front();
            result.push_back({p.first->val, p.second});

            // insert left first to process left to right
            if (p.first->left)
                queue.push_back({p.first->left, p.second-1});
            if (p.first->right)
                queue.push_back({p.first->right, p.second+1});
        }
        return result;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        // do bfs (level order) traversal of each tree
        // build a vector<int> for each level
        // check each level for differences
        vector<pair<int, int>> p_order = bfs(p);
        vector<pair<int, int>> q_order = bfs(q);
        if (p_order.size() != q_order.size())
            return false;
        for (int i = 0; i < p_order.size(); i++) {
            pair<int, int> pp = p_order[i];
            pair<int, int> pq = q_order[i];
            if (pp.first != pq.first)
                return false;
            if (pp.second != pq.second)
                return false;
        } 
        return true;
    }
};
