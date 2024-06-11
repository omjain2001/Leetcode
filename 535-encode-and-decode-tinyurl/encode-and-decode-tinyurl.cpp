class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        string ans = "";
        int count = 0;
        for(auto ele: longUrl){
            if(ele == '/'){
                ans += '@';
            } else ans += ele;
        }
        return ans;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string ans = "";
        for(auto ele: shortUrl){
            if(ele == '@') ans += '/';
            else ans += ele;
        }
        return ans;
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));