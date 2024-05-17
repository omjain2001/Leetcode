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
    ListNode* insertionSortList(ListNode* head) {
        ListNode *curr = head;
        while(curr && curr -> next != NULL){
            if(curr -> next -> val < curr -> val){
                ListNode *next = curr -> next;
                if(next -> val < head -> val){
                    curr -> next = next -> next;
                    next -> next = head;
                    head = next;
                } else {
                    ListNode *temp = head;
                    while(temp -> next -> val < next -> val) temp = temp -> next;
                    ListNode *temp2 = temp -> next;
                    curr -> next = next -> next;
                    next -> next = temp -> next;
                    temp -> next = next;
                    // temp -> next = curr -> next;
                    // curr -> next = curr -> next -> next;
                    // temp -> next -> next = temp2;
                }
            } else curr = curr -> next;
        }
        return head;
    }
};