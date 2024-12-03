class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s;
        for(auto ele: operations){
            if(ele == "+"){
                int n1 = s.top();
                s.pop();
                int n2 = s.top();
                s.push(n1);
                s.push(n1+n2);
            } else if(ele == "D"){
                s.push(s.top()*2);
            } else if(ele == "C"){
                s.pop();
            } else {
                s.push(stoi(ele));
            }
        }
        int sum = 0;
        while(!s.empty()){
            sum += s.top();
            s.pop();
        }
        return sum;
    }
};