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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == NULL) return list2;
        if(list2 == NULL) return list1;
        ListNode *curr = NULL, *head = NULL;
        while(list1 != NULL && list2 != NULL){
            if(list1 -> val <= list2 -> val){
                if(curr == NULL){
                    curr = list1;
                    head = curr;
                } else {
                    curr -> next = list1;
                    curr = curr -> next;
                }
                list1 = list1 -> next;
            } else {
                if(curr == NULL){
                    curr = list2;
                    head = curr;
                } else {
                    curr -> next = list2;
                    curr = curr -> next;
                }
                list2 = list2 -> next;
            }
        }
        if(list1) curr -> next = list1;
        else curr -> next = list2;
        return head;
    }
};