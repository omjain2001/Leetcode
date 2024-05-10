class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<long long> v(primes.size(),0);
        vector<long long> ans(1,1);
        while(ans.size() != n){
            long long mini = INT_MAX;
            long long idx = 0;
            for(int i=0; i<primes.size(); i++){
                if(mini > (primes[i] * ans[v[i]])){
                    mini = primes[i] * ans[v[i]];
                    idx = i;
                }
            }
            ans.push_back(primes[idx]*ans[v[idx]]);
            for(int i=0; i<primes.size(); i++){
                if(mini == primes[i]*ans[v[i]]) v[i]++;
            }
        }
        // for(auto ele: ans){
        //     cout<<ele<<" ";
        // }
        return ans.back();
    }
};