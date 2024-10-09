class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        vector<int> pairs;
        sort(potions.begin(), potions.end());
        for(auto ele: spells){
            int l = 0, r = potions.size()-1;
            while(l <= r){
                int mid = (l+r)/2;
                long long prod = (long long)potions[mid] * ele;
                if(prod >= success) r = mid-1;
                else l = mid+1;
            }
            pairs.push_back(potions.size() - l);
        }
        return pairs;
    }
};