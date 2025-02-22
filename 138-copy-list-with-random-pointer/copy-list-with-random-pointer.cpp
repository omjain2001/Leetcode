/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, int> old_map_idx;
        Node *curr = head;
        int count = 0;
        while(curr != NULL){
            old_map_idx[curr] = count;
            count++;
            curr = curr->next;
        }

        unordered_map<int,int> old_map;
        curr = head;
        while(curr != NULL){
            if(curr->random != NULL) old_map[old_map_idx[curr]] = old_map_idx[curr->random];
            else old_map[old_map_idx[curr]] = -1;
            curr = curr->next;
        }
        unordered_map<int, Node*> new_map;
        curr = head;
        Node *newhead = NULL;
        count = 0;
        while(curr){
            Node *newnode = new Node(curr->val);
            new_map[count] = newnode;
            if(newhead == NULL) newhead = newnode;
            curr = curr->next;
            count++;
        }
        new_map[count] = NULL;

        // Map random pointers
        curr = newhead;
        count = 0;
        while(curr != NULL){
            curr->next = new_map[count+1];
            if(old_map[count] >= 0){
                curr -> random = new_map[old_map[count]];
            }
            curr = curr->next;
            count++;
        }
        return newhead;
    }
};