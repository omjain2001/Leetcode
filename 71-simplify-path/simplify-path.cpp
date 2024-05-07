class Solution {
public:
    string simplifyPath(string path) {
        int i = path.length()-1;
        int count = 0;
        string ans = "";
        while(i >= 0){
            string s = "";
            while(path[i] != '/'){
                s += path[i];
                i--;
            }
            if(s == "" || s == "."){
                i--;
                continue;
            }
            else if(s == "..") count++;
            else{
                if(count > 0) count--;
                else {reverse(s.begin(),s.end()); ans = "/" + s + ans;}
            }
            i--;
        }
        return ans == "" ? "/" : ans;
    }
};