class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long sum = 0;
        sort(piles.begin(), piles.end());
        for(auto ele: piles) sum += ele;
        long long l = 1, r = sum;
        while(l <= r){
            long long mid = (l+r)/2;
            int count = 0;
            for(int i=0; i<piles.size(); i++){
                count += ceil((double)piles[i]/mid);
            }
            if(count <= h){
                r = mid-1;
            } else l = mid+1;
        }
        return l;
    }
};