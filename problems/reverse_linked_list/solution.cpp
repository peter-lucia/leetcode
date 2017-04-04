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
    ListNode* reverseList(ListNode* head) {
    //    if (head == nullptr) {
    //        return head;
    //    }
    
        ListNode *temp = NULL, *nextNode = NULL;
        while (head) {
            nextNode = head->next;
            head->next = temp;
            temp = head;
            head = nextNode;
        }
        return temp;
    }
};