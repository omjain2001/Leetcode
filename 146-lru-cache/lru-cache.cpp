class LRUCache {
public:

    class Node {
        public:
            int key;
            int val;
            Node *prev;
            Node *next;

            Node(){
                this->key = 0;
                this->val = 0;
                this->prev = NULL;
                this->next = NULL;
            }

            Node(int key, int val){
                this->key = key;
                this->val = val;
                this->prev = NULL;
                this->next = NULL;
            }
    };

    int capacity = 0;
    Node *head, *tail;
    unordered_map<int, Node*> m;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(-1,-1);
        this->tail = new Node(1000,1000);
        this->tail->prev = this->head;
        this->head->next = this->tail;
    }

    void printLL(){
        Node *temp = head;
        cout<<"Forward Pass: ";
        while(temp != NULL){
            cout<<temp->val<<" ";
            temp = temp->next;
        }
        cout<<endl;
        cout<<"Reverse Pass: ";
        temp = tail;
        while(temp != NULL){
            cout<<temp->val<<" ";
            temp = temp->prev;
        }
        cout<<endl;
    }
    
    int get(int key) {
        if(this->m.find(key) != this->m.end()){
            Node *keynode = this->m[key];
            keynode->prev->next = keynode->next;
            keynode->next->prev = keynode->prev;
            keynode->next = NULL;
            keynode->prev = NULL;
            // Node *newnode = new Node(keynode -> val);
            keynode->prev = this->head;
            keynode->next = this->head->next;
            this->head->next->prev = keynode;
            this->head->next = keynode;
            // this->m[key] = newnode;
            // delete keynode;
            // keynode = NULL;
            // printLL();
            // cout<<"Get: "<<keynode->val<<endl;
            return keynode->val;
        } else return -1;
    }
    
    void put(int key, int value) {
        if(this->m.find(key) != this->m.end()){
            Node *tempnode = this->m[key];
            tempnode->val = value;
            tempnode->prev->next = tempnode->next;
            tempnode->next->prev = tempnode->prev;
            tempnode->next = this->head->next;
            tempnode->prev = this->head;
            tempnode->next->prev = tempnode;
            this->head->next = tempnode;
            
        }
        else if(this->m.size() == this->capacity){
            Node *delnode = this->tail->prev;
            delnode->prev->next = delnode->next;
            delnode->next->prev = delnode->prev;
            this->m.erase(delnode->key);
            delnode->next = NULL;
            delnode->prev = NULL;
            delete delnode;
            delnode = NULL;

            Node *newnode = new Node(key,value);
            this->m[key] = newnode;
            newnode->prev = this->head;
            newnode->next = this->head->next;
            this->head->next->prev = newnode;
            this->head->next = newnode;
            // printLL();
            // cout<<"Remove and Put: "<<head->next->val<<"->"<<tail->prev->val<<endl;
        } else {
            Node *newnode = new Node(key,value);
            this->m[key] = newnode;
            newnode->prev = this->head;
            newnode->next = this->head->next;
            this->head->next->prev = newnode;
            this->head->next = newnode;
            // printLL();
            // cout<<"Put: "<<head->next->val<<"->"<<tail->prev->val<<endl;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */