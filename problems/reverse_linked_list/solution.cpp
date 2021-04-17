/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
            
        ListNode* tmp_node = nullptr; // when starting next_node 
        ListNode* prev_node = nullptr;
        while (head != nullptr) {
            tmp_node = head->next;  
            
            // point head to prev node
            head->next = prev_node;
            // make prev_node the new head
            prev_node = head;
            
            // head is now head->next
            head = tmp_node;
        }
        return prev_node;
    }
};