class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int count = 0;
        int n = piles.size();
        sort(piles.begin(), piles.end());
        int left = 0;
        int right = n-1;
        int mid = n-2;

        while(left < mid){
            count += piles[mid];
            left++;
            right = mid-1;
            mid = right-1;
        }

        return count;
    }
};