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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<pair<int,ListNode*>, vector<pair<int,ListNode*>>, greater<pair<int,ListNode*>>> pq;
        for(auto ele: lists){
            if(ele) pq.push({ele->val, ele});
        }
        ListNode *head = NULL;
        ListNode *prev = NULL;
        while(!pq.empty()){
            pair<int,ListNode*> p = pq.top();
            pq.pop();
            if(head == NULL){
                head = p.second;
                if(p.second->next) pq.push({p.second->next->val, p.second->next});
                prev = p.second;
            } else {
                prev->next = p.second;
                if(p.second->next) pq.push({p.second->next->val, p.second->next});
                prev = p.second;   
            }
        }

        return head;
    }
};