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

    ListNode* reverseList(ListNode* head){
        ListNode *prev = NULL;
        ListNode *curr = head;
        ListNode *next = head;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    void reorderList(ListNode* head) {
        ListNode *fast = head, *slow = head;
        while(fast->next != NULL && fast -> next -> next != NULL){
            fast = fast -> next -> next;
            slow = slow -> next;
        }
        ListNode *temp = slow->next;
        slow->next = NULL;
        slow = temp;
        ListNode *head2 = reverseList(slow);
        ListNode *curr1 = head;
        while(curr1 != NULL && head2 != NULL){
            temp = head2->next;
            head2->next = curr1->next;
            curr1->next = head2;
            curr1 = curr1->next->next;
            head2 = temp;
        }
    }
};