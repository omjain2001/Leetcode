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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ListNode *curr = head;
        while(curr){
            curr = curr->next;
            length++;
        }
        int left = length-n;
        int count = 1;
        curr = head;
        while(count < left){
            curr = curr -> next;
            count++;
        }
        ListNode *temp = NULL;
        if(left == 0){
            temp = head -> next;
            head->next = NULL;
            delete head;
            head = temp;
        } else {
            temp = curr->next->next;
            curr->next->next = NULL;
            delete curr->next;
            curr->next = temp;
        }
        return head; 
    }
};