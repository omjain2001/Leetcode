class Solution {
public:
    bool validPalindrome(string s) {
       bool removed = false;
       int i = 0, j = s.length()-1;
       while(i <= j){
        if(s[i] == s[j]){
            i++;
            j--;
        }
        else {
            int start = i, end = j-1;
            bool isvalid = true;
            while(start <= end){
                if(s[start] != s[end]){
                    isvalid = false;
                    break;
                }
                start++;
                end--;
            }
            if(isvalid) return true;
            start = i+1;
            end = j;
            while(start <= end){
                if(s[start] != s[end]) return false;
                start++;
                end--;
            }
            return true;
        }
       }
       return true; 
    }
};