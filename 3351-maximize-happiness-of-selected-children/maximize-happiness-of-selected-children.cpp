class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(),happiness.end(),greater<int>());
        long long sum = 0;
        for(int i=0; i<k && (happiness[i] - i) > 0; i++){
            sum += happiness[i] - i;
        }
        return sum;
    }
};