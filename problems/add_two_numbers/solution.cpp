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
    ListNode* addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode dummyHead(0);
        ListNode *current = &dummyHead;
        int carry = 0;
        while (l1 || l2 || carry) {
            int a;
            int b;
            int total;
            if (l1) {
                //std::cout << "got here..\n";
                a = l1->val;
                l1 = l1->next;
            }
            else {
                a = 0;
                //std::cout << "l1 is out...\n";
                l1 = nullptr;
            }
            if (l2) {
                b = l2->val;
                //std::cout << "got here too\n";
                l2 = l2->next;
            }
            else {
                b = 0;
                std::cout << "l2 is out..\n";
                l2 = nullptr;
            }
            total = a + b + carry;
           // std::cout << "Current total: " << total % 10 << "\n";
            current->next = new ListNode(total % 10);
            carry = total / 10;
            current = current->next;



        }
        return dummyHead.next;
    }
};

