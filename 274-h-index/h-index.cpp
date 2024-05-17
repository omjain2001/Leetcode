class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int maxi = 0;
        int n = citations.size();
        int i = 0;
        while(i < n && citations[i] == 0) i++;
        while(i < n){
            if((n-i) <= citations[i]) maxi = max(maxi, (n-i));
            i++;
        }
        return maxi;
    }
};