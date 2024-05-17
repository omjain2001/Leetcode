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
    ListNode *merge(ListNode *head1, ListNode *head2){
        ListNode *head = NULL;
        if(head1 -> val <= head2 -> val){
            head = head1;
            head1 = head1 -> next;
        } else {
            head = head2;
            head2 = head2 -> next;
        }
        ListNode *curr = head;
        while(head1 != NULL && head2 != NULL){
            if(head1 -> val < head2 -> val){
                curr -> next = head1;
                curr = head1;
                head1 = head1 -> next;
            } else {
                curr -> next = head2;
                curr = head2;
                head2 = head2 -> next;
            }
        }
        if(head1) curr -> next = head1;
        else curr -> next = head2;
        return head;
    }
    ListNode* mergeSort(ListNode *head){
        if(head == NULL || head -> next == NULL) return head;
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast -> next != NULL && fast -> next -> next != NULL){
            slow = slow -> next;
            fast = fast -> next -> next;
        }

        ListNode *temp = slow -> next;
        slow -> next = NULL;
        ListNode *head1 = mergeSort(head);
        ListNode *head2 = mergeSort(temp);
        return merge(head1,head2);
    }
    ListNode* sortList(ListNode* head) {
        return mergeSort(head);
    }
};