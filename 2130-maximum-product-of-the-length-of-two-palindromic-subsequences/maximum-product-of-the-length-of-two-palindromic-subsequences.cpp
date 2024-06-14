class Solution {
public:
    int maxProduct(string s) {
        int n = s.length();
        unordered_map<int,int> m;

        for(int i=1; i<(1<<n); i++){
            string subseq = "";
            for(int j=0; j<n; j++){
                if((i & (1 << j)) != 0) subseq += s[j];
            }
            string temp = subseq;
            reverse(subseq.begin(), subseq.end());
            if(temp == subseq) m[i] = subseq.length();
        }
        int maxi = INT_MIN;
        for(auto m1: m){
            for(auto m2: m){
                if((m1.first & m2.first) == 0) maxi = max(maxi, m1.second * m2.second);
            }
        }

        return maxi;
    }
};