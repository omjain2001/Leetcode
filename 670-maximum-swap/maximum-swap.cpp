class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        sort(s.begin(), s.end(), greater<char>());
        cout<<s<<endl;
        string temp = to_string(num);
        int i=0;
        while(i < s.length() && temp[i] == s[i]) i++;
        if(i == s.length()) return num;
        int idx = -1;
        for(int j=s.length()-1; j>=i; j--){
            if(temp[j] == s[i]){
                idx = j;
                break;
            }
        }
        // while(idx < s.length()-1 && temp[idx] == temp[idx+1]) idx++;
        swap(temp[i],temp[idx]);
        return stoi(temp);
    }
};