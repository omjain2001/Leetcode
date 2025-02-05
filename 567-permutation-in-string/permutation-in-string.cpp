class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.length(), n2 = s2.length();
        if(n1 > n2) return false;
        sort(s1.begin(), s1.end());
        if(n1 == n2){
            sort(s2.begin(), s2.end());
            return s1 == s2;
        }


        string temp = "";
        for(int i=0; i<n2; i++){
            temp += s2[i];
            if(i >= n1-1){
                string str = temp;
                sort(str.begin(), str.end());
                if(str == s1) return true;
                temp = temp.substr(1,n1-1);
            }
        }
        return false; 
    }
};