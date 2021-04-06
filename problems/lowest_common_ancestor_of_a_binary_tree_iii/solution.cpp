/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        // search upwards from p and q, adding each found node to a set
        // if the node being added that is reachable from either p or q already exists in the set
        // then we have found the lowest common ancestor
        
        std::unordered_set<Node*> parents = {};
        
        Node* s = p;
        Node* t = q;
        while (s != nullptr || t != nullptr) {
            if (s != nullptr) {
                if (parents.find(s) != parents.end())
                    return s;
                parents.insert(s);
                s = s->parent;
            }
            if (t != nullptr) {
                if (parents.find(t) != parents.end())
                    return t;
                parents.insert(t);
                t = t->parent;
            }
        }
        return nullptr;
    }
};