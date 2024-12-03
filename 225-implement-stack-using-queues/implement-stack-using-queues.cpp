class MyStack {
public:
    queue<int> q1, q2;
    MyStack() {
        
    }
    
    void push(int x) {
        if(!q1.empty()) q1.push(x);
        else q2.push(x);
    }
    
    int pop() {
        if(q1.empty()){
            int n = q2.size();
            while(n > 1){
                q1.push(q2.front());
                q2.pop();
                n--;
            }
            int ans = q2.front();
            q2.pop();
            return ans;
        } else {
            int n = q1.size();
            while(n > 1){
                q2.push(q1.front());
                q1.pop();
                n--;
            }
            int ans = q1.front();
            q1.pop();
            return ans;
        }
    }
    
    int top() {
        if(q1.empty()){
            int n = q2.size();
            while(n > 1){
                q1.push(q2.front());
                q2.pop();
                n--;
            }
            int ans = q2.front();
            q1.push(q2.front());
            q2.pop();
            return ans;
        } else {
            int n = q1.size();
            while(n > 1){
                q2.push(q1.front());
                q1.pop();
                n--;
            }
            int ans = q1.front();
            q2.push(q1.front());
            q1.pop();
            return ans;
        }  
    }
    
    bool empty() {
        if(q1.empty() && q2.empty()) return true;
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */