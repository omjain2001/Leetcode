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
    pair<ListNode*,ListNode*> reverse(ListNode *head, int k){
        ListNode *prev = NULL;
        ListNode *curr = head;
        int count = 0;
        while(curr && (count < k)){
            ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp; 
            count++;
        }
        return {prev, curr};
    }
    ListNode* recur(ListNode *head, int count, int k){
        if(head == NULL || count == 0) return head;
        auto [curr, next] = reverse(head, k);
        head->next = recur(next, count-1, k);
        return curr;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        ListNode *temp = head;
        while(temp){
            temp = temp->next;
            len++;
        }
        int grps = len/k;
        return recur(head, grps, k);
    }
};