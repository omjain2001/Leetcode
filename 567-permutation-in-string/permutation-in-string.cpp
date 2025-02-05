class Solution {
public:
    bool checkEqual(int a[26], int b[26]){
        for(int i=0; i<26; i++){
            if(a[i] != b[i]) return false;
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {

        // Complexity  = O(nlgn)

        // int n1 = s1.length(), n2 = s2.length();
        // if(n1 > n2) return false;
        // sort(s1.begin(), s1.end());
        // if(n1 == n2){
        //     sort(s2.begin(), s2.end());
        //     return s1 == s2;
        // }


        // string temp = "";
        // for(int i=0; i<n2; i++){
        //     temp += s2[i];
        //     if(i >= n1-1){
        //         string str = temp;
        //         sort(str.begin(), str.end());
        //         if(str == s1) return true;
        //         temp = temp.substr(1,n1-1);
        //     }
        // }
        // return false; 

        
        // Complexity = O(26 * n)

        if(s1.length() > s2.length()) return false;
        int a[26] = {0};
        for(auto i: s1){
            a[i-'a']++;
        }

        int b[26] = {0};
        int i=0;
        while(i < s1.length() && i < s2.length()){
            b[s2[i]-'a']++;
            i++;
        }

        if(checkEqual(a,b)) return true;

        while(i < s2.length()){
            b[s2[i]-'a']++;
            b[s2[i-s1.length()]-'a']--;
            if(checkEqual(a,b)) return true;
            i++;
        }
        return false;


    }
};