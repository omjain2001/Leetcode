class Solution {
public:
    bool check(int capacity, int days, vector<int> &weights){
        int c = capacity;
        int dayCount = 1;
        for(int i=0; i<weights.size(); i++){
            if(weights[i] <= c){
                c -= weights[i];
            } else {
                dayCount++;
                c = capacity - weights[i];
            }
        }
        if(dayCount <= days) return true;
        return false;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int maxi = INT_MIN;
        int sum = 0;
        for(auto ele: weights){
            sum += ele;
            maxi = max(maxi, ele);
        }

        int l = maxi, h = sum;
        int minCapacity = 0;
        while(l <= h){
            int mid = (l+h)/2;
            if(check(mid, days, weights)){
                minCapacity = mid;
                h = mid-1;
            } else {
                l = mid+1;
            }
        }

        return minCapacity;
    }
};