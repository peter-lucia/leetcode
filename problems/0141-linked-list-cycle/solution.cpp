/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        map<ListNode*, bool> visited;
        visited.insert({head, true});

        while (head != NULL) {
            head = head->next;
            if (auto it = visited.find(head) != visited.end()) {
                return true;
            }
            visited.insert({head, true});
        }
        return false;
        
    }
};
