class Solution {
public:
    int numSteps(string s) {
        int count = 0;
        vector<char> v(s.length());
        for(int i=0; i<s.length(); i++){
            v[i] = s[i];
        }
        for(int i=s.length()-1; i>0; i--){
            if(v[i] == '0') count++;
            else{
                count++;
                v[i] = '1';
                while(i >= 0 && v[i] == '1'){
                    count++;
                    i--;
                }
                if(i >= 0){
                    v[i] = '1';
                    i++;
                }
            }
        }
        return count;
    }
};