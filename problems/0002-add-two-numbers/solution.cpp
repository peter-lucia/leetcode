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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // length of l1 and l2 can be different
        // don't forget carry at the end even if l1 and l2 are NULL
        int carry = 0;
        int tenPow = 0;
        // result stays the same even after prev is reassigned
        ListNode* result = new ListNode(0); // result's value is ignored since we return result->next
        ListNode* prev = result;

        while (l1 != NULL || l2 != NULL || carry) {
            int a = 0;
            int b = 0;
            if (l1 != NULL)
                a = l1->val;
            if (l2 != NULL)
                b = l2->val;
            int total = (a + b + carry);
            carry = 1 ? total >= 10 : 0;
            total = total % 10;
            ListNode* node = new ListNode(total);
            prev->next = node;

            // move prev, l1, l2 each to the next node
            if (l1 != NULL)
                l1 = l1->next;
            if (l2 != NULL)
                l2 = l2->next;
            prev = prev->next;
        }
        return result->next;
    }
};
